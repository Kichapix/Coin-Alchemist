from dataclasses import dataclass, asdict

@dataclass
class Goal:
    name: str
    cost: int
    priority: int
    category: str

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            cost=data["cost"],
            priority=data["priority"],
            category=data["category"]
        )