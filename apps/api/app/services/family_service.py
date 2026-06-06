from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.family import Family, FamilyMembership
from app.schemas.family import FamilyCreate, FamilyUpdate

FAMILY_ADMIN = "FAMILY_ADMIN"


class FamilyService:
    def list_families_for_user(self, db: Session, user_id: str) -> list[Family]:
        statement = (
            select(Family)
            .join(FamilyMembership, FamilyMembership.family_id == Family.id)
            .where(FamilyMembership.user_id == user_id)
        )
        return list(db.scalars(statement))

    def create_family(self, db: Session, user_id: str, payload: FamilyCreate) -> Family:
        existing_membership = db.scalar(
            select(FamilyMembership).where(FamilyMembership.user_id == user_id)
        )
        if existing_membership is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User already belongs to a family.",
            )

        family = Family(
            name=payload.name,
            goals=payload.goals,
            preferences=payload.preferences,
        )
        db.add(family)
        db.flush()
        membership = FamilyMembership(
            family_id=family.id,
            user_id=user_id,
            role=FAMILY_ADMIN,
        )
        db.add(membership)
        db.commit()
        db.refresh(family)
        return family

    def get_family_for_user(self, db: Session, user_id: str, family_id: str) -> Family:
        self.ensure_user_has_family_access(db, user_id, family_id)
        family = db.get(Family, family_id)
        if family is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Family not found.")
        return family

    def update_family(
        self,
        db: Session,
        user_id: str,
        family_id: str,
        payload: FamilyUpdate,
    ) -> Family:
        family = self.get_family_for_user(db, user_id, family_id)
        if payload.name is not None:
            family.name = payload.name
        if payload.goals is not None:
            family.goals = payload.goals
        if payload.preferences is not None:
            family.preferences = payload.preferences
        db.commit()
        db.refresh(family)
        return family

    def delete_family(self, db: Session, user_id: str, family_id: str) -> None:
        family = self.get_family_for_user(db, user_id, family_id)
        db.delete(family)
        db.commit()

    def ensure_user_has_family_access(self, db: Session, user_id: str, family_id: str) -> None:
        statement = select(FamilyMembership).where(
            FamilyMembership.family_id == family_id,
            FamilyMembership.user_id == user_id,
        )
        membership = db.scalar(statement)
        if membership is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User does not have access to this family.",
            )
