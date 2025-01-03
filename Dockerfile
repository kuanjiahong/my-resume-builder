
FROM python:3.12.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt --no-cache-dir

COPY ./myresumebuilder/manage.py ./
COPY ./myresumebuilder/myresumebuildersite ./myresumebuildersite
COPY ./myresumebuilder/resumebuilder ./resumebuilder

RUN adduser -D myuser
USER myuser

# Collect static files (if any)
# RUN python myresumebuilder/manage.py collectstatic

EXPOSE 8000

# For production
CMD ["gunicorn", "--bind=0.0.0.0:8000", "myresumebuildersite.wsgi"]

# For development
# CMD ["python", "myresumebuilder/manage.py", "runserver", "0.0.0.0:8000"]
