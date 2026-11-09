# Lesson 02 — Creating Django Projects and Applications

## 1. Introduction

After understanding the difference between Django projects and applications, the next step is learning how to create them.

Django provides two important commands:

- `django-admin startproject` — creates a Django project.
- `python manage.py startapp` — creates a Django application.

These commands establish the basic structure required to develop Django applications.

## 2. Creating a Django Project

A Django project can be created using the `startproject` command.

### Command

```powershell
django-admin startproject myproject
```

### Explanation

| Part | Purpose |
|---|---|
| `django-admin` | Django's administrative command-line utility |
| `startproject` | Creates a new Django project |
| `myproject` | Name of the project |

### Generated Structure

```text
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

Django creates an outer project directory and an inner Python package containing the project configuration.

## 3. Understanding manage.py

`manage.py` is a command-line utility automatically created when a Django project is generated.

It allows developers to execute Django management commands for that project.

Examples:

```powershell
python manage.py runserver
python manage.py startapp students
python manage.py check
python manage.py migrate
python manage.py createsuperuser
```

**Important:** Run `manage.py` commands from the directory containing `manage.py`, unless you explicitly provide the correct project path.

## 4. Creating a Django Application

After creating a project, we can create an application inside it.

### Command

```powershell
python manage.py startapp students
```

### Explanation

| Part | Purpose |
|---|---|
| `python` | Executes the Python interpreter |
| `manage.py` | Project management script |
| `startapp` | Creates a Django application |
| `students` | Application name |

### Generated Application Structure

```text
students/
│
├── migrations/
│   └── __init__.py
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

Each generated file has a specific responsibility within the application.

## 5. Understanding Application Files

| File | Purpose |
|---|---|
| `__init__.py` | Marks the directory as a Python package |
| `admin.py` | Registers and customizes models in Django admin |
| `apps.py` | Contains application configuration |
| `models.py` | Defines database models |
| `tests.py` | Contains automated tests |
| `views.py` | Contains request-handling view functions or classes |
| `migrations/` | Stores database migration files |

## 6. Registering an Application

Creating an application does not automatically register it in the project settings.

To register it, open:

```text
myproject/settings.py
```

Find:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Add your application:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'students',
]
```

Django can now recognize the application as part of the project.

### Using AppConfig

You can also register an application using its configuration class:

```python
'students.apps.StudentsConfig',
```

This is useful when application-specific configuration is required.

## 7. Creating Multiple Applications

A project can contain multiple applications.

Example:

```powershell
python manage.py startapp students
python manage.py startapp teachers
python manage.py startapp courses
python manage.py startapp departments
```

Register each application in `INSTALLED_APPS`.

A possible project structure:

```text
university_system/
│
├── manage.py
│
├── university_system/
│   ├── settings.py
│   └── urls.py
│
├── students/
├── teachers/
├── courses/
└── departments/
```

## 8. Starting a Project in the Current Directory

Django also supports creating a project directly inside the current directory.

```powershell
django-admin startproject myproject .
```

The dot (`.`) tells Django to use the current directory as the destination.

Example:

```text
DjangoProject/
│
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── venv/
```

This approach avoids creating an additional outer project folder.

**Important:** Use an empty or appropriately prepared directory to avoid overwriting existing files.

## 9. Checking the Project

After creating the project and registering the application, run:

```powershell
python manage.py check
```

If no configuration issues are detected, Django reports:

```text
System check identified no issues (0 silenced).
```

## 10. Complete Practical Workflow

```powershell
# Create a project
django-admin startproject university_system

# Enter the project directory
cd university_system

# Create applications
python manage.py startapp students
python manage.py startapp teachers
python manage.py startapp courses

# Check project configuration
python manage.py check

# Start the development server
python manage.py runserver
```

After creating the applications, remember to register them in `INSTALLED_APPS`.

## 11. Common Mistakes

### Mistake 1 — Running startapp Outside the Project

The `startapp` command is normally executed using the project's `manage.py` file.

Make sure you are inside the directory containing `manage.py`.

### Mistake 2 — Forgetting INSTALLED_APPS

Creating an application does not automatically add it to `INSTALLED_APPS`.

Register it in `settings.py`.

### Mistake 3 — Incorrect Application Name

Use the actual application name when registering it.

For example:

```python
'students',
```

### Mistake 4 — Confusing Project and Application Directories

The outer project directory, inner configuration package, and individual applications serve different purposes.

Understand their roles before modifying files.

## 12. Knowledge Check

1. Which command creates a Django project?
2. Which command creates a Django application?
3. What is the purpose of `manage.py`?
4. What does `startproject` generate?
5. What does `startapp` generate?
6. Why do we register applications in `INSTALLED_APPS`?
7. What is the purpose of `apps.py`?
8. Can a project contain multiple applications?
9. What does the dot (`.`) mean in `django-admin startproject myproject .`?
10. Which command checks the Django project configuration?

## 13. Practical Task

Create a Django project named `university_system`.

Inside it, create three applications:

- `students`
- `teachers`
- `courses`

Then:

1. Inspect the generated project structure.
2. Open `settings.py`.
3. Register all three applications in `INSTALLED_APPS`.
4. Run `python manage.py check`.
5. Start the development server.

## Key Takeaways

- `django-admin startproject` creates a Django project.
- `python manage.py startapp` creates an application.
- `manage.py` executes project management commands.
- Every application has its own structure and responsibilities.
- Applications must be registered in `INSTALLED_APPS`.
- One Django project can contain multiple applications.

---

**Lesson Status:** Completed

**Next Lesson:** Django Project Structure and Settings