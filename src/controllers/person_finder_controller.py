from typing import Dict
from src.models.sqllite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqllite.entities.people import PeopleTable
from src.errors.errors_types.http_not_found import HttpNotFoundError
from .interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    # pylint: disable=too-few-public-methods
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_id(person_id)
        response = self.__format_response(person)
        return response

    def __find_person_id(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.get_person(person_id)
        if not person:
            raise HttpNotFoundError("Pessoa não encontrada")

        return person

    def __format_response(self, person: PeopleTable) -> Dict:
        return {
            "data": {
                "type": "person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name" : person.pet_name,
                    "pet_type": person.pet_type
                }
            }
        }
