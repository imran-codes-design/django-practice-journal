# Lesson 08 — Practical Project: Student Registration Form

## Project Goal
Build a small student registration workflow that combines HTML forms, Django views, validation, CSRF protection, and redirects.

## Requirements
The form should collect:
- Full name
- Email address
- Age
- Course or program
- Optional short message

## Suggested Project Structure
```text
student_registration/
├── forms.py
├── urls.py
├── views.py
└── templates/
    └── student_registration/
        ├── register.html
        └── success.html
```
This is a suggested app-level structure; adapt it to the existing Django project rather than replacing existing files.

## Implementation Steps
1. Create a Django app or use a dedicated practice app.
2. Add the app to `INSTALLED_APPS`.
3. Define a `StudentRegistrationForm` in `forms.py`.
4. Create a view that displays an empty form on GET.
5. On POST, bind `request.POST` to the form and call `is_valid()`.
6. Display validation errors when the submitted data is invalid.
7. Process valid data. For this exercise, you may first display a success response; optionally persist records with a model in a later extension.
8. Redirect to a named success page after successful processing.
9. Add app-level URLs and include them in the project URL configuration.
10. Test valid, invalid, and repeated submissions.

## Acceptance Checklist
- [ ] GET displays the registration form.
- [ ] The form uses POST and includes `{% csrf_token %}`.
- [ ] Every field has appropriate server-side validation.
- [ ] Invalid submissions show useful errors.
- [ ] Valid submissions are processed only after `is_valid()`.
- [ ] Successful submission redirects to a named success page.
- [ ] URL names and namespaces are consistent.
- [ ] `python manage.py check` reports no project configuration issues.

## Optional Extensions
- Save registrations using a Django model.
- Add Bootstrap styling.
- Add a unique email constraint if the business rule requires it.
- Add automated tests for valid and invalid form submissions.

## Common Troubleshooting
- **403 CSRF failure:** check middleware, cookies, and the template token.
- **NoReverseMatch:** verify the URL name and namespace.
- **KeyError in cleaned_data:** check that `is_valid()` succeeded and the field name matches.
- **Form data missing:** check each input's `name` and the form's method.

## Final Review
Explain the full request lifecycle for a registration: browser form submission, Django URL routing, view validation, processing, redirect, and success-page GET.
