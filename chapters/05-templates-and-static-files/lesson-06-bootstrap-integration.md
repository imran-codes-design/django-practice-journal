# Lesson 06 — Bootstrap Integration with Django Templates

## Learning Objectives
- Explain how Bootstrap can be included in a Django page.
- Add Bootstrap styles and JavaScript to a shared base template.
- Reuse the base layout across child templates.
- Verify Bootstrap components and responsive utilities.

## 1. What Is Bootstrap?
Bootstrap is a frontend CSS framework providing responsive layout utilities and prebuilt interface components. It works with Django because Django templates render HTML, CSS, and JavaScript.

## 2. Include Bootstrap in the Base Template
Use the official Bootstrap documentation to obtain current CDN links. Add the stylesheet inside the base template's head and the JavaScript bundle before the closing body tag.

```html
<head>
    <!-- Other head elements -->
    <link href="BOOTSTRAP_CSS_CDN" rel="stylesheet">
</head>
<body>
    {% block content %}{% endblock %}
    <script src="BOOTSTRAP_JS_BUNDLE_CDN"></script>
</body>
```

Replace the placeholders with official CDN URLs and matching integrity/crossorigin attributes supplied by Bootstrap's documentation. Alternatively, install and serve Bootstrap assets locally.

## 3. Use Bootstrap Classes
```html
<div class="container py-4">
    <div class="card shadow-sm">
        <div class="card-body">
            <h1 class="h3">Student Portal</h1>
            <p class="text-muted">Manage student information.</p>
            <a href="#" class="btn btn-primary">Explore</a>
        </div>
    </div>
</div>
```
Bootstrap classes style the HTML; Django remains responsible for routing, views, templates, and backend behavior.

## 4. Combine Bootstrap with Template Inheritance
Add Bootstrap once in the shared base template. Child templates can extend the base and focus on page-specific content. This avoids repeating framework asset references on every page.

## 5. Practical Tasks
1. Add Bootstrap to a shared base template.
2. Create a child template that extends the base.
3. Build a responsive navigation bar and card.
4. Add a Bootstrap-styled form or alert.
5. Resize the browser and verify responsive behavior.
6. Check the browser console and Network panel for errors.

## 6. Common Errors
- Mixing incompatible Bootstrap CSS and JavaScript versions.
- Omitting the JavaScript bundle when using interactive components.
- Forgetting that Bootstrap styling does not replace Django form validation or backend security.

## Key Takeaways
- Bootstrap is a frontend framework; it does not replace Django's template engine.
- A shared base template is a good place for common framework assets.
- Use official Bootstrap documentation for current CDN URLs and version-specific setup.

## Review Questions
1. Does Bootstrap replace Django's template engine?
2. Why include common Bootstrap assets in a base template?
3. Which Bootstrap components require JavaScript?
