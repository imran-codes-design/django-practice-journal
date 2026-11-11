# Lesson 03 — Creating HTML Forms in Django

## Learning Objectives
- Understand the purpose of an HTML form.
- Use the action and method attributes.
- Connect a form to a Django URL.

## 1. Basic HTML Form
```html
<form action="/contact/" method="post">
    <label for="full_name">Full name</label>
    <input id="full_name" type="text" name="full_name" required>

    <button type="submit">Submit</button>
</form>
```

## 2. Important Attributes
- `action`: URL that receives the submitted form.
- `method`: HTTP method, usually GET or POST.
- `name`: key used to identify a submitted field.
- `type`: controls the kind of input.
- `required`: browser-side required-field check.

The `name` attribute is important: Django uses it as the key in submitted form data. An input with only an `id` and no `name` will not submit a useful field value.

## 3. Use Django URL Names
Prefer Django's URL reversing instead of hardcoding paths:
```html
<form action="{% url 'contact' %}" method="post">
    {% csrf_token %}
    <input type="text" name="full_name" required>
    <button type="submit">Send</button>
</form>
```
The URL name `contact` must exist in the URL configuration.

## Practical Task
Create a contact form with name, email, and message fields. Give its destination URL a name and use the `url` template tag.

## Common Mistakes
- Missing the input `name` attribute.
- Using a URL name that is not defined.
- Omitting CSRF token from a POST form.

## Key Takeaways
HTML forms collect input. The action determines the destination, the method determines how data is sent, and each submitted field needs a name.

## Review Questions
1. What does the form action attribute do?
2. Why does an input need a name?
3. Why is Django's `url` template tag useful?
