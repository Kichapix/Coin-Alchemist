from ui.priority_selector import PrioritySelector
from ui.category_selector import CategorySelector
from models.goal import Goal
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox
)

from PySide6.QtGui import QIntValidator


class AddGoalDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.goal = None

        self.setWindowTitle("Добавить цель")

        self.resize(420, 500)

        self.setStyleSheet("""
            background-color: #111827;
            color: white;
        """)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Название

        name_label = QLabel("Название цели")
        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "Например: Новый ноутбук"
        )
        # Стоимость

        cost_label = QLabel("Стоимость")
        self.cost_input = QLineEdit()

        self.cost_input.setPlaceholderText(
            "Например: 60000"
        )

        self.cost_input.setValidator(
            QIntValidator(0, 100000000)
        )

        # Приоритет

        priority_label = QLabel("Приоритет")
        self.priority_selector = PrioritySelector()

        # Категория

        category_label = QLabel("Категория")
        self.category_selector = CategorySelector()

        field_style = """
        QLineEdit, QComboBox {
            background-color: #0F172A;
            color: white;
            border: 2px solid #1E293B;
            border-radius: 10px;
            padding: 10px;
            font-size: 15px;
        }

        QLineEdit:focus,
        QComboBox:focus {
            border: 2px solid #7C3AED;
        }

        QComboBox QAbstractItemView {
            background-color: #0F172A;
            color: white;
            selection-background-color: #7C3AED;
            selection-color: white;
            border: 1px solid #1E293B;
        }
        """

        error_style = """
        QLineEdit {
            background-color: #0F172A;
            color: white;
            border: 2px solid #EF4444;
            border-radius: 10px;
            padding: 10px;
            font-size: 15px;
        }
        """

        self.name_input.setStyleSheet(field_style)

        self.cost_input.setStyleSheet(field_style)

        self.field_style = field_style
        self.error_style = error_style

        # Кнопка

        save_button = QPushButton(
            "Сохранить"
        )

        save_button.setFixedHeight(50)

        save_button.setStyleSheet("""
        QPushButton {
            background-color: #7C3AED;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #8B5CF6;
        }

        QPushButton:pressed {
            background-color: #6D28D9;
        }
        """)

        save_button.clicked.connect(
            self.save_goal
        )

        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        layout.addWidget(cost_label)
        layout.addWidget(self.cost_input)

        layout.addWidget(priority_label)
        layout.addWidget(self.priority_selector)

        layout.addWidget(category_label)
        layout.addWidget(self.category_selector)

        layout.addStretch()

        layout.addWidget(save_button)

    def save_goal(self):

        self.name_input.setStyleSheet(
            self.field_style
        )

        self.cost_input.setStyleSheet(
            self.field_style
        )

        has_error = False

        name = self.name_input.text().strip()

        cost = self.cost_input.text().strip()

        priority = self.priority_selector.get_value()

        category = self.category_selector.get_value()

        if not name:
            self.name_input.setStyleSheet(
                self.error_style
            )

            has_error = True

        if not cost:
            self.cost_input.setStyleSheet(
                self.error_style
            )

            has_error = True

        if has_error:
            return

        self.goal = Goal(
            name=name,
            cost=int(cost),
            priority=priority,
            category=category
        )

        self.accept()