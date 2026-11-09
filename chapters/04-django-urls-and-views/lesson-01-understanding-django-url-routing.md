# Lesson 01 — Understanding Django URL Routing

## 1. What Is URL Routing?

URL routing is the process of matching an incoming URL to a specific view in a Django application.

When a user visits a URL, Django checks its URL configuration to determine which view should handle the request.

For example:

```text
http://127.0.0.1:8000/students/
```

Django checks the configured URL patterns and calls the matching view.

## 2. What Is a URL Dispatcher?

Django's URL dispatcher is responsible for:

1. Receiving an incoming HTTP request.
2. Checking the configured URL patterns.
3. Finding the matching URL pattern.
4. Calling the associated view.
5. Returning the view's HTTP response to the client.

The URL dispatcher connects URLs with views. It does not contain the main business logic of the application.

## 3. What Is URLconf?

URLconf means URL Configuration.

It is a Python module that defines URL patterns for a Django project or application.

By default, Django uses the project-level URL configuration specified by `ROOT_URLCONF` in `settings.py`.

Example:

```python
# myproject/urls.py

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```

## 4. Understanding urlpatterns

`urlpatterns` is a Python list containing URL patterns.

Each pattern defines a URL and the view or handler that should process it.

Example:

```python
from django.urls import path
from students import views

urlpatterns = [
    path('students/', views.student_list),
]
```

In this example:

- `path()` defines a URL pattern.
- `'students/'` is the URL route.
- `views.student_list` is the view that handles the request.

## 5. Understanding path()

Django provides the `path()` function to define URL patterns.

Basic syntax:

```python
path(route, view, kwargs=None, name=None)
```

| Argument | Purpose |
|---|---|
| `route` | Defines the URL pattern. |
| `view` | Specifies the view that handles the request. |
| `kwargs` | Optional additional arguments passed to the view. |
| `name` | Optional name assigned to the URL pattern. |

Example:

```python
path('about/', views.about, name='about')
```

Here, `about/` is the route, `views.about` is the view, and `about` is the URL name.

## 6. Example of URL Routing

Consider this view:

```python
# students/views.py

from django.http import HttpResponse

def student_list(request):
    return HttpResponse("Welcome to the Student List")
```

Its URL configuration:

```python
# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list),
]
```

If the application URL configuration is included in the project URL configuration, visiting `/students/` will execute `student_list()`.

## 7. How Django Processes a Request

The basic flow is:

```text
Browser
   |
   | HTTP Request
   v
Django URL Dispatcher
   |
   | Matches URL Pattern
   v
View Function
   |
   | Creates HTTP Response
   v
Browser
```

## 8. Important Points

- URL routing connects incoming URLs to views.
- Django uses URLconf modules for URL configuration.
- `urlpatterns` is a list of URL patterns.
- `path()` is used to define URL patterns.
- A view handles the request and returns a response.
- Project-level and app-level URL configurations can be connected using `include()`.

## 9. Knowledge Check

**Q1. What is the main purpose of URL routing in Django?**

A. To create database tables.

B. To connect URLs with views.

C. To install Django packages.

D. To create HTML templates.

**Answer:** B. To connect URLs with views.

**Q2. What is URLconf?**

A. A database configuration file.

B. A Python module containing URL patterns.

C. A Django template.

D. A static files directory.

**Answer:** B. A Python module containing URL patterns.

**Q3. Which function is commonly used to define URL patterns?**

A. `render()`

B. `HttpResponse()`

C. `path()`

D. `models()`

**Answer:** C. `path()`

## 10. Practical Task

Create a simple Django view that returns:

```text
Welcome to Django URL Routing
```

Then connect that view to a URL route named `routing/` and test it using the Django development server.

## Lesson Summary

Django URL routing determines which view handles an incoming request. URLconf defines URL patterns, `urlpatterns` stores them, and `path()` connects routes to views.

**Lesson Status:** Completed