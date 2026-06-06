from datetime import datetime
from uuid import uuid4

from sqlalchemy import DateTime, ForeignKey, JSON, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class FamilyMember(Base):
    __tablename__ = "family_members"

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid4()))
    family_id: Mapped[str] = mapped_column(String, ForeignKey("families.id"), index=True)
    user_id: Mapped[str | None] = mapped_column(String, ForeignKey("users.id"), index=True)
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int | None]
    gender: Mapped[str | None] = mapped_column(String)
    height_cm: Mapped[float | None] = mapped_column(Numeric(6, 2))
    weight_kg: Mapped[float | None] = mapped_column(Numeric(6, 2))
    waist_cm: Mapped[float | None] = mapped_column(Numeric(6, 2))
    activity_level: Mapped[str | None] = mapped_column(String)
    medical_conditions: Mapped[list | None] = mapped_column(JSON)
    medications: Mapped[list | None] = mapped_column(JSON)
    allergies: Mapped[list | None] = mapped_column(JSON)
    food_preferences: Mapped[list | None] = mapped_column(JSON)
    meal_timing_preferences: Mapped[dict | None] = mapped_column(JSON)
    exercise_preferences: Mapped[dict | None] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
