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

## Database
Install  [`PostgreSQL`] (https://www.postgresql.org/download/) on your OS 
Install  [`pgAdmin`] (https://www.pgadmin.org/download/)
Create a [`new sever and db`] (https://stackoverflow.com/questions/53267642/create-new-local-server-in-pgadmin)
Create an .env file, copy the content of conf.default.yml and change the values to your local values