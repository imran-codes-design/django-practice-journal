# Lesson 05 — Static Files: CSS, JavaScript and Images

## Learning Objectives
- Distinguish static files from templates and uploaded media.
- Organize app-level static assets.
- Configure the static URL prefix.
- Load CSS, JavaScript, and images using Django static template tags.

## 1. What Are Static Files?
Static files are assets used by a website, such as CSS stylesheets, JavaScript files, fonts, and images. They are different from user-uploaded media, which requires separate media configuration.

## 2. App-Level Static Directory
```text
students/
├── static/
│   └── students/
│       ├── css/style.css
│       ├── js/app.js
│       └── images/logo.png
└── templates/
    └── students/home.html
```

## 3. Static Settings
A typical development setting includes:

```python
STATIC_URL = "static/"
```

If using a project-level static directory, configure STATICFILES_DIRS with its path. For production collection, Django commonly uses STATIC_ROOT with the collectstatic command. A production web server or storage service serves the collected files.

## 4. Load Assets in a Template
At the top of a template:

```django
{% load static %}
```

Reference CSS, JavaScript, and an image:

```html
<link rel="stylesheet" href="{% static 'students/css/style.css' %}">
<script src="{% static 'students/js/app.js' %}" defer></script>
<img src="{% static 'students/images/logo.png' %}" alt="Student portal logo">
```

## 5. Practical Tasks
1. Create a CSS file and apply a visible style.
2. Add a JavaScript file and verify it executes.
3. Add an image and render it using the static tag.
4. Inspect the browser Network panel for failed asset requests.

## 6. Common Errors
- Forgetting to load the static tag library.
- Using an incorrect path after the static URL prefix.
- Duplicating or omitting the app namespace in a static path.
- Confusing static files with uploaded media.
- Expecting development static-file behavior to be the production deployment strategy.

## Key Takeaways
- Static assets include CSS, JavaScript, images, and fonts.
- Use load static and the static tag in templates.
- Development serving and production static deployment are different concerns.

## Review Questions
1. What is the difference between static files and uploaded media?
2. What does STATIC_URL define?
3. What is the purpose of collectstatic?
