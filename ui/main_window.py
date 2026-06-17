from services.budget_service import BudgetService
from ui.add_goal_dialog import AddGoalDialog
from PySide6.QtCore import Qt
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
    QAbstractItemView,
    QHeaderView,
    QScrollArea,
    QGridLayout
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.budget_service = BudgetService()
        self.selected_goal = None
        self.filepath = "data/goals.json"
        self.budget_service.load_goals(
            self.filepath
        )
        self.setWindowTitle("Coin Alchemist")

        self.resize(1100, 700)
        self.setMinimumSize(1000, 650)

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

        budget_card.setFixedSize(500, 90)

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

        budget_layout.setSpacing(5)

        budget_layout.addWidget(budget_title)
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

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_area.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.scroll_area.setVerticalScrollBarPolicy(
            Qt.ScrollBarAsNeeded
        )

        self.scroll_area.setStyleSheet("""
        QScrollArea {
            border: none;
            background: transparent;
        }

        QScrollBar:vertical {
            background: #111827;
            width: 10px;
        }

        QScrollBar::handle:vertical {
            background: #7C3AED;
            border-radius: 5px;
        }
        """)

        self.goals_widget = QWidget()

        self.goals_container = QGridLayout()

        self.goals_container.setSpacing(15)

        self.goals_widget.setLayout(
            self.goals_container
        )

        self.scroll_area.setWidget(
            self.goals_widget
        )

        self.scroll_area.setMinimumHeight(350)

        content_layout.addWidget(
            self.scroll_area,
            1
        )

        self.goals_table = QTableWidget()

        self.goals_table.setAlternatingRowColors(True)

        self.goals_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.goals_table.verticalHeader().setVisible(False)

        self.goals_table.verticalHeader().setDefaultSectionSize(
            42
        )

        self.goals_table.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch
        )

        self.goals_table.setEditTriggers(

            QAbstractItemView.NoEditTriggers

        )

        self.goals_table.setColumnCount(4)

        self.goals_table.setHorizontalHeaderLabels([
            "Название",
            "Категория",
            "Стоимость",
            "Приоритет"
        ])

        self.goals_table.setStyleSheet("""
        QTableWidget {
            background-color: #111827;
            color: white;
            border-radius: 12px;
            gridline-color: #1E293B;
            alternate-background-color: #172033;
            selection-background-color: #7C3AED;
        }

        QHeaderView::section {
            background-color: #1E293B;
            color: white;
            padding: 8px;
            border: none;
        }
        """)

        self.goals_table.hide()
        content_layout.addSpacing(15)

        self.add_goal_button = QPushButton("+ Добавить цель")
        self.add_goal_button.setFixedSize(180, 45)

        self.add_goal_button.setStyleSheet("""
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

        self.delete_goal_button = QPushButton("🗑 Удалить цель")
        self.delete_goal_button.setFixedSize(180,45)

        self.delete_goal_button.setStyleSheet("""
        QPushButton {
            background-color: #1E293B;
            color: #F87171;
            border: 1px solid #EF4444;
            border-radius: 10px;
            font-size: 14px;
            font-weight: bold;
        }

        QPushButton:hover {
            background-color: #7F1D1D;
        }

        QPushButton:pressed {
            background-color: #991B1B;
        }
        """)

        self.delete_goal_button.clicked.connect(
            self.delete_selected_goal
        )

        buttons_layout = QHBoxLayout()

        buttons_layout.addWidget(
            self.add_goal_button
        )

        buttons_layout.addWidget(
            self.delete_goal_button
        )

        buttons_layout.addStretch()

        content_layout.addLayout(
            buttons_layout
        )
        content_layout.addSpacing(20)

        self.add_goal_button.clicked.connect(
            self.open_add_goal_dialog
        )

        self.delete_goal_button.clicked.connect(
            self.delete_selected_goal
        )

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

        self.refresh_table()

    def open_add_goal_dialog(self):
        dialog = AddGoalDialog()

        result = dialog.exec()

        if result and dialog.goal:
            self.budget_service.add_goal(
                dialog.goal
            )

            self.budget_service.save_goals(
                self.filepath
            )

            self.refresh_table()

    def add_goal_to_table(self, goal):
        row = self.goals_table.rowCount()

        self.goals_table.insertRow(row)

        self.goals_table.setItem(
            row,
            0,
            QTableWidgetItem(goal.name)
        )

        self.goals_table.setItem(
            row,
            1,
            QTableWidgetItem(goal.category)
        )

        self.goals_table.setItem(
            row,
            2,
            QTableWidgetItem(str(goal.cost))
        )

        self.goals_table.setItem(
            row,
            3,
            QTableWidgetItem(str(goal.priority))
        )

    def refresh_table(self):

        while self.goals_container.count():

            item = self.goals_container.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

        goals = self.budget_service.get_goals()

        index = 0

        for goal in goals:
            card = QFrame()

            if goal == self.selected_goal:
                card.setStyleSheet("""
                    QFrame {
                        background-color: #111827;
                        border: 2px solid #7C3AED;
                        border-radius: 12px;
                        padding: 12px;
                    }
                """)
            else:
                card.setStyleSheet("""
                    QFrame {
                        background-color: #111827;
                        border: 2px solid transparent;
                        border-radius: 12px;
                        padding: 12px;
                    }
                """)

            card.mousePressEvent = (
                lambda event, g=goal:
                self.select_goal(g)
            )

            card.setFixedHeight(150)

            card_layout = QVBoxLayout()
            card.setLayout(card_layout)

            title = QLabel(goal.name)

            title.setStyleSheet("""
                color: white;
                font-size: 18px;
                font-weight: bold;
                border: none;
            """)

            info = QLabel(
                f"{goal.category} • {goal.cost:,} ₽ • Приоритет {goal.priority}"
            )

            info.setStyleSheet("""
                color: #94A3B8;
                font-size: 14px;
                border: none;
            """)

            card_layout.addWidget(title)
            card_layout.addWidget(info)

            row = index // 2
            col = index % 2

            self.goals_container.addWidget(
                card,
                row,
                col
            )

            index += 1

    def delete_selected_goal(self):

        row = self.goals_table.currentRow()

        if row < 0:
            return

        goals = self.budget_service.get_goals()

        goal = goals[row]

        self.budget_service.remove_goal(
            goal
        )

        self.budget_service.save_goals(
            self.filepath
        )

        self.refresh_table()

    def select_goal(self, goal):
        self.selected_goal = goal
        self.refresh_table()

    def delete_selected_goal(self):

        if not self.selected_goal:
            return

        self.budget_service.remove_goal(
            self.selected_goal
        )

        self.refresh_table()

        self.selected_goal = None