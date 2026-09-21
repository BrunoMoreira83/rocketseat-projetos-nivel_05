# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from sqlalchemy import Column, BIGINT, String
from src.models.sqllite.settings.base import Base

class PeopleTable(Base):
    __tablename__ = "people"

    id = Column(BIGINT, primary_kay=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, Foreignkey="pets.id")

    def __repr__(self):
        return (
        f"People [first_name={self.first_name},"
        f"last_name={self.last_name}, pet_id={self.pet_id}]"
        )
