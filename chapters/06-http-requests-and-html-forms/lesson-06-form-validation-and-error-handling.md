# Lesson 06 — Form Validation and Error Handling

## Learning Objectives
- Explain why submitted data must be validated.
- Understand basic Django form validation.
- Display validation errors to the user.

## 1. Browser Validation vs Server Validation
HTML attributes such as `required` and `type="email"` provide convenient browser checks. They are not a security boundary. The server must validate every submitted value.

## 2. A Django Form
```python
from django import forms

class StudentForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=16, max_value=100)
```

## 3. Validate in a View
```python
def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["full_name"]
            # Process validated data here.
            return HttpResponse("Registration accepted")
    else:
        form = StudentForm()

    return render(request, "register.html", {"form": form})
```
After `is_valid()` succeeds, use `cleaned_data` for validated values. If validation fails, the bound form contains errors.

## 4. Display the Form and Errors
```html
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
```
Django's default form rendering includes field errors. You can customize error presentation later.

## Practical Task
Add name, email, and age fields. Test valid input, missing input, an invalid email, and an age outside the allowed range.

## Common Mistakes
- Reading `cleaned_data` before calling `is_valid()`.
- Saving unvalidated raw POST values.
- Forgetting to return the bound form when validation fails.

## Key Takeaways
Validate data on the server. Use Django forms and process `cleaned_data` only after successful validation.

## Review Questions
1. What does `form.is_valid()` return?
2. Where are validated values stored?
3. What should a view return when the form is invalid?
