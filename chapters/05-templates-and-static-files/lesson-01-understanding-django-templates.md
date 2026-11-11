# Lesson 01 — Understanding Django Templates

## Learning Objectives
- Explain why web applications use templates.
- Understand the relationship between a view and a template.
- Render an HTML template with Django's render() shortcut.
- Pass dynamic data from Python to HTML through context.

## 1. What Is a Django Template?
A Django template is a text file, usually HTML, containing page structure and placeholders for dynamic data. Django's template engine processes those placeholders and produces the response content. Templates separate presentation from application logic.

## 2. View and Template Relationship
A view receives a request, prepares data, and selects a template. Django combines the template with context data and returns the rendered response.

```python
from django.shortcuts import render

def home(request):
    context = {
        "page_title": "Django Practice Journal",
        "learner": "Imran",
    }
    return render(request, "students/home.html", context)
```

Example template at students/templates/students/home.html:

```html
<h1>{{ page_title }}</h1>
<p>Welcome, {{ learner }}!</p>
```

The render() shortcut accepts the request, template name, and an optional context dictionary.

## 3. Template Organization
```text
students/
└── templates/
    └── students/
        └── home.html
```
The inner app-name directory namespaces the template and helps avoid collisions between apps.

## 4. Practical Tasks
1. Create an HTML template inside an app's templates/app_name/ directory.
2. Create a view that passes at least two context values.
3. Render the template using render().
4. Open the route and verify the dynamic values.

## 5. Testing
```powershell
python manage.py runserver
python manage.py check
```

## 6. Common Errors
- TemplateDoesNotExist: check the template path, app registration, and template settings.
- Blank variable: check the context key and spelling in the template.
- 404 response: verify that the URL pattern connects to the intended view.

## Key Takeaways
- Templates define presentation; views prepare and provide data.
- render() combines a template with context and returns an HTTP response.
- App-namespaced template directories keep templates organized.

## Review Questions
1. What problem do Django templates solve?
2. What are the three common arguments passed to render()?
3. Why use an app-name directory inside templates/?
