from services.budget_service import BudgetService
from models.goal import Goal


def test_add_goal():

    service = BudgetService()

    goal = Goal(
        "Книга",
        500,
        3,
        "Образование"
    )

    service.add_goal(goal)

    assert len(
        service.get_goals()
    ) == 1