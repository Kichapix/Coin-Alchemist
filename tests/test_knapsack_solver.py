from algorithms.knapsack_solver import KnapsackSolver
from models.goal import Goal


def test_knapsack_solver():

    goals = [
        Goal("A", 100, 10, "Техника"),
        Goal("B", 50, 5, "Техника")
    ]

    solver = KnapsackSolver()

    result = solver.solve(
        goals,
        100
    )

    assert result["total_priority"] >= 10