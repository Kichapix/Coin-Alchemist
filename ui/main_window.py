from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QHeaderView
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QWidget,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QFrame,
    QLabel,
    QPushButton,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coin Alchemist")
        self.resize(1280, 800)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #0F172A;
            }
        """)

        # Центральный виджет
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Главный layout
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        central_widget.setLayout(main_layout)

        # ===== SIDEBAR =====

        sidebar = QFrame()
        sidebar.setFixedWidth(220)

        sidebar.setStyleSheet("""
            background-color: #111827;
            border-radius: 12px;
        """)

        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        # Логотип
        logo = QLabel("🧙")
        logo.setAlignment(Qt.AlignCenter)

        logo.setStyleSheet("""
            color: #7C3AED;
            font-size: 42px;
            border: none;
        """)

        # Заголовок
        title = QLabel("Coin Alchemist")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            color: #F8FAFC;
            font-size: 22px;
            font-weight: bold;
            border: none;
        """)

        # Подзаголовок
        subtitle = QLabel("Turn goals into decisions")
        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""
            color: #94A3B8;
            font-size: 12px;
            border: none;
        """)

        sidebar_layout.addSpacing(30)

        sidebar_layout.addWidget(logo)
        sidebar_layout.addWidget(title)
        sidebar_layout.addWidget(subtitle)

        sidebar_layout.addSpacing(40)

        goals_button = QPushButton("🎯  Цели")
        opt_button = QPushButton("📈  Оптимизация")
        compare_button = QPushButton("⚖️  Сравнение")
        saved_button = QPushButton("📄  Планы")
        settings_button = QPushButton("⚙️  Настройки")

        menu_style = """
        QPushButton {
            background-color: transparent;
            color: #CBD5E1;
            border: none;
            padding: 12px;
            text-align: left;
            font-size: 14px;
            border-radius: 8px;
        }

        QPushButton:hover {
            background-color: #1E293B;
        }

        QPushButton:pressed {
            background-color: #334155;
        }
        """

        goals_button.setStyleSheet(menu_style)
        opt_button.setStyleSheet(menu_style)
        compare_button.setStyleSheet(menu_style)
        saved_button.setStyleSheet(menu_style)
        settings_button.setStyleSheet(menu_style)

        sidebar_layout.addWidget(goals_button)
        sidebar_layout.addWidget(opt_button)
        sidebar_layout.addWidget(compare_button)
        sidebar_layout.addWidget(saved_button)
        sidebar_layout.addWidget(settings_button)

        sidebar_layout.addStretch()

        # ===== CONTENT =====

        content = QFrame()

        content.setStyleSheet("""
            background-color: #0F172A;
        """)

        content_layout = QVBoxLayout()
        content.setLayout(content_layout)

        content_layout.setAlignment(Qt.AlignTop)

        page_title = QLabel("Мои финансовые цели")

        page_title.setStyleSheet("""
            color: #F8FAFC;
            font-size: 30px;
            font-weight: bold;
            border: none;
        """)

        page_subtitle = QLabel(
            "Добавляйте цели, указывайте бюджет и находите оптимальный план"
        )

        page_subtitle.setStyleSheet("""
            color: #94A3B8;
            font-size: 14px;
            border: none;
        """)

        content_layout.addSpacing(40)
        content_layout.addWidget(page_title)
        content_layout.addSpacing(8)
        content_layout.addWidget(page_subtitle)
        content_layout.addSpacing(30)

        budget_card = QFrame()

        budget_card.setFixedSize(320, 140)

        budget_card.setStyleSheet("""
            background-color: #111827;
            border-radius: 12px;
        """)

        budget_layout = QVBoxLayout()
        budget_card.setLayout(budget_layout)

        budget_title = QLabel("Ваш бюджет")

        budget_title.setStyleSheet("""
            color: #F8FAFC;
            font-size: 14px;
            font-weight: bold;
            border: none;
        """)

        budget_input = QLineEdit()

        budget_input.setPlaceholderText("50000")

        budget_input.setValidator(
            QIntValidator(0, 100000000)
        )

        budget_input.setStyleSheet("""
            QLineEdit {
                background-color: #0F172A;
                color: white;
                border: 2px solid #7C3AED;
                border-radius: 8px;
                padding: 10px;
                font-size: 16px;
            }
        """)

        budget_layout.addWidget(budget_title)
        budget_layout.addSpacing(10)
        budget_layout.addWidget(budget_input)

        content_layout.addWidget(budget_card)
        content_layout.addSpacing(20)

        table_title = QLabel("Список целей")

        table_title.setStyleSheet("""
            color: #F8FAFC;
            font-size: 20px;
            font-weight: bold;
            border: none;
        """)

        content_layout.addWidget(table_title)

        goals_table = QTableWidget()

        goals_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        goals_table.setEditTriggers(

            QAbstractItemView.NoEditTriggers

        )

        goals_table.setColumnCount(4)

        goals_table.setHorizontalHeaderLabels([
            "Название",
            "Категория",
            "Стоимость",
            "Приоритет"
        ])

        goals_table.setRowCount(3)

        goals_table.setItem(
            0, 0,
            QTableWidgetItem("Ноутбук")
        )

        goals_table.setItem(
            0, 1,
            QTableWidgetItem("Техника")
        )

        goals_table.setItem(
            0, 2,
            QTableWidgetItem("60000")
        )

        goals_table.setItem(
            0, 3,
            QTableWidgetItem("10")
        )

        goals_table.setItem(
            1, 0,
            QTableWidgetItem("Курсы Python")
        )

        goals_table.setItem(
            1, 1,
            QTableWidgetItem("Образование")
        )

        goals_table.setItem(
            1, 2,
            QTableWidgetItem("15000")
        )

        goals_table.setItem(
            1, 3,
            QTableWidgetItem("8")
        )

        goals_table.setItem(
            2, 0,
            QTableWidgetItem("Наушники")
        )

        goals_table.setItem(
            2, 1,
            QTableWidgetItem("Техника")
        )

        goals_table.setItem(
            2, 2,
            QTableWidgetItem("10000")
        )

        goals_table.setItem(
            2, 3,
            QTableWidgetItem("5")
        )

        goals_table.setStyleSheet("""
        QTableWidget {
            background-color: #111827;
            color: white;
            border-radius: 12px;
            gridline-color: #1E293B;
        }

        QHeaderView::section {
            background-color: #1E293B;
            color: white;
            padding: 8px;
            border: none;
        }
        """)

        content_layout.addWidget(goals_table)
        content_layout.addSpacing(15)

        add_goal_button = QPushButton("+ Добавить цель")
        add_goal_button.setFixedSize(180, 45)

        add_goal_button.setStyleSheet("""
        QPushButton {
            background-color: #7C3AED;
            color: white;
            border: none;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #8B5CF6;
        }

        QPushButton:pressed {
            background-color: #6D28D9;
        }
        """)

        content_layout.addWidget(add_goal_button)
        content_layout.addSpacing(20)

        optimize_button = QPushButton(
            "⚡ Оптимизировать план"
        )
        optimize_button.setMinimumHeight(80)
        optimize_button.setStyleSheet("""
        QPushButton {
            background-color: #7C3AED;
            color: white;
            border: none;
            border-radius: 14px;
            font-size: 20px;
            font-weight: bold;
            padding: 20px;
        }

        QPushButton:hover {
            background-color: #8B5CF6;
        }

        QPushButton:pressed {
            background-color: #6D28D9;
        }
        """)
        content_layout.addWidget(optimize_button)
        # ===== ДОБАВЛЯЕМ В ОКНО =====

        main_layout.addWidget(sidebar)
        main_layout.addWidget(content)