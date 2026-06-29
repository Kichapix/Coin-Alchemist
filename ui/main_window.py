from services.budget_service import BudgetService
from ui.add_goal_dialog import AddGoalDialog
from ui.result_dialog import ResultDialog
from algorithms.knapsack_solver import KnapsackSolver
from algorithms.greedy_solver import GreedySolver
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import *

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.budget_service = BudgetService()
        self.selected_goal = None
        self.filepath = Path("data/goals.json")

        try:
            self.budget_service.load_goals(
                self.filepath
            )
        except FileNotFoundError:
            pass

        self.setWindowTitle("Coin Alchemist")

        self.resize(1100, 700)
        self.showMaximized()

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

        sidebar_layout.addWidget(title)
        sidebar_layout.addWidget(subtitle)

        self.opt_button = QPushButton("Оптимизация")
        self.compare_button = QPushButton("Сравнение")

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

        self.opt_button.setStyleSheet(menu_style)
        self.compare_button.setStyleSheet(menu_style)

        sidebar_layout.addWidget(self.opt_button)
        sidebar_layout.addWidget(self.compare_button)

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

        self.budget_input = QLineEdit()

        self.budget_input.setPlaceholderText("50000")

        self.budget_input.setValidator(
            QIntValidator(0, 100000000)
        )

        self.budget_input.setStyleSheet("""
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
        budget_layout.addWidget(self.budget_input)

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

        self.add_goal_button = QPushButton("Добавить цель")
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

        self.delete_goal_button = QPushButton("Удалить цель")
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

        self.compare_button.clicked.connect(
            self.compare_algorithms
        )

        self.opt_button.clicked.connect(
            self.optimize_plan
        )
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

            card.setMinimumWidth(300)

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

    def select_goal(self, goal):
        self.selected_goal = goal
        self.refresh_table()

    def delete_selected_goal(self):

        if not self.selected_goal:
            return

        reply = QMessageBox.question(
            self,
            "Удаление цели",
            f'Удалить цель "{self.selected_goal.name}"?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        self.budget_service.remove_goal(
            self.selected_goal
        )

        self.selected_goal = None

        self.budget_service.save_goals(
            self.filepath
        )

        self.refresh_table()

    def optimize_plan(self):


        budget_text = self.budget_input.text()

        if not budget_text:
            return

        budget = int(budget_text)

        if budget <= 0:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Бюджет должен быть больше 0."
            )
            return

        if budget > 100000:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Бюджет должен быть не больше 100000 ₽."
            )
            return

        goals = self.budget_service.get_goals()

        if not goals:
            QMessageBox.information(
                self,
                "Нет целей",
                "Добавьте хотя бы одну цель для оптимизации."
            )
            return

        solver = KnapsackSolver()

        result = solver.solve(
            goals,
            budget
        )


        if not result["goals"]:
            QMessageBox.information(
                self,
                "План не найден",
                "Для указанного бюджета невозможно выбрать ни одной цели."
            )
            return

        goals_text = ""

        for goal in result["goals"]:
            goals_text += f"✓ {goal.name}\n"

        message = (
            f"{goals_text}\n"
            f"━━━━━━━━━━━━━━\n\n"
            f"Общая стоимость: "
            f"{result['total_cost']} ₽\n\n"
            f"Суммарный приоритет: "
            f"{result['total_priority']}"
        )

        dialog = ResultDialog(
            "Оптимальный план",
            message
        )

        dialog.exec()

    def compare_algorithms(self):

        budget_text = self.budget_input.text()

        if not budget_text:
            return

        budget = int(budget_text)

        if budget <= 0:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Бюджет должен быть больше 0."
            )
            return

        if budget > 100000:
            QMessageBox.warning(
                self,
                "Ошибка",
                "Бюджет должен быть не больше 100000 ₽."
            )
            return

        goals = self.budget_service.get_goals()

        if not goals:
            QMessageBox.information(
                self,
                "Нет целей",
                "Добавьте хотя бы одну цель."
            )
            return

        greedy_solver = GreedySolver()
        knapsack_solver = KnapsackSolver()

        greedy_result = greedy_solver.solve(
            goals,
            budget
        )

        knapsack_result = knapsack_solver.solve(
            goals,
            budget
        )

        greedy_goals = ""

        for goal in greedy_result["goals"]:
            greedy_goals += f"✓ {goal.name}\n"

        knapsack_goals = ""

        for goal in knapsack_result["goals"]:
            knapsack_goals += f"✓ {goal.name}\n"

        if greedy_result["total_priority"] > knapsack_result["total_priority"]:
            winner = "Победитель: GREEDY"

        elif knapsack_result["total_priority"] > greedy_result["total_priority"]:
            winner = "Победитель: KNAPSACK"

        else:
            winner = "Ничья"

        message = (
            "GREEDY\n\n"
            f"{greedy_goals}\n"
            f"Стоимость: {greedy_result['total_cost']} ₽\n"
            f"Приоритет: {greedy_result['total_priority']}\n\n"
            "━━━━━━━━━━━━━━\n\n"
            "KNAPSACK\n\n"
            f"{knapsack_goals}\n"
            f"Стоимость: {knapsack_result['total_cost']} ₽\n"
            f"Приоритет: {knapsack_result['total_priority']}\n\n"
            f"{winner}"
        )

        dialog = ResultDialog(
            "Сравнение алгоритмов",
            message
        )

        dialog.exec()