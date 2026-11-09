# Lesson 01 — Understanding Django Projects

## 1. Introduction

Django is a Python web framework that follows a project-based architecture.

Before developing a Django application, it is important to understand what a Django project is and how its applications work together.

A Django project provides the overall configuration and structure for a website or web-based system.

## 2. What Is a Django Project?

A Django project is the complete configuration and collection of applications that make up a website or web system.

It contains:

- Project settings
- Main URL configuration
- ASGI configuration
- WSGI configuration
- Management script
- One or more Django applications

For example, an online learning platform could be a Django project containing applications for students, courses, payments, and authentication.

## 3. What Is a Django Application?

A Django application is a modular component designed to perform a particular functionality within a Django project.

Examples:

| Application | Responsibility |
|---|---|
| `students` | Student management |
| `courses` | Course management |
| `accounts` | User authentication |
| `orders` | Order management |
| `blog` | Blog posts and articles |

Each application can contain its own models, views, URLs, templates, and other components.

## 4. Difference Between Project and Application

| Django Project | Django Application |
|---|---|
| Represents the complete website or system | Handles a specific feature |
| Contains project configuration | Contains feature-specific functionality |
| Can contain multiple applications | Belongs to a Django project when used |
| Created using `startproject` | Created using `startapp` |
| Contains `settings.py` and main `urls.py` | Commonly contains `models.py`, `views.py`, and `admin.py` |

### Simple Example

Imagine developing a Student Management System.

The complete system is the Django project.

Inside it, we can create applications such as:

- Students
- Teachers
- Courses
- Attendance

Each application manages a separate part of the system.

## 5. Understanding Django Architecture

A typical Django project can contain multiple applications:

```text
school_management/
│
├── manage.py
│
├── school_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── apps.py
│   └── tests.py
│
├── teachers/
│
└── courses/
```

**Note:** This is a simplified example. Each application can contain additional files and directories as the project grows.

## 6. Why Does Django Use Applications?

Django applications make development more organized and maintainable.

Main advantages:

1. **Modularity:** Each application handles a specific functionality.
2. **Reusability:** Applications can be reused in other Django projects.
3. **Maintainability:** Changes can be managed within individual applications.
4. **Scalability:** New features can be added without placing all functionality in one application.
5. **Separation of concerns:** Different features can be developed independently.

## 7. Can One Project Have Multiple Applications?

Yes.

A single Django project can contain multiple applications.

For example:

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

All applications share the main project configuration but manage their own responsibilities.

## 8. Practical Example

Suppose we want to build a University Management System.

We can divide it into separate applications:

| Application | Functionality |
|---|---|
| `students` | Register and manage students |
| `teachers` | Manage teacher information |
| `courses` | Manage university courses |
| `departments` | Manage academic departments |

This approach keeps the project organized instead of putting every feature into one large application.

## 9. Knowledge Check

1. What is a Django project?
2. What is a Django application?
3. What is the main difference between a project and an application?
4. Can one Django project contain multiple applications?
5. Give three examples of Django applications.
6. Why does Django use a modular application structure?
7. Which file contains the main project settings?

## 10. Practical Task

Plan a Django project for a University Management System.

Identify at least four applications that would be useful and describe the responsibility of each one.

Do not create the applications yet. We will implement project and application creation in the next lesson.

## Key Takeaways

- A Django project represents the complete web system.
- A Django application handles a specific feature.
- One project can contain multiple applications.
- Applications improve modularity, maintainability, and reusability.
- Good application design helps organize larger Django projects.

---

**Lesson Status:** Completed

**Next Lesson:** Creating Django Projects and Applications