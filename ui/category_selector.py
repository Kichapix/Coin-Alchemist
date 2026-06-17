from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class CategorySelector(QWidget):

    value_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.selected_category = "Техника"

        self.buttons = {}

        layout = QHBoxLayout()
        layout.setSpacing(10)

        self.setLayout(layout)

        categories = {
            "Техника": "🖥",
            "Образование": "🎓",
            "Путешествия": "✈",
            "Дом": "🏠",
            "Другое": "📦"
        }

        for category, icon in categories.items():

            button = QPushButton(
                f"{icon} {category}"
            )

            button.clicked.connect(
                lambda checked=False,
                c=category:
                self.select_category(c)
            )

            self.buttons[category] = button

            layout.addWidget(button)

        self.update_styles()

    def select_category(self, category):

        self.selected_category = category

        self.update_styles()

        self.value_changed.emit(category)

    def get_value(self):

        return self.selected_category

    def update_styles(self):

        for category, button in self.buttons.items():

            if category == self.selected_category:

                button.setStyleSheet("""
                    QPushButton {
                        background-color: #7C3AED;
                        color: white;
                        border: none;
                        border-radius: 10px;
                        padding: 10px 16px;
                        font-weight: bold;
                    }
                """)

            else:

                button.setStyleSheet("""
                    QPushButton {
                        background-color: #0F172A;
                        color: #CBD5E1;
                        border: 2px solid #1E293B;
                        border-radius: 10px;
                        padding: 10px 16px;
                    }

                    QPushButton:hover {
                        border: 2px solid #7C3AED;
                    }
                """)