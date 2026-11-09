# Lesson 04 — Function-Based Views (FBVs)

## 1. What Are Function-Based Views?

A Function-Based View (FBV) is a Python function that receives an HTTP request and returns an HTTP response.

FBVs are used to handle application logic, process user requests, retrieve data, and display responses.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Django")
```

Here:

- `home` is the view function.
- `request` contains information about the incoming HTTP request.
- `HttpResponse()` returns a response to the browser.

## 2. Basic Structure of a Function-Based View

Syntax:

```python
def view_name(request):
    # Application logic
    return response
```

A Django view must return an appropriate HTTP response.

Common response functions include:

- `HttpResponse()`
- `render()`
- `redirect()`

## 3. Using HttpResponse()

`HttpResponse()` returns a direct HTTP response, commonly containing text or HTML.

Example:

```python
from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>About Us</h1>")
```

The browser displays the returned HTML.

## 4. Using render()

The `render()` function combines a template with context data and returns an HTTP response.

Syntax:

```python
render(request, template_name, context=None)
```

Example:

```python
from django.shortcuts import render

def home(request):
    context = {
        'name': 'Imran',
        'course': 'Django'
    }

    return render(request, 'home.html', context)
```

Example template:

```html
<h1>Welcome {{ name }}</h1>
<p>Course: {{ course }}</p>
```

The template displays the values passed through the context dictionary.

## 5. Understanding the Request Object

The `request` parameter is an HTTP request object.

It provides information about the current request.

Common request attributes include:

| Attribute | Purpose |
|---|---|
| `request.method` | HTTP method, such as GET or POST |
| `request.GET` | Query parameters sent through the URL |
| `request.POST` | Form data submitted through POST |
| `request.FILES` | Uploaded files |
| `request.path` | Requested URL path |
| `request.user` | Current authenticated user or anonymous user |

Example:

```python
from django.http import HttpResponse

def check_request(request):
    return HttpResponse(f"Request method: {request.method}")
```

## 6. Handling GET Requests

GET requests are commonly used to retrieve or display information.

Example:

```python
from django.http import HttpResponse

def student_list(request):
    if request.method == 'GET':
        return HttpResponse("Displaying students")

    return HttpResponse("Method not allowed", status=405)
```

## 7. Handling POST Requests

POST requests are commonly used to submit data to the server.

Example:

```python
from django.http import HttpResponse

def register_student(request):
    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        return HttpResponse(f"Registered: {student_name}")

    return HttpResponse("Please submit the registration form")
```

For HTML forms, POST requests should include Django's CSRF token when CSRF protection is enabled.

Example:

```html
<form method="POST">
    {% csrf_token %}
    <input type="text" name="student_name">
    <button type="submit">Register</button>
</form>
```

## 8. Connecting a Function-Based View to a URL

View:

```python
# students/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("Student Management System")
```

URL configuration:

```python
# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student_home'),
]
```

Project URL configuration:

```python
# myproject/urls.py

from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
]
```

Visiting `/students/` executes the `home()` view.

## 9. Function-Based Views vs Class-Based Views

| Function-Based Views | Class-Based Views |
|---|---|
| Defined using Python functions | Defined using Python classes |
| Straightforward for beginners | Provide reusable class-based structures |
| Uses conditional logic for different methods | Commonly uses methods such as `get()` and `post()` |
| Can be simple and explicit | Supports inheritance and mixins |

Both approaches are supported by Django.

## 10. Advantages of Function-Based Views

- Easy to understand.
- Simple to write and debug.
- Suitable for small and straightforward operations.
- Provide direct control over request handling.
- Useful for learning Django's request-response process.

## 11. Knowledge Check

**Q1. What is a Function-Based View?**

A. A database table.

B. A Python function that handles a request and returns a response.

C. An HTML template.

D. A URL configuration file.

**Answer:** B.

**Q2. Which parameter does a Django view normally receive first?**

A. `self`

B. `request`

C. `response`

D. `model`

**Answer:** B.

**Q3. Which function renders an HTML template with context data?**

A. `path()`

B. `include()`

C. `render()`

D. `redirect()`

**Answer:** C.

**Q4. Which request attribute contains submitted POST form data?**

A. `request.GET`

B. `request.POST`

C. `request.FILES`

D. `request.path`

**Answer:** B.

## 12. Practical Task

Create three Function-Based Views in a Django application:

1. `home()` — returns a welcome message using `HttpResponse()`.
2. `about()` — displays an HTML template using `render()`.
3. `check_method()` — displays the HTTP request method.

Connect all three views to separate URL patterns and test them in your browser.

## Lesson Summary

Function-Based Views are Python functions that handle HTTP requests and return HTTP responses. They can use `HttpResponse()` for direct responses, `render()` for templates, and the request object to access submitted data and request information.

**Lesson Status:** Completed