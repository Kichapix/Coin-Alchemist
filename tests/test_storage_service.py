from services.storage_service import StorageService
from models.goal import Goal


def test_save_and_load_goals(tmp_path):

    filepath = tmp_path / "goals.json"

    goals = [
        Goal(
            "Книга",
            500,
            3,
            "Образование"
        )
    ]

    storage = StorageService()

    storage.save_goals(
        goals,
        filepath
    )

    loaded_goals = storage.load_goals(
        filepath
    )

    assert len(loaded_goals) == 1
    assert loaded_goals[0].name == "Книга"