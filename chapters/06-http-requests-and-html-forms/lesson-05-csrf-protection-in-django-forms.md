# Lesson 05 — CSRF Protection in Django Forms

## Learning Objectives
- Explain Cross-Site Request Forgery (CSRF).
- Understand Django's CSRF protection.
- Add a CSRF token to a POST form.

## 1. What Is CSRF?
Cross-Site Request Forgery is an attack in which a malicious site attempts to cause a user's browser to submit an unwanted request to another site where the user is authenticated.

## 2. Django Protection
Django includes CSRF middleware in the default project configuration. For unsafe requests such as POST, Django checks for a valid CSRF token.

## 3. Add the Token to a Template
```html
<form method="post">
    {% csrf_token %}
    <input type="text" name="full_name" required>
    <button type="submit">Submit</button>
</form>
```
Place `{% csrf_token %}` inside each internal POST form rendered by Django.

## 4. Common CSRF Errors
A `403 Forbidden` response with a CSRF verification failure can occur when:
- The token is missing from the form.
- The form submits to an unexpected or incorrectly configured endpoint.
- Cookies are blocked or the CSRF cookie is not available.
- A custom AJAX request does not send the CSRF token correctly.

Do not disable CSRF middleware to make a form work. Fix the token or request configuration.

## Practical Task
Submit a Django POST form with the token, then remove the token temporarily in a local practice environment and observe the failure. Restore it immediately.

## Key Takeaways
CSRF protection helps prevent forged requests. Keep Django's protection enabled and include the template token in POST forms.

## Review Questions
1. What does CSRF stand for?
2. Which template tag adds the token?
3. Should CSRF middleware be disabled to fix a missing-token error?
