from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class PrioritySelector(QWidget):

    value_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.value = 5

        self.buttons = []

        layout = QHBoxLayout()
        layout.setSpacing(6)

        self.setLayout(layout)

        for i in range(10):
            button = QPushButton(str(i + 1))

            button.setFixedSize(40, 40)

            button.clicked.connect(
                lambda checked=False, n=i + 1:
                self.set_value(n)
            )

            self.buttons.append(button)

            layout.addWidget(button)

        self.update_buttons()

    def set_value(self, value):
        self.value = value

        self.update_buttons()

        self.value_changed.emit(value)

    def get_value(self):
        return self.value

    def update_buttons(self):

        for index, button in enumerate(self.buttons):

            if index < self.value:

                button.setStyleSheet("""
                    QPushButton {
                        background-color: #7C3AED;
                        color: white;
                        border: none;
                        border-radius: 12px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                """)

            else:

                button.setStyleSheet("""
                    QPushButton {
                        background-color: #1E293B;
                        color: #94A3B8;
                        border: none;
                        border-radius: 12px;
                        font-size: 14px;
                        font-weight: bold;
                    }
                """)