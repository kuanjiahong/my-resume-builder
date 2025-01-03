$Env:DEBUG="True" # True if development else False
$Env:SECRET_KEY=""
$Env:SESSION_COOKIE_SECURE="False"
$Env:CSRF_COOKIE_SECURE="False"
$Env:ALLOWED_HOSTS="localhost, 127.0.0.1"
$Env:SECURE_SSL_REDIRECT="False"
$Env:SECURE_HSTS_SECONDS="0"
$Env:SECURE_HSTS_INCLUDE_SUBDOMAINS="False"
$Env:SECURE_HSTS_PRELOAD="False"

# Database
$Env:DB_HOST="localhost"
$Env:POSTGRES_DB="myresumebuilder"
$Env:POSTGRES_USER="postgres"
$Env:POSTGRES_PASSWORD=""