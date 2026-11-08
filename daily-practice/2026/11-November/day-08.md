# Daily Django Learning — November 8, 2026

## Today's Chapter

Chapter 08: Django Forms and Validation

**Chapter documentation:** [Chapter 08 — Forms and Validation](../../../django-topics/08-forms-and-validation/README.md)

## Learning Completed

- Created a Django form using `forms.Form`.
- Defined student registration fields.
- Configured required fields and validation rules.
- Implemented POST request handling.
- Validated submitted information with `is_valid()`.
- Retrieved validated information using `cleaned_data`.
- Rendered Django forms using `form.as_p`.
- Understood ChoiceField values and display labels.

## Practical Task

**Student Registration Form**

Implemented a registration form in the existing `students` app.

### Files Created or Updated

- `students/forms.py` — created the StudentForm.
- `students/views.py` — implemented form handling and validation.
- `students/templates/students/register.html` — updated the registration template.

## Important Concept Learned

Django ChoiceField uses two values:

```python
('bio', 'Data Science')
```

The first value (`bio`) is submitted to the server. The second value (`Data Science`) is displayed to the user.

## Today's Result

Completed the Student Registration Form practical and published the implementation to GitHub.

## Next Session

Study Django ModelForm and learn how to save validated form data into the database.