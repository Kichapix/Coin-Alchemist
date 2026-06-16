class GreedySolver:

    def solve(self, goals, budget):

        sorted_goals = sorted(
            goals,
            key=lambda goal:
            goal.priority / goal.cost,
            reverse=True
        )

        selected_goals = []

        remaining_budget = budget

        for goal in sorted_goals:

            if goal.cost <= remaining_budget:

                selected_goals.append(goal)

                remaining_budget -= goal.cost

        return {
            "goals": selected_goals,
            "total_cost": sum(
                goal.cost
                for goal in selected_goals
            ),
            "total_priority": sum(
                goal.priority
                for goal in selected_goals
            )
        }