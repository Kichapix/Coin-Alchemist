from models.goal import Goal


def test_goal_to_dict():

    goal = Goal(
        "Ноутбук",
        60000,
        10,
        "Техника"
    )

    data = goal.to_dict()

    assert data["name"] == "Ноутбук"
    assert data["cost"] == 60000
    assert data["priority"] == 10
    assert data["category"] == "Техника"


def test_goal_from_dict():

    data = {
        "name": "Книга",
        "cost": 500,
        "priority": 3,
        "category": "Образование"
    }

    goal = Goal.from_dict(data)

    assert goal.name == "Книга"
    assert goal.cost == 500