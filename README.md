# Привет

Тут лежит финальный проект из курса [Автоматизация тестирования с помощью Selenium и Python — Stepik](https://stepik.org/575)

- Использовался Python версии 3.12.10
- Если команда `pip install -r requirements.txt` не сработала
```
pip install selenium pytest
```

- Тесты проверялись только на хроме.
- Добавлен флаг для запуска тестов без открытия окон браузера

```
pytest --headless=true
```

- Маркеры зарегистрированы в файле `pyproject.toml`

```
"step_4",
"step_6",
"step_8",
"step_10",
"step_13",
"login_quest",
"need_review"
```

- Маркеры `step_n` соответствуют шагам урока `4.3 Улучшаем дизайн тестов`

Команда для клонирования репозитория

```
git clone https://github.com/yuriy989/selenium_part4_final.git
```
