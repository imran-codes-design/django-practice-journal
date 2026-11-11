# Lesson 04 — Handling Form Data in Views

## Learning Objectives
- Read GET and POST values in a Django view.
- Check the request method before processing a submission.
- Return a useful response.

## 1. Read GET Data
For a URL such as `/search/?q=django`:
```python
def search(request):
    query = request.GET.get("q", "")
    return HttpResponse(f"Search term: {query}")
```

## 2. Read POST Data
```python
from django.http import HttpResponse

def contact(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        return HttpResponse(f"Thank you, {full_name}")
    return HttpResponse("Submit the contact form.")
```

## 3. Important Request Attributes
- `request.method`: HTTP method, such as GET or POST.
- `request.GET`: query-string parameters.
- `request.POST`: submitted form fields for form-encoded POST requests.
- `request.FILES`: uploaded files when the form is configured for file upload.

## 4. Never Trust Browser Input
Client-side attributes such as `required` improve usability but can be bypassed. Validate submitted values on the server before saving or using them. Avoid rendering untrusted input as raw HTML.

## Practical Task
Create a form with a name field. On GET, show the form; on POST, read and display a safely handled name.

## Common Mistakes
- Accessing POST values without checking the request method.
- Using the wrong field name in `request.POST.get()`.
- Treating browser validation as sufficient server-side validation.

## Key Takeaways
Django exposes query parameters through `request.GET` and form submissions through `request.POST`. Always validate untrusted input.

## Review Questions
1. How do you read a query parameter named q?
2. How do you read a POST field named email?
3. Why is server-side validation necessary?
