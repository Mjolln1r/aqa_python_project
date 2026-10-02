![CI](https://github.com/Mjolln1r/aqa_python_project/actions/workflows/tests.yml/badge.svg)
# AQA Python Project

Учебный проект для практики автоматизации тестирования на Python.

## Стек
- Python 3.11
- pytest
- requests (API тесты)
- Playwright (UI тесты)
- Pydantic / jsonschema (валидация схем)
- Allure (отчёты)
- GitHub Actions (CI/CD)

## Что тестируется
API тесты для jsonplaceholder.typicode.com:
- GET /users — получение пользователей
- POST /users — создание пользователя
- Валидация JSON схемы ответа
- Негативные сценарии (404)

UI тесты через Playwright:
- Проверка элементов страницы
- Page Object Model

## Запуск тестов

Установка зависимостей:
```bash
pip install -r requirements.txt
playwright install chromium
```

Запуск всех тестов:
```bash
pytest tests/ -v
```

Запуск с Allure отчётом:
```bash
pytest tests/ -v --alluredir=allure-results
allure serve allure-results
```
## CI/CD
GitHub Actions автоматически запускает тесты при push в main.
Allure результаты сохраняются как артефакт после каждого прогона.
