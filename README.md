# Django-Movies-DB

A django project which creates an ORM database about movies, directors and actors. The
project also implements a text client which uses custom flag commands, so the database can be updated and queried
through just using terminal. It also creates an API with CRUD functionality to all 3 tables
and its text client can access data through it. Project is also broadened by adding certain tests, using pytest module.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pipenv, django, 
django-extensions and djangorestframework

```bash
pip install pipenv, django, django-extensions, djangorestframework
```

If you want to use VSCode terminal with this django project you have to select a correct
python interpreter. First get knowledge of a venv directory:

```bash
pipenv --venv
```

Copy the returned path and paste it as a custom python interpreter in VSCode (press
SHIFT+CTRL+P for a search bar)

## Usage

Create virtual environment in project directory and activate it

```bash
python -m venv ./venv-orm
.\venv-orm\Scripts\Activate
```

Then you can access the database. You can work with three main tables, there are various
options like adding, deleting, writing out and querying through the tables, in order to
learn which flags to use type:

```bash
python manage.py movies --help
python manage.py actors --help
python manage.py directors --help
```

For example to add an actor to the database you can write

```bash
python manage.py actors --add --name 'Christian Bale' --date_of_birth '1974-1-30' --latest_movie 'Thor: Love and Thunder'
```

If you want to access data through API instead use --mode "api" flag, when writing a statement:

```bash
python manage.py movies --mode "api" --write
```

In order to run implemented tests, you shall install pytest and initialize it in correct directory:

```bash
pip install pytest
cd tests
pytest
```

## Post Scriptum
The code was altered to match PEP 8 standards, using autopep8 module
```bash
pip install autopep8
autopep8 --in-place --recursive .\MoviesDB_KO\
```
Type adnotations are implemented in the code, they were checked using mypy module
```bash
pip install mypy
mypy .\MoviesDB_KO\
```
