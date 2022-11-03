## audit-trail-fastAPI
Backend for Carl Zeiss project. Uses `python3.9` and [`poetry`](https://python-poetry.org/) as package manager.

### Getting started
1. `poetry shell` to create a virtual environment if it doesn't exist already and activate it
2. `poetry install` to install all dependencies from `pyproject.toml`
3. `uvicorn main:app --reload` to start the local server

### Pycharm
Pycharm will detect that you opened a `poetry` project and suggest creating a venv
from `pyproject.toml`. If you created the venv already, skip this and just add
the python interpreter from the venv (Pycharm should detect its location). Then, add
a run configuration for the server (choose `fastAPI` from the options).