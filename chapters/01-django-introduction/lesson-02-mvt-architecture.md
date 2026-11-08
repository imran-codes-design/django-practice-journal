# Lesson 02 — Django MVT Architecture

## 1. What is MVT Architecture?

MVT stands for:

- **M — Model**
- **V — View**
- **T — Template**

MVT is Django's architectural pattern for organizing application code. It separates database operations, application logic, and presentation.

This separation makes Django applications easier to develop, maintain, and extend.

## 2. Understanding the Three Components

### A. Model

A Model represents the structure of application data and defines how data is stored in the database.

Models are generally written in an application's `models.py` file.

Example:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
```

**Explanation:**

- `Student` defines a database model.
- `name` stores the student's name.
- `email` stores the student's email.
- `age` stores the student's age.
- Django ORM uses this model to interact with the database.

### B. View

A View receives an HTTP request, processes the required application logic, and returns an HTTP response.

Views are generally written in an application's `views.py` file.

Example:

```python
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()

    return render(
        request,
        'students/student_list.html',
        {'students': students}
    )
```

**Explanation:**

- `request` represents the incoming HTTP request.
- `Student.objects.all()` retrieves all student records.
- `render()` combines a template with the supplied context data.
- The view returns the resulting HTTP response.

### C. Template

A Template controls how information is displayed to the user.

Templates are generally written in HTML files.

Example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student List</title>
</head>
<body>

    <h1>Registered Students</h1>

    {% for student in students %}
        <p>{{ student.name }}</p>
        <p>{{ student.email }}</p>
        <hr>
    {% empty %}
        <p>No students found.</p>
    {% endfor %}

</body>
</html>
```

**Explanation:**

- `{{ student.name }}` displays a student's name.
- `{{ student.email }}` displays a student's email.
- `{% for %}` loops through the students.
- `{% empty %}` displays a message when there are no students.

## 3. How Do Model, View, and Template Work Together?

Consider a Student Management System.

When a user opens the student list page:

1. The browser sends a request to Django.
2. Django's URL dispatcher matches the requested URL with a view.
3. The View executes the application logic.
4. The View retrieves student records through the Model.
5. The View passes the data to the Template.
6. The Template generates HTML.
7. Django returns the HTML response to the browser.

## 4. MVT Architecture Flow

```text
             USER / BROWSER
                    |
                    | HTTP Request
                    v
              URL Dispatcher
                    |
                    v
                  VIEW
                    |
                    | Database Query
                    v
                  MODEL
                    |
                    | Database Records
                    v
                  VIEW
                    |
                    | Context Data
                    v
                TEMPLATE
                    |
                    | Generated HTML
                    v
              HTTP RESPONSE
                    |
                    v
             USER / BROWSER
```

**Important:** The Model communicates with the database. The View coordinates the application's logic, and the Template generates the presentation.

## 5. Where Are These Components Located?

In a typical Django application:

```text
students/
│
├── models.py
├── views.py
├── urls.py
│
└── templates/
    └── students/
        └── student_list.html
```

| Component         | File                                   |
| ----------------- | -------------------------------------- |
| Model             | `models.py`                            |
| View              | `views.py`                             |
| Template          | `templates/students/student_list.html` |
| URL configuration | `urls.py`                              |

## 6. MVT vs MVC

Django uses MVT, while many other frameworks describe their architecture using MVC.

| MVC        | Django MVT |
| ---------- | ---------- |
| Model      | Model      |
| View       | Template   |
| Controller | View       |

The naming differs, but both patterns separate application responsibilities.

In Django, the framework's URL dispatcher and request-handling machinery take care of much of the work commonly associated with a controller.

## 7. Key Takeaways

- MVT stands for Model, View, and Template.
- Model manages application data and database structure.
- View handles requests and application logic.
- Template controls the presentation of data.
- URL configuration connects incoming URLs to views.
- Django combines these components to generate HTTP responses.

## 8. Practice Questions

1. What does MVT stand for?
2. What is the responsibility of a Model?
3. Where do we write Django views?
4. What is the purpose of a Template?
5. What does `Student.objects.all()` do?
6. Which function can render a template with context data?
7. What is the role of URL configuration in Django?
8. Explain the difference between MVC and MVT.

## 9. Practical Task

**Task:**

Create a simple Student List page using the MVT architecture.

Requirements:

1. Create a `Student` model with name, email, and age.
2. Create a view that retrieves all students.
3. Create an HTML template to display student records.
4. Connect the view to a URL.
5. Open the page in your browser.

Use your existing `students` app for this exercise. Check your current model before adding another `Student` model.

## 10. Lesson Status

- [x] MVT architecture studied.
- [x] Model responsibilities understood.
- [x] View responsibilities understood.
- [x] Template responsibilities understood.
- [x] MVT request flow documented.
- [x] Practice questions completed.
- [x] Practical task completed.
