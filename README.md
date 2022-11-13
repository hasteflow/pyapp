# Project

## Things taken into consideration

* this read me file
* package management and virtual envs
* project structure and organization
* user normal workflow and oauth
    * auth and validation
    * migrations
* django templating blocks
* tests and integrations tests
* gitignore file
* admin panel and filtering

## Would be nice to add

* django command for user stats / reports from CLI
* test pipelines
* add docker integration and project setup
* add makefile basic commands
* add celery / dramatiq delayed task
* user change password lol
* user email auth workflow
* more unit and integration tests for
    * models
    * forms
    * views
    * selenium pages

## Project structure

    ├── poetry.lock
    ├── poetry.toml
    ├── pyapp
    │   ├── db.sqlite3
    │   ├── functional_tests
    │   │   └── test_user_login.py
    │   ├── geckodriver.log
    │   ├── iam_app
    │   │   ├── asgi.py
    │   │   ├── __init__.py
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── manage.py
    │   └── users
    │       ├── admin.py
    │       ├── apps.py
    │       ├── decorators.py
    │       ├── forms
    │       │   ├── __init__.py
    │       │   ├── user_login_form.py
    │       │   └── user_registration_form.py
    │       ├── __init__.py
    │       ├── migrations
    │       │   ├── __init__.py
    │       ├── models.py
    │       ├── templates
    │       │   └── users
    │       │       ├── homepage.html
    │       │       ├── login.html
    │       │       ├── logout.html
    │       │       ├── main
    │       │       │   └── content_page.html
    │       │       ├── register.html
    │       │       └── secret_area.html
    │       ├── tests
    │       │   ├── __init__.py
    │       │   ├── test_user_forms.py
    │       │   └── test_user_views.py
    │       ├── urls.py
    │       └── views.py
    ├── pyproject.toml
    ├── README.md
    └── tests
        └── __init__.py
