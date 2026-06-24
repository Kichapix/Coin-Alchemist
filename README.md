# Coin Alchemist — учебная ознакомительная практика 2026

**Студент:** Конопельный Родион Сергеевич 
**Группа:** БИН-24-1  
**Вариант:** Б-29 - Планировщик личного бюджета  
**Язык:** Python 3.12

## Описание

Coin Alchemist - приложение для планирования личного бюджета. Пользователь может добавлять финансовые цели, указывать их стоимость и приоритет, задавать доступный бюджет и находить оптимальный набор целей с помощью алгоритмов оптимизации.

В проекте реализованы два алгоритма: жадный алгоритм (Greedy) и алгоритм динамического программирования для задачи о рюкзаке (Knapsack).

## Структура репозитория

```text
.
├── algorithms/
│   ├── greedy_solver.py      # жадный алгоритм
│   └── knapsack_solver.py    # алгоритм задачи о рюкзаке
├── data/
│   └── goals.json            # сохранённые цели пользователя
├── models/
│   └── goal.py               # модель финансовой цели
├── services/
│   ├── budget_service.py     # работа с целями
│   └── storage_service.py    # сохранение и загрузка данных
├── tests/
│   ├── test_budget_service.py
│   ├── test_goal.py
│   ├── test_greedy_solver.py
│   ├── test_integration.py
│   ├── test_knapsack_solver.py
│   └── test_storage_service.py
├── ui/
│   ├── add_goal_dialog.py
│   ├── category_selector.py
│   ├── main_window.py
│   ├── priority_selector.py
│   └── result_dialog.py
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── requirements.txt
├── main.py
└── README.md
```

## Установка и запуск

### Локально

```bash
# Клонировать репозиторий
git clone https://github.com/kichapix/coin-alchemist.git
cd coin-alchemist

# Создать виртуальное окружение
python -m venv .venv

# Активировать окружение
source .venv/bin/activate        # macOS / Linux
# или
.venv\Scripts\activate           # Windows

# Установить зависимости
pip install -r requirements.txt

# Запустить приложение
python main.py
```

### В Docker

```bash
# Собрать и запустить контейнер
docker compose up --build
```

После запуска приложение будет доступно по адресу:

```text
http://localhost:6080/vnc.html
```

Для остановки контейнера:

```bash
docker compose down
```

## Запуск тестов

```bash
python -m pytest tests/ -v
```

## Зависимости

- Python 3.12
- PySide6 6.11.1
- pytest 9.0.3
- Docker