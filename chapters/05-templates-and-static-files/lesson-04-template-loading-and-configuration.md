# Lesson 04 — Template Loading and Configuration

## Learning Objectives
- Locate template configuration in Django settings.
- Understand DIRS and APP_DIRS.
- Explain how Django discovers templates.
- Organize project-level and app-level template directories.

## 1. The TEMPLATES Setting
Django's template engine is configured in settings.py through the TEMPLATES setting. A typical configuration resembles:

```python
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```
Inspect the actual project settings before changing them.

## 2. DIRS
DIRS is a list of additional filesystem directories where Django looks for templates. A project-level directory can be configured using BASE_DIR:

```python
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
```

Place BASE_DIR / "templates" in the DIRS list of the existing TEMPLATES configuration. Do not create a second TEMPLATES setting.

## 3. APP_DIRS
When APP_DIRS is True, Django's app-directory loader looks for templates in installed apps' templates/ directories.

```text
my_app/
└── templates/
    └── my_app/
        └── page.html
```
The app must be included in INSTALLED_APPS for its templates to be discovered.

## 4. Practical Tasks
1. Inspect the project's TEMPLATES configuration.
2. Identify DIRS and APP_DIRS values.
3. Locate one app-level template.
4. If needed, create a project-level templates/ directory and configure DIRS.
5. Render a template from each location and verify discovery.

## 5. Common Errors
- App missing from INSTALLED_APPS.
- Incorrect template path or filename.
- APP_DIRS disabled when relying on app template discovery.
- Incorrect project-level directory in DIRS.

## Key Takeaways
- DIRS adds project-specific template search locations.
- APP_DIRS=True enables discovery inside installed apps.
- Namespaced template paths reduce naming conflicts.

## Review Questions
1. What is the purpose of TEMPLATES in settings?
2. What is the difference between DIRS and APP_DIRS?
3. Why should app templates be namespaced?
