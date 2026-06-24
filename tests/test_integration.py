from services.budget_service import BudgetService
from algorithms.knapsack_solver import KnapsackSolver
from models.goal import Goal


def test_budget_service_and_solver_integration():

    service = BudgetService()

    service.add_goal(
        Goal(
            "Ноутбук",
            60000,
            8,
            "Техника"
        )
    )

    service.add_goal(
        Goal(
            "Книга",
            1000,
            3,
            "Образование"
        )
    )

    solver = KnapsackSolver()

    result = solver.solve(
        service.get_goals(),
        61000
    )

    assert result["total_cost"] == 61000
    assert result["total_priority"] == 11
    assert len(result["goals"]) == 2