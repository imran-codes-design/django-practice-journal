# Lesson 05 — Dynamic URLs and URL Parameters

## 1. What Are Dynamic URLs?

A dynamic URL is a URL that contains variable values.

Instead of creating a separate URL for every student, product, or article, we can use one URL pattern that accepts different values.

For example:

```text
/students/1/
/students/2/
/students/3/
```

These URLs can all use the same view function with different student IDs.

Dynamic URLs make Django applications more flexible and maintainable.

## 2. Static URLs vs Dynamic URLs

| Static URL | Dynamic URL |
|---|---|
| `/students/` | `/students/1/` |
| `/about/` | `/students/25/` |
| `/contact/` | `/products/10/` |
| Fixed route | Accepts variable values |

## 3. Using Django Path Converters

Django provides path converters to capture values from URLs.

Common path converters:

| Converter | Description | Example |
|---|---|---|
| `str` | Matches non-empty text without `/` | `ali` |
| `int` | Matches positive integers | `25` |
| `slug` | Matches letters, numbers, hyphens and underscores | `django-basics` |
| `uuid` | Matches a UUID value | UUID string |
| `path` | Matches text including `/` characters | `articles/django` |

Syntax:

```python
path('<converter:parameter_name>/', view_function)
```

## 4. Dynamic URL with an Integer Parameter

URL configuration:

```python
# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('students/<int:student_id>/', views.student_detail),
]
```

View:

```python
# students/views.py

from django.http import HttpResponse

def student_detail(request, student_id):
    return HttpResponse(f"Student ID: {student_id}")
```

Example URL:

```text
http://127.0.0.1:8000/students/25/
```

Expected response:

```text
Student ID: 25
```

Django captures `25` as an integer and passes it to the view as `student_id`.

## 5. Dynamic URL with a String Parameter

URL configuration:

```python
path('profile/<str:username>/', views.profile)
```

View:

```python
def profile(request, username):
    return HttpResponse(f"Welcome, {username}")
```

Example URL:

```text
/profile/imran/
```

Expected response:

```text
Welcome, imran
```

## 6. Using Multiple Dynamic Parameters

A URL can contain more than one dynamic parameter.

URL configuration:

```python
path(
    'courses/<int:course_id>/<str:course_name>/',
    views.course_detail
)
```

View:

```python
def course_detail(request, course_id, course_name):
    return HttpResponse(
        f"Course ID: {course_id}, Course Name: {course_name}"
    )
```

Example URL:

```text
/courses/10/python/
```

Expected response:

```text
Course ID: 10, Course Name: python
```

The parameter names in the URL pattern must match the arguments accepted by the view.

## 7. Using the Slug Converter

A slug is a URL-friendly text value commonly used for articles, blog posts, and product pages.

Example:

```python
path('articles/<slug:slug>/', views.article_detail)
```

View:

```python
def article_detail(request, slug):
    return HttpResponse(f"Article: {slug}")
```

Example URL:

```text
/articles/django-url-routing/
```

Expected response:

```text
Article: django-url-routing
```

## 8. What Happens When a URL Does Not Match?

Django checks the URL patterns in order.

If no pattern matches the requested URL, Django returns a 404 Not Found response.

For example, an `int` converter will not match a non-integer value:

```text
/students/abc/
```

For a route using `<int:student_id>`, this URL will not match.

## 9. Important Points

- Dynamic URLs accept variable values.
- Django uses path converters to capture URL values.
- `<int:student_id>` captures an integer.
- `<str:username>` captures non-empty text without `/`.
- Captured values are passed to view functions as keyword arguments.
- View parameter names must match the names in the URL pattern.
- Django returns a 404 response if no URL pattern matches.

## 10. Knowledge Check

**Q1. Which converter is used to capture an integer from a URL?**

A. `str`

B. `int`

C. `slug`

D. `path`

**Answer:** B. `int`

**Q2. What does `<str:username>` capture?**

A. An integer.

B. A UUID.

C. Non-empty text without `/`.

D. A database object.

**Answer:** C.

**Q3. Which converter is commonly used for URL-friendly article names?**

A. `slug`

B. `int`

C. `uuid`

D. `float`

**Answer:** A. `slug`

**Q4. What happens when no URL pattern matches a request?**

A. Django creates a new route.

B. Django returns a 404 response.

C. Django restarts the server.

D. Django creates a database.

**Answer:** B.

## 11. Practical Task

Create a student detail page using a dynamic URL.

Requirements:

1. Define a URL pattern using `<int:student_id>`.
2. Create a view named `student_detail`.
3. Accept `student_id` as a view parameter.
4. Return the student ID using `HttpResponse()`.
5. Test multiple URLs, such as `/students/1/`, `/students/2/`, and `/students/10/`.
6. Test an invalid value such as `/students/abc/`.

## Lesson Summary

Dynamic URLs allow Django applications to handle variable values through a single URL pattern. Path converters capture values and pass them to view functions as arguments.

**Lesson Status:** Completed