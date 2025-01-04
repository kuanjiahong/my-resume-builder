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


### Run server locally:

First, set the environment variables

Windows:

```powershell
.\ps-set-env-dev.ps1
```

Linux / macOs:
```shell
./unix-set-env-dev.sh
```


```bash
cd myresumebuilder
python manage.py migrate
python manage.py runserver
```

### Run container:

First, [install Docker](https://www.docker.com/)

Second, create a `.env` file and populate the environment variables as shown in `env-example.txt`.

```shell
docker compose up
```

## Deployment

Reference: https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

Run manage.py check --deploy
```shell
python manage.py check --deploy
```

Generate `SECRET_KEY`
```shell
python -c "import secrets; print(secrets.token_urlsafe(60))"
```
Reference:
- https://stackoverflow.com/questions/34897740/what-is-the-simplest-and-safest-method-to-generate-an-api-key-and-secret-in-pyth
- https://docs.python.org/3/library/secrets.html

Environment-specific settings:

```python
DEBUG="False"
SESSION_COOKIE_SECURE="True"
CSRF_COOKIE_SECURE="True"
ALLOWED_HOSTS="your-domain.com, another-domain-if-any.com"
SECURE_SSL_REDIRECT="True"
SECURE_HSTS_SECONDS="31536000" # one year - but can first start with a small value for testing e.g. 3600 (one hour)
SECURE_HSTS_INCLUDE_SUBDOMAINS="True"
SECURE_HSTS_PRELOAD="True"
```
