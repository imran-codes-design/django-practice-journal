# Lesson 03 — Template Inheritance

## Learning Objectives
- Explain why template inheritance is useful.
- Define a reusable parent template.
- Extend a parent template from a child template.
- Override named blocks.

## 1. Why Template Inheritance?
Most pages share elements such as navigation, a footer, and common CSS/JavaScript references. Copying these into every page creates duplication. Template inheritance lets a parent define the shared layout while child templates provide page-specific content.

## 2. Create a Base Template
Example: students/templates/students/base.html

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{% block title %}Student Portal{% endblock %}</title>
</head>
<body>
    <header><h1>Student Portal</h1></header>
    <main>{% block content %}{% endblock %}</main>
    <footer>Learning Django</footer>
</body>
</html>
```

## 3. Extend the Base Template
Example: students/templates/students/home.html

```django
{% extends "students/base.html" %}

{% block title %}Home | Student Portal{% endblock %}

{% block content %}
    <h2>Welcome</h2>
    <p>This is the home page.</p>
{% endblock %}
```
The extends tag should appear at the beginning of the child template, before other template content.

## 4. Practical Tasks
1. Create a base layout with header, navigation, main content, and footer.
2. Define blocks for page title, extra CSS, content, and extra JavaScript.
3. Create two child templates that extend the base.
4. Verify that shared layout changes appear on both pages.

## 5. Common Errors
- TemplateDoesNotExist: check the path in extends.
- Missing child content: ensure the block names match exactly.
- Unexpected content: place page-specific markup inside the intended block.

## Key Takeaways
- Parent templates contain shared structure.
- Child templates use extends and override named block sections.
- Inheritance reduces duplication and keeps layouts consistent.

## Review Questions
1. What is the purpose of template inheritance?
2. What do extends and block do?
3. Why must child block names match the parent?
