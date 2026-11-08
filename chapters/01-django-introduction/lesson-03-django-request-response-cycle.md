# Lesson 03 — Django Request-Response Cycle

## 1. What is the Request-Response Cycle?

The Request-Response Cycle describes how Django receives an HTTP request from a client, processes it, and sends an HTTP response back.

A client is usually a web browser.

**Example:**

When a user visits:

`http://127.0.0.1:8000/students/`

The browser sends an HTTP request to the Django development server. Django processes the request and returns an HTTP response containing the requested page.

## 2. Main Components Involved

| Component        | Responsibility                              |
| ---------------- | ------------------------------------------- |
| Browser / Client | Sends HTTP requests                         |
| Web Server       | Receives requests and passes them to Django |
| Middleware       | Processes requests and responses            |
| URL Dispatcher   | Matches URLs with views                     |
| View             | Executes application logic                  |
| Model / ORM      | Interacts with the database when needed     |
| Template         | Generates HTML when needed                  |
| HTTP Response    | Returns the result to the client            |

## 3. Step-by-Step Request Processing

### Step 1: Client Sends a Request

A user opens a URL in the browser.

Example:

`http://127.0.0.1:8000/students/`

The browser sends an HTTP GET request.

### Step 2: Django Receives the Request

The Django development server receives the request and passes it into Django's request-handling system.

### Step 3: Middleware Processes the Request

Django runs the request through the configured middleware.

Middleware can perform tasks such as:

- Session handling.
- Authentication.
- Security checks.
- CSRF protection.

### Step 4: URL Dispatcher Matches the URL

Django checks the URL patterns in the project's URL configuration and, when included, the application's URL configuration.

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
]
```

Django matches the `students/` URL with the `student_list` view.

### Step 5: View Executes Application Logic

The matched view receives the request and performs the required operations.

Example:

```python
from django.shortcuts import render

def student_list(request):
    students = [
        {'name': 'Ali', 'age': 22},
        {'name': 'Asad', 'age': 23},
    ]

    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )
```

### Step 6: Template Generates HTML

Django renders the template using the context data supplied by the view.

Example:

```html
<h1>Student List</h1>

{% for student in students %}
    <p>{{ student.name }} - {{ student.age }}</p>
{% endfor %}
```

### Step 7: Django Creates an HTTP Response

The `render()` function returns an `HttpResponse` containing the generated HTML.

Django then processes the response through the response side of middleware.

### Step 8: Browser Displays the Result

The server sends the HTTP response to the browser, which displays the HTML page.

## 4. Request-Response Flow Diagram

```text
             BROWSER / CLIENT
                    |
                    | HTTP Request
                    v
              DJANGO SERVER
                    |
                    v
                MIDDLEWARE
                    |
                    v
              URL DISPATCHER
                    |
                    v
                   VIEW
                    |
                    v
              MODEL / ORM
             (If Required)
                    |
                    v
                  VIEW
                    |
                    v
                TEMPLATE
             (If Required)
                    |
                    v
              HTTP RESPONSE
                    |
                    v
                MIDDLEWARE
                    |
                    v
             BROWSER / CLIENT
```

**Note:** Model and Template are not required for every request. A view can return an HTTP response directly without querying a database or rendering a template.

## 5. Important Django Functions

### `render()`

Combines a template with context data and returns an HTTP response.

```python
return render(request, 'home.html', {'name': 'Ali'})
```

### `HttpResponse()`

Returns a basic HTTP response directly.

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to Django')
```

### `redirect()`

Redirects the client to another URL or named route.

```python
from django.shortcuts import redirect

def home(request):
    return redirect('student_list')
```

## 6. Difference Between Request and Response

| Request                                            | Response                                |
| -------------------------------------------------- | --------------------------------------- |
| Sent by the client                                 | Sent by the server                      |
| Travels from browser to Django                     | Travels from Django to browser          |
| Contains information about the requested operation | Contains the result of processing       |
| Example: GET `/students/`                          | Example: HTML page with student records |

## 7. Key Takeaways

- The browser sends an HTTP request to Django.
- Middleware processes the request and response.
- URL Dispatcher matches the requested URL with a view.
- The view executes application logic.
- Models and templates are used when required.
- Django returns an HTTP response to the browser.
- `render()`, `HttpResponse()`, and `redirect()` are commonly used response functions.

## 8. Practice Questions

1. What is the Request-Response Cycle?
2. What happens when a browser sends a GET request?
3. What is the role of middleware?
4. What does the URL Dispatcher do?
5. What is the responsibility of a view?
6. What does `render()` return?
7. What is the difference between `HttpResponse()` and `redirect()`?
8. Does every Django request require a database query?
9. Does every Django request require a template?

## 9. Practical Task

**Task: Build and test a simple Django request-response flow.**

Requirements:

1. Create a URL named `cycle-demo/`.
2. Connect it to a view called `cycle_demo`.
3. Make the view return an `HttpResponse`.
4. Open the URL in your browser.
5. Change the view to use `render()` with an HTML template.
6. Compare both responses.

## 10. Lesson Status

- [x] Request-Response Cycle studied.
- [x] Middleware role understood.
- [x] URL Dispatcher understood.
- [x] View processing understood.
- [x] HTTP responses understood.
- [x] Practice questions completed.
- [x] Practical task completed.
