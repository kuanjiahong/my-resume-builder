# My Resume Builder

An application to build resume

## Built With

Language: Python v3.12.5

Framework: Django v5.1.4

Database: Postgres v17.2

## Getting Started

Create virtual environment `python -m venv .venv`

Install python packages `pip install -r requirements.txt`

Database setup:

- [Install Postgres](https://www.postgresql.org/download/)
- Create database with name `myresumebuilder` ([Postgres Documentation](https://www.postgresql.org/docs/current/sql-createdatabase.html))
- Setup Postgres connection ([Django Documentation](https://docs.djangoproject.com/en/5.1/ref/databases/#postgresql-notes)):
  - [The Password File - Postgres Documentation](https://www.postgresql.org/docs/current/libpq-pgpass.html)
  - [The Connection Service File - Postgres Documentation](https://www.postgresql.org/docs/current/libpq-pgservice.html)

Create a `.env` file and populate the environment variables as shown in `env-example`.

Run server locally:

Before running the server locally, set the environment variables in `env-example` in the terminal.

Windows: 
- [about Environment Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables?view=powershell-7.4)
- [Stack Overflow - Setting Windows PowerShell environment variables](https://stackoverflow.com/questions/714877/setting-windows-powershell-environment-variables)

Linux/macOs:
- [freecodecamp - How to Set an Environment Variable in Linux](https://www.freecodecamp.org/news/how-to-set-an-environment-variable-in-linux/)


```bash
cd myresumebuilder
python manage.py migrate
python manage.py runserver
```

Run container:

First, [install Docker](https://www.docker.com/)

Second, make sure you have a `.env` file in the root of the project

```shell
docker compose up
```
