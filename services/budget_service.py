from services.storage_service import StorageService


class BudgetService:

    def __init__(self):
        self.goals = []
        self.storage = StorageService()

    def add_goal(self, goal):
        self.goals.append(goal)

    def remove_goal(self, goal):
        self.goals.remove(goal)

    def get_goals(self):
        return self.goals

    def save_goals(self, filepath):
        self.storage.save_goals(
            self.goals,
            filepath
        )

    def load_goals(self, filepath):
        self.goals = self.storage.load_goals(
            filepath
        )