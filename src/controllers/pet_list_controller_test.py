from src.models.sqllite.entities.pets import PetsTable
from .pet_list_controller import PetListController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name="Rex", type="Dog", id=4),
            PetsTable(name="Buddy", type="Cat", id=2),
        ]

def test_list_pets():
    controller = PetListController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 2,
            "attributes": [
                {"name": "Rex", "id": 4},
                {"name": "Buddy", "id": 2}
            ]
        }
    }

    assert response == expected_response
