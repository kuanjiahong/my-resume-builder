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

Run server:

```bash
cd myresumebuilder
python manage.py migrate
python manage.py runserver
```
