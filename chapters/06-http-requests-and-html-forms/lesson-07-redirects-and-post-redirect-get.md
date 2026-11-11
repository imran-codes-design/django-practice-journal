# Lesson 07 — Redirects and the POST-Redirect-GET Pattern

## Learning Objectives
- Understand Django redirects.
- Explain the POST-Redirect-GET pattern.
- Prevent accidental duplicate submissions on refresh.

## 1. Redirect a User
Django's `redirect()` shortcut returns an HTTP redirect response:
```python
from django.shortcuts import redirect

def done(request):
    return redirect("success")
```
The URL name `success` must be configured. You can also redirect to a model object or a URL, depending on the use case.

## 2. POST-Redirect-GET (PRG)
A common workflow is:
1. Browser sends a POST request.
2. Django validates and processes the data.
3. Django redirects to a result page.
4. Browser follows the redirect with a GET request.

This means refreshing the result page normally repeats the GET, not the original POST.

## 3. Example
```python
from django.shortcuts import redirect, render

def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save or process validated data here.
            return redirect("registration_success")
    else:
        form = StudentForm()

    return render(request, "register.html", {"form": form})
```

## 4. Redirect Is Not a Database Transaction
PRG reduces accidental resubmission caused by refreshing the result page, but it does not guarantee exactly-once processing. Important operations may also need database constraints or idempotency protections.

## Practical Task
After a valid form submission, redirect to a named success URL. Refresh the success page and confirm the browser does not prompt to resubmit the form.

## Common Mistakes
- Redirecting to a URL name that does not exist.
- Returning a success page directly after POST when PRG is intended.
- Assuming PRG alone prevents every duplicate operation.

## Key Takeaways
Use redirects after successful POST processing. PRG improves browser behavior and reduces accidental duplicate submissions.

## Review Questions
1. What are the three steps in PRG?
2. Which Django shortcut performs a redirect?
3. Does PRG guarantee exactly-once processing?
