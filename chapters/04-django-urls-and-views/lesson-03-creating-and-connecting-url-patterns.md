# Lesson 03 — Creating and Connecting URL Patterns

## 1. Introduction

Django URL patterns define which view should handle a particular URL.

To connect a URL with a view, Django provides the `path()` function.

A URL configuration normally contains:

- Imports
- View references
- `urlpatterns`
- URL patterns

## 2. Importing Required Functions

The `path()` function is imported from `django.urls`.

Example:

```python
from django.urls import path
```

To connect application URLs inside the project URL configuration, import `include()` as well:

```python
from django.urls import path, include
```

## 3. Creating a View

First, create a view function inside an application's `views.py` file.

Example:

```python
# students/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Students Application")
```

A view receives an HTTP request and returns an HTTP response.

## 4. Creating App-Level URL Patterns

Create a `urls.py` file inside the application directory.

Example:

```python
# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student_home'),
]
```

Explanation:

- `path()` defines the route.
- `''` represents the application's root route.
- `views.home` identifies the view function.
- `name='student_home'` assigns a name to the URL pattern.

## 5. Connecting App-Level URLs to Project-Level URLs

Open the project's main `urls.py` file.

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

The `include()` function connects the students application's URL configuration to the project.

## 6. Understanding the Final URL

The project-level route:

```python
path('students/', include('students.urls'))
```

The app-level route:

```python
path('', views.home, name='student_home')
```

The final URL becomes:

```text
/students/
```

Django combines the project-level prefix with the matching app-level route.

## 7. Creating Multiple URL Patterns

An application can define multiple URL patterns.

Example:

```python
# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student_home'),
    path('about/', views.about, name='student_about'),
    path('contact/', views.contact, name='student_contact'),
]
```

Each URL pattern can connect to a different view.

## 8. Common URL Configuration Errors

| Error | Possible cause |
|---|---|
| `ModuleNotFoundError` | Incorrect application or module path |
| `ImportError` | Incorrect view import |
| `AttributeError` | Referenced view does not exist |
| `404 Page Not Found` | URL does not match any configured pattern |
| `TypeError` | Incorrect view signature or URL arguments |

## 9. Practical Commands

Start the Django development server:

```bash
python manage.py runserver
```

Check the project for configuration errors:

```bash
python manage.py check
```

## 10. Knowledge Check

**Q1. Which function defines a URL pattern?**

A. `render()`

B. `path()`

C. `include()`

D. `HttpResponse()`

**Answer:** B. `path()`

**Q2. What does `include()` do?**

A. Creates a database.

B. Connects another URL configuration.

C. Creates a view.

D. Loads a template.

**Answer:** B. Connects another URL configuration.

**Q3. What does an empty route `''` represent inside an included app URL configuration?**

A. The application's root route.

B. The admin route.

C. A database route.

D. An invalid URL.

**Answer:** A. The application's root route.

## 11. Practical Task

Create a Django application URL configuration containing three routes:

- Home
- About
- Contact

Connect each route to a separate view function.

Then connect the application URL configuration to the project-level `urls.py` using `include()` and test all three routes in the browser.

## Lesson Summary

URL patterns connect incoming requests to Django views. The `path()` function defines routes, while `include()` connects application-level URL configurations to the project-level configuration.

**Lesson Status:** Completed