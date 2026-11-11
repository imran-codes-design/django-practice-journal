# Lesson 02 — Template Variables, Tags and Filters

## Learning Objectives
- Display context values with template variables.
- Control output with template tags.
- Transform values with filters.
- Iterate over collections and handle empty results.

## 1. Template Variables
Use double curly braces to display a value supplied by the view:

```django
<h1>{{ title }}</h1>
<p>{{ student.name }}</p>
```
Django resolves the variable against the template context. Missing variables generally render as an empty string with the default configuration.

## 2. Template Tags
Tags use the percent-curly-brace delimiters and provide logic or template instructions.

```django
{% if is_enrolled %}
    <p>Student is enrolled.</p>
{% else %}
    <p>Enrollment is pending.</p>
{% endif %}
```

Loop example:

```django
<ul>
{% for student in students %}
    <li>{{ student.name }}</li>
{% empty %}
    <li>No students found.</li>
{% endfor %}
</ul>
```

Other useful tags include with, url, csrf_token, and include.

## 3. Template Filters
Filters modify a value before display. They use the pipe character:

```django
{{ name|title }}
{{ description|truncatewords:12 }}
{{ created_at|date:"d M Y" }}
{{ total|default:"Not available" }}
```

Filters can be chained, for example: name|lower|capfirst.

## 4. Practical Tasks
1. Pass a list of students from a view.
2. Display the list with a for loop.
3. Add an empty branch.
4. Use if/else for a status value.
5. Apply at least three filters to displayed values.

## 5. Common Errors
- Forgetting to close if and for blocks.
- Using a context key that does not match the view.
- Treating template syntax as ordinary Python; DTL has its own syntax and limitations.

## Key Takeaways
- Variables display context data.
- Tags provide control flow and template instructions.
- Filters format or transform values for presentation.

## Review Questions
1. What is the difference between a template variable and a tag?
2. What does the empty clause do in a loop?
3. How can multiple filters be chained?
