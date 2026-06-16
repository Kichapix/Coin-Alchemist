class KnapsackSolver:

    def solve(self, goals, budget):
        n = len(goals)

        dp = [
            [0] * (budget + 1)
            for _ in range(n + 1)
        ]

        for i in range(1, n + 1):

            goal = goals[i - 1]

            cost = goal.cost
            value = goal.priority

            for current_budget in range(budget + 1):

                if cost <= current_budget:

                    dp[i][current_budget] = max(
                        dp[i - 1][current_budget],

                        dp[i - 1][current_budget - cost]
                        + value
                    )

                else:

                    dp[i][current_budget] = (
                        dp[i - 1][current_budget]
                    )

        selected_goals = []

        current_budget = budget

        for i in range(n, 0, -1):

            if (
                    dp[i][current_budget]
                    !=
                    dp[i - 1][current_budget]
            ):
                goal = goals[i - 1]

                selected_goals.append(goal)

                current_budget -= goal.cost

        selected_goals.reverse()

        return {
            "goals": selected_goals,
            "total_cost": sum(goal.cost for goal in selected_goals),
            "total_priority": sum(goal.priority for goal in selected_goals)
        }