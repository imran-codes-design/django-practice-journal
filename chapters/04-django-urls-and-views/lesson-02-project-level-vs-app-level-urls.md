# Lesson 02 — Project-Level vs App-Level URLs

## 1. Introduction

Django supports two levels of URL configuration:

1. Project-Level URL Configuration
2. App-Level URL Configuration

Separating URL configurations makes Django projects easier to organize, maintain, and scale.

## 2. Project-Level URLs

The project-level `urls.py` file is the main URL configuration of a Django project.

It is normally located inside the project configuration package, alongside `settings.py`.

Example structure:

```text
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

The project-level `urls.py` file is responsible for connecting application URL configurations and defining project-wide routes.

Example:

```python
# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
]
```

Here:

- `admin/` connects Django's admin site.
- `students/` connects the students application's URL configuration.
- `include()` imports and connects another URL configuration.

## 3. App-Level URLs

An app-level `urls.py` file contains URL patterns related to a particular Django application.

Django does not automatically create this file when you run `startapp`. You normally create it yourself.

Example structure:

```text
students/
    migrations/
    __init__.py
    admin.py
    apps.py
    models.py
    tests.py
    views.py
    urls.py
```

Example:

```python
# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
]
```

The app-level URL configuration defines routes related to student functionality.

## 4. What Is include()?

The `include()` function connects another URL configuration to the main project URL configuration.

It allows each application to manage its own URL patterns.

Example:

```python
# myproject/urls.py

from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
]
```

Django forwards URLs beginning with `students/` to `students.urls`.

The remaining part of the URL is matched against the patterns defined inside that application.

For example:

| Requested URL | App-level route |
|---|---|
| `/students/` | `''` |
| `/students/add/` | `'add/'` |
| `/students/edit/` | `'edit/'` |

The prefix `students/` is handled by the project-level configuration.

## 5. Difference Between Project-Level and App-Level URLs

| Project-Level URLs | App-Level URLs |
|---|---|
| Main URL configuration | Application-specific configuration |
| Located beside `settings.py` | Located inside an application |
| Connects applications | Defines routes for an application |
| Uses `include()` to connect app URLs | Usually connects routes to views |
| Manages project-wide routing | Manages application-specific routing |

## 6. What Is ROOT_URLCONF?

`ROOT_URLCONF` is a Django setting that identifies the project's main URL configuration module.

It is defined in `settings.py`.

Example:

```python
# myproject/settings.py

ROOT_URLCONF = 'myproject.urls'
```

This tells Django to use `myproject.urls` as the root URL configuration.

Django starts URL resolution from this module when processing incoming requests.

## 7. Complete Request Example

Suppose a user visits:

```text
http://127.0.0.1:8000/students/add/
```

Project-level URL configuration:

```python
# myproject/urls.py

from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
]
```

App-level URL configuration:

```python
# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student),
]
```

View:

```python
# students/views.py

from django.http import HttpResponse

def add_student(request):
    return HttpResponse("Add Student Page")
```

Request flow:

```text
Browser Request
      |
      v
ROOT_URLCONF
      |
      v
myproject/urls.py
      |
      | Matches students/
      v
include('students.urls')
      |
      v
students/urls.py
      |
      | Matches add/
      v
views.add_student()
      |
      v
HTTP Response
```

Expected browser output:

```text
Add Student Page
```

## 8. Important Points

- Django starts URL resolution from the root URL configuration.
- `ROOT_URLCONF` identifies the root URL configuration module.
- Project-level URLs connect application URL configurations.
- App-level URLs define routes for individual applications.
- `include()` connects another URL configuration.
- The project-level route prefix is removed before matching the remaining route in the included URL configuration.
- The `urls.py` file inside an app is generally created manually.

## 9. Knowledge Check

**Q1. Which file normally contains the main project URL configuration?**

A. `settings.py`

B. Project-level `urls.py`

C. `models.py`

D. `admin.py`

**Answer:** B. Project-level `urls.py`

**Q2. Which function connects an application URL configuration to the project URL configuration?**

A. `render()`

B. `path()`

C. `include()`

D. `redirect()`

**Answer:** C. `include()`

**Q3. What does `ROOT_URLCONF` specify?**

A. The database location.

B. The main URL configuration module.

C. The template directory.

D. The installed applications.

**Answer:** B. The main URL configuration module.

**Q4. Where is an app-level `urls.py` normally located?**

A. Beside `manage.py`.

B. Inside the Django application directory.

C. Inside the virtual environment.

D. Inside the database directory.

**Answer:** B. Inside the Django application directory.

## 10. Practical Task

Create a simple URL configuration using two levels:

1. Create `urls.py` inside a Django application.
2. Define a route for the application.
3. Create a view that returns an HTTP response.
4. Import `include` in the project-level `urls.py`.
5. Connect the application URL configuration.
6. Run the development server and test the route in your browser.

## Lesson Summary

Project-level URL configuration acts as the main entry point for URL routing. App-level URL configuration organizes routes belonging to individual applications. Django's `include()` function connects these configurations, while `ROOT_URLCONF` identifies the root URL module.

**Lesson Status:** Completed