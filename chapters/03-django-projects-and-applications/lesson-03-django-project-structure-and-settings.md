# Lesson 03 — Django Project Structure and Settings

## 1. Introduction

After creating a Django project and its applications, we need to understand how the project is organized.

Django follows a structured architecture in which different files have specific responsibilities.

Understanding the project structure helps developers configure applications, manage URLs, connect databases, and maintain Django projects efficiently.

## 2. Understanding Django Project Structure

A typical Django project looks like this:

```text
university_system/
│
├── manage.py
│
├── university_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
└── teachers/
```

The project contains:

- A management script.
- An inner configuration package.
- One or more Django applications.

## 3. Understanding manage.py

`manage.py` is the command-line utility used to interact with a Django project.

It provides access to different Django management commands.

Examples:

```powershell
python manage.py runserver
python manage.py check
python manage.py startapp students
python manage.py migrate
python manage.py createsuperuser
```

It also sets the default settings module for the project.

## 4. Understanding settings.py

`settings.py` is one of the most important files in a Django project.

It contains the main configuration of the application.

File location:

```text
university_system/settings.py
```

It controls:

- Installed applications.
- Middleware.
- Database configuration.
- Templates.
- Static files.
- Internationalization.
- Security settings.
- Allowed hosts.

## 5. Understanding INSTALLED_APPS

`INSTALLED_APPS` is a setting that tells Django which applications are included in the project.

Example:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'students',
    'teachers',
]
```

### Why Is INSTALLED_APPS Important?

Django uses this configuration to discover and integrate registered applications.

It is important for features such as:

- Model discovery.
- Application configuration.
- Migration management.
- Admin integration.
- Application-provided templates and static files.

An application created using `startapp` should be registered here when it is intended to be part of the project.

## 6. Understanding ROOT_URLCONF

The `ROOT_URLCONF` setting identifies the main URL configuration module.

Example:

```python
ROOT_URLCONF = 'university_system.urls'
```

This tells Django where to find the project's main URL patterns.

The project-level `urls.py` can then include URL configurations from individual applications.

## 7. Understanding DATABASES

The `DATABASES` setting defines the database connection used by the Django project.

A default SQLite configuration looks like this:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Django supports several database backends, including:

- SQLite
- PostgreSQL
- MySQL
- Oracle

The database configuration determines where Django stores and retrieves application data.

## 8. Understanding TEMPLATES

The `TEMPLATES` setting controls Django's template engine.

A typical configuration includes:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Important options:

| Setting | Purpose |
|---|---|
| `BACKEND` | Defines the template engine |
| `DIRS` | Specifies additional template directories |
| `APP_DIRS` | Allows Django to search application template directories |
| `OPTIONS` | Contains additional template configuration |

## 9. Understanding MIDDLEWARE

Middleware is a collection of components that process requests and responses during Django's request-response lifecycle.

Example:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

Each middleware component performs a particular task.

Examples include:

- Security checks.
- Session handling.
- CSRF protection.
- Authentication processing.
- Message handling.

Middleware will be studied in greater detail in a later chapter.

## 10. Understanding ALLOWED_HOSTS

`ALLOWED_HOSTS` defines the hostnames or IP addresses that Django accepts in incoming HTTP requests.

Example:

```python
ALLOWED_HOSTS = []
```

For local development, Django's development configuration commonly permits localhost and loopback addresses when this setting is empty and `DEBUG=True`.

For production, explicitly configure the domains or hostnames that should be allowed.

Example:

```python
ALLOWED_HOSTS = [
    'example.com',
    'www.example.com',
]
```

Do not use `'*'` as a production shortcut without understanding the security implications.

## 11. Understanding STATIC_URL

Static files include CSS, JavaScript, and image assets used by the application.

Example:

```python
STATIC_URL = 'static/'
```

This setting defines the URL prefix used when referencing static assets.

Django's static-file configuration will be covered in the templates and static files chapter.

## 12. Understanding WSGI and ASGI

Django provides two application entry-point interfaces.

### WSGI

WSGI stands for Web Server Gateway Interface.

It is a standard interface between synchronous Python web applications and compatible web servers.

File:

```text
university_system/wsgi.py
```

### ASGI

ASGI stands for Asynchronous Server Gateway Interface.

It supports asynchronous application handling and is useful for applications requiring asynchronous capabilities.

File:

```text
university_system/asgi.py
```

Both files expose an application callable that compatible servers can use.

## 13. Understanding apps.py

Every Django application normally contains an `apps.py` file.

Example:

```python
from django.apps import AppConfig


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'students'
```

This file defines the application's configuration class.

It can be referenced in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'students.apps.StudentsConfig',
]
```

## 14. Understanding Other Application Files

| File or Directory | Responsibility |
|---|---|
| `models.py` | Defines database models |
| `views.py` | Handles application requests |
| `admin.py` | Configures Django admin |
| `apps.py` | Defines application configuration |
| `tests.py` | Contains automated tests |
| `migrations/` | Stores database migration history |
| `__init__.py` | Marks a directory as a Python package |

## 15. Practical Inspection of Your Project

Open your existing Django project and inspect the following files:

```text
manage.py
myproject/settings.py
myproject/urls.py
students/apps.py
students/models.py
students/views.py
```

Understand what each file does and how it contributes to the application.

You can inspect the Django configuration using:

```powershell
python manage.py check
```

## 16. Knowledge Check

1. What is the purpose of `manage.py`?
2. Which file contains the main Django project configuration?
3. What is `INSTALLED_APPS`?
4. What does `ROOT_URLCONF` specify?
5. Which setting controls the database connection?
6. What is the purpose of `MIDDLEWARE`?
7. What does `ALLOWED_HOSTS` control?
8. What is the purpose of `STATIC_URL`?
9. What is the difference between WSGI and ASGI?
10. What is the responsibility of `apps.py`?

## 17. Practical Task

Inspect your existing Django project.

Complete the following tasks:

1. Open `settings.py`.
2. Identify all registered applications in `INSTALLED_APPS`.
3. Find the `ROOT_URLCONF` setting.
4. Identify the configured database engine.
5. Inspect the `MIDDLEWARE` list.
6. Find the `TEMPLATES` configuration.
7. Open your application's `apps.py`.
8. Run `python manage.py check`.

Write down the purpose of each configuration you inspected.

## Key Takeaways

- Django projects follow a structured directory architecture.
- `manage.py` executes project management commands.
- `settings.py` controls the main project configuration.
- `INSTALLED_APPS` registers applications.
- `ROOT_URLCONF` identifies the main URL configuration.
- `DATABASES` defines database connections.
- `MIDDLEWARE` controls request-response processing.
- WSGI and ASGI provide application interfaces for compatible servers.

---

**Lesson Status:** Completed

**Chapter Status:** Completed

**Next Chapter:** Chapter 04 — URLs and Views