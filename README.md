# VAWebTests — UI Autotests (Selenium + Python)

Автоматизированные UI-тесты для web-приложения на Python + Selenium.  
Реализован паттерн **Page Object Model (POM)**.

---

## Стек

| Инструмент | Назначение |
|---|---|
| Python 3.11+ | Язык разработки |
| Selenium | UI-автоматизация браузера |
| pytest | Фреймворк для тестов |
| webdriver-manager | Авто-загрузка драйвера браузера |
| Allure | Отчётность |

---

## Структура проекта

```
VAWebTests/
├── core/               # Настройка драйвера, базовые классы
├── pages/              # Page Objects (страницы приложения)
├── tests/              # Тест-кейсы
├── conftest.py         # Фикстуры pytest (инициализация драйвера)
├── pytest.ini          # Конфигурация pytest
├── requirements.txt    # Зависимости
└── .gitignore
```

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/3007ver/VAWebTests.git
cd VAWebTests
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
```

### 3. Запустить тесты

```bash
# Все тесты
pytest

# С генерацией Allure-отчёта
pytest --alluredir=allure-results

# Конкретный тест
pytest tests/test_login.py -v
```

### 4. Открыть Allure-отчёт

```bash
allure serve allure-results
```

---

## CI

Тесты автоматически запускаются при каждом пуше и pull request через **GitHub Actions**.  
Результаты доступны во вкладке [Actions](../../actions).

## Примечание по CI
Тестируемый сайт ограничивает доступ с зарубежных IP-адресов,
поэтому тесты в GitHub Actions падают по таймауту.
Локально тесты проходят успешно.
