# Система управления библиотекой

* Добавление книги:
```
python main.py add
```
* Удаление книги:
```
python main.py delete
```
* Поиск книги:
```
python main.py search
```
* Отображение всех книг:
```
python main.py list
```
* Изменение статуса книги:
```
python main.py change-status
```

Чтобы запустить тесты:
```
python -m pytest ./tests
```

Статический анализ:
```
uv run mypy ./
uv run ruff format .
uv run ruff check --fix .
```
