# Lesson 06 — URL Names, Namespaces and reverse()

## 1. What Are Named URL Patterns?

Django allows us to assign a name to each URL pattern.

Named URLs make applications easier to maintain because we can refer to a route by its name instead of writing its complete URL repeatedly.

Example:

```python
# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='student_home'),
    path('about/', views.about, name='student_about'),
]
```

Here:

- `student_home` is the name of the home URL.
- `student_about` is the name of the about URL.

## 2. Why Use Named URLs?

Consider this example:

```html
<a href="/students/about/">About</a>
```

This is a hardcoded URL.

If the route changes, we must update every place where that URL is written.

Instead, we can use a named URL:

```html
<a href="{% url 'student_about' %}">About</a>
```

Django generates the correct URL using its name.

This reduces hardcoding and makes applications easier to maintain.

## 3. Using the URL Template Tag

Django provides the `{% url %}` template tag to generate URLs from named URL patterns.

Syntax:

```django
{% url 'url_name' %}
```

Example:

```html
<a href="{% url 'student_home' %}">Home</a>
<a href="{% url 'student_about' %}">About</a>
```

Django resolves each URL name and generates the corresponding URL.

## 4. Named URLs with Dynamic Parameters

Named URLs can also contain dynamic parameters.

URL configuration:

```python
# students/urls.py

urlpatterns = [
    path(
        'students/<int:student_id>/',
        views.student_detail,
        name='student_detail'
    ),
]
```

Template:

```django
<a href="{% url 'student_detail' student_id=10 %}">
    View Student
</a>
```

Generated URL:

```text
/students/10/
```

The parameter supplied to the URL template tag must match the parameter expected by the URL pattern.

## 5. What Are URL Namespaces?

Namespaces help distinguish URL names when a project contains multiple applications.

For example, two applications may both have a URL named `home`.

Without namespaces, these names can become ambiguous.

Django supports application namespaces to organize URL names.

In the app-level URL configuration:

```python
# students/urls.py

from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
```

In the project-level URL configuration:

```python
# myproject/urls.py

from django.urls import path, include

urlpatterns = [
    path('students/', include('students.urls')),
]
```

Now we can reference the named URL using its namespace:

```django
<a href="{% url 'students:home' %}">Home</a>
<a href="{% url 'students:about' %}">About</a>
```

The format is:

```text
namespace:url_name
```

## 6. What Is reverse()?

Django provides the `reverse()` function to generate a URL from its name in Python code.

It is imported from `django.urls`.

Example:

```python
from django.urls import reverse
from django.http import HttpResponse

def home(request):
    url = reverse('students:about')
    return HttpResponse(f"About URL: {url}")
```

The `reverse()` function resolves the named URL and returns its URL path.

Example result:

```text
/students/about/
```

## 7. Using reverse() with Dynamic Parameters

The `reverse()` function also supports dynamic URL parameters.

Example:

```python
from django.urls import reverse

url = reverse(
    'students:student_detail',
    kwargs={'student_id': 10}
)
```

Generated URL:

```text
/students/10/
```

The keyword arguments must match the parameter names defined in the URL pattern.

## 8. redirect() with Named URLs

Django's `redirect()` shortcut can also use a named URL.

Example:

```python
from django.shortcuts import redirect

def home(request):
    return redirect('students:about')
```

This redirects the user to the URL associated with `students:about`.

## 9. Difference Between {% url %} and reverse()

| `{% url %}` | `reverse()` |
|---|---|
| Used inside Django templates | Used inside Python code |
| Generates a URL from a named route | Generates a URL from a named route |
| Uses template syntax | Uses a Python function |
| Useful for links in HTML | Useful in views and other Python logic |

## 10. Important Points

- Named URLs are defined using the `name` argument in `path()`.
- `{% url %}` generates URLs inside templates.
- `app_name` defines an application's namespace.
- Namespaces help organize URL names across applications.
- Use `namespace:url_name` to reference namespaced routes.
- `reverse()` generates URLs inside Python code.
- `redirect()` can redirect users using named URL patterns.
- Named URLs help avoid hardcoded URL paths.

## 11. Knowledge Check

**Q1. Which argument assigns a name to a URL pattern?**

A. `route`

B. `view`

C. `name`

D. `kwargs`

**Answer:** C. `name`

**Q2. Which template tag generates a URL from its name?**

A. `{% path %}`

B. `{% url %}`

C. `{% include %}`

D. `{% route %}`

**Answer:** B. `{% url %}`

**Q3. Which function generates a URL from its name in Python code?**

A. `render()`

B. `include()`

C. `reverse()`

D. `path()`

**Answer:** C. `reverse()`

**Q4. What is the purpose of a namespace?**

A. To create database tables.

B. To organize and distinguish URL names.

C. To install Django applications.

D. To create templates.

**Answer:** B. To organize and distinguish URL names.

## 12. Practical Task

Create a small student application with the following routes:

1. Home
2. About
3. Student Detail

Requirements:

- Assign a name to each URL pattern.
- Define `app_name = 'students'`.
- Generate links using the `{% url %}` template tag.
- Generate a dynamic student detail URL.
- Use `reverse()` inside a Python view.
- Test the generated URLs in your browser.

## Lesson Summary

Named URL patterns allow Django applications to reference routes without hardcoding URL paths. The `{% url %}` template tag generates URLs inside templates, while `reverse()` performs the same task inside Python code. Namespaces organize URL names across applications.

**Lesson Status:** Completed