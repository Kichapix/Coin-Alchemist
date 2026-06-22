from algorithms.greedy_solver import GreedySolver
from models.goal import Goal


def test_greedy_solver():

    goals = [
        Goal("A", 100, 10, "Техника"),
        Goal("B", 50, 5, "Техника")
    ]

    solver = GreedySolver()

    result = solver.solve(
        goals,
        100
    )

    assert result["total_cost"] <= 100