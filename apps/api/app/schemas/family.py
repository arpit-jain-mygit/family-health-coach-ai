from pydantic import BaseModel, ConfigDict


class FamilyCreate(BaseModel):
    name: str
    goals: dict | None = None
    preferences: dict | None = None


class FamilyUpdate(BaseModel):
    name: str | None = None
    goals: dict | None = None
    preferences: dict | None = None


class FamilyResponse(BaseModel):
    id: str
    name: str
    goals: dict | None = None
    preferences: dict | None = None

    model_config = ConfigDict(from_attributes=True)
