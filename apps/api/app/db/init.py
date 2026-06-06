from app.db.base import Base
from app.db.session import engine
from app.models import Family, FamilyMember, FamilyMembership, User  # noqa: F401


def initialize_database() -> None:
    Base.metadata.create_all(bind=engine)
