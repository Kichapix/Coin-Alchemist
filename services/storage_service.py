import json
from models.goal import Goal

class StorageService:

    def save_goals(self, goals, filepath):

        goals_data = []

        for goal in goals:
            goals_data.append(goal.to_dict())

        data = {
            "goals": goals_data
        }

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def load_goals(self, filepath):

        with open(filepath, "r", encoding="utf-8") as file:

            data = json.load(file)

        goals = []

        for goal_data in data["goals"]:

            goals.append(

                Goal.from_dict(goal_data)

            )

        return goals