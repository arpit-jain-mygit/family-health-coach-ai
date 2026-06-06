from fastapi import APIRouter, Depends, status

from app.api.deps import CurrentUserId, DatabaseSession
from app.schemas.family import FamilyCreate, FamilyResponse, FamilyUpdate
from app.services.family_service import FamilyService

router = APIRouter(prefix="/families", tags=["families"])


def get_family_service() -> FamilyService:
    return FamilyService()


@router.get("", response_model=list[FamilyResponse])
def list_families(
    db: DatabaseSession,
    current_user_id: CurrentUserId,
    family_service: FamilyService = Depends(get_family_service),
) -> list[FamilyResponse]:
    return family_service.list_families_for_user(db, current_user_id)


@router.post("", response_model=FamilyResponse, status_code=status.HTTP_201_CREATED)
def create_family(
    payload: FamilyCreate,
    db: DatabaseSession,
    current_user_id: CurrentUserId,
    family_service: FamilyService = Depends(get_family_service),
) -> FamilyResponse:
    return family_service.create_family(db, current_user_id, payload)


@router.get("/{family_id}", response_model=FamilyResponse)
def get_family(
    family_id: str,
    db: DatabaseSession,
    current_user_id: CurrentUserId,
    family_service: FamilyService = Depends(get_family_service),
) -> FamilyResponse:
    return family_service.get_family_for_user(db, current_user_id, family_id)


@router.patch("/{family_id}", response_model=FamilyResponse)
def update_family(
    family_id: str,
    payload: FamilyUpdate,
    db: DatabaseSession,
    current_user_id: CurrentUserId,
    family_service: FamilyService = Depends(get_family_service),
) -> FamilyResponse:
    return family_service.update_family(db, current_user_id, family_id, payload)


@router.delete("/{family_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_family(
    family_id: str,
    db: DatabaseSession,
    current_user_id: CurrentUserId,
    family_service: FamilyService = Depends(get_family_service),
) -> None:
    family_service.delete_family(db, current_user_id, family_id)
