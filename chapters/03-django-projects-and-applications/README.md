# Chapter 03 — Django Projects and Applications

## Overview

Django follows a project-based architecture that allows developers to organize web applications into reusable and maintainable components.

A Django project contains the main configuration and settings for a website, while Django applications handle specific features and functionalities.

This chapter explains Django projects, applications, their creation, and the overall project structure.

## Learning Objectives

By completing this chapter, you will understand how to:

- Understand the difference between a Django project and an application.
- Create a Django project using `django-admin`.
- Create Django applications using `manage.py`.
- Understand the Django project directory structure.
- Understand the purpose of `settings.py`.
- Configure installed applications using `INSTALLED_APPS`.
- Understand how multiple applications work together inside one project.

## Lessons

| Lesson | Topic | Status |
|---|---|---|
| 01 | Understanding Django Projects | Completed |
| 02 | Creating Django Projects and Applications | Completed |
| 03 | Django Project Structure and Settings | Completed |

## Key Concepts

### Django Project

A Django project represents the complete web application. It contains the main configuration, settings, URL configuration, and server entry points.

### Django Application

A Django application is a modular component responsible for a specific functionality within a project.

Examples include:

- Student Management
- User Authentication
- Blog Management
- Product Management
- Course Management

### Project and Application Relationship

A single Django project can contain multiple applications. Each application can handle a separate feature while sharing the project's configuration and resources.

## Practical Commands

```powershell
# Create a Django project
django-admin startproject myproject

# Enter the project directory
cd myproject

# Create a Django application
python manage.py startapp students

# Run Django system checks
python manage.py check

# Start the development server
python manage.py runserver
```

## Important Files

| File | Purpose |
|---|---|
| `manage.py` | Executes Django management commands |
| `settings.py` | Contains project configuration |
| `urls.py` | Defines project-level URL routing |
| `asgi.py` | ASGI application entry point |
| `wsgi.py` | WSGI application entry point |
| `apps.py` | Contains application configuration |
| `models.py` | Defines database models |
| `views.py` | Contains application views |
| `admin.py` | Configures Django admin registration |
| `tests.py` | Contains application tests |

## Key Takeaways

- A Django project represents the complete website or system.
- A Django application handles a specific feature.
- One project can contain multiple applications.
- `django-admin startproject` creates a project.
- `python manage.py startapp` creates an application.
- `settings.py` controls the main project configuration.
- Applications must be registered in `INSTALLED_APPS` when required.

## Chapter Progress

**Chapter Status:** Completed

## Next Chapter

**Chapter 04 — URLs and Views**