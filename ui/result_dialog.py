from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton
)

from PySide6.QtCore import Qt


class ResultDialog(QDialog):

    def __init__(self, title, text):
        super().__init__()

        self.setWindowTitle(title)

        self.resize(400, 300)

        self.setStyleSheet("""
            QDialog {
                background-color: #111827;
            }
        """)

        layout = QVBoxLayout(self)

        title_label = QLabel(title)

        title_label.setAlignment(
            Qt.AlignCenter
        )

        title_label.setStyleSheet("""
            color: white;
            font-size: 22px;
            font-weight: bold;
        """)

        content_label = QLabel(text)

        content_label.setWordWrap(True)

        content_label.setStyleSheet("""
            color: #CBD5E1;
            font-size: 15px;
        """)

        content_label.setAlignment(
            Qt.AlignCenter
        )

        close_button = QPushButton("Закрыть")

        close_button.setStyleSheet("""
        QPushButton {
            background-color: #7C3AED;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 12px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #8B5CF6;
        }
        """)

        close_button.clicked.connect(
            self.accept
        )

        layout.addWidget(title_label)
        layout.addWidget(content_label)
        layout.addStretch()
        layout.addWidget(close_button)