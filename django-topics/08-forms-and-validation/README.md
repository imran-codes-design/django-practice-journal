# Chapter 08: Django Forms and Validation

## 1. Learning Objectives

By completing this chapter, I learned how to:

- Create Django forms using `forms.Form`.
- Define form fields and their validation rules.
- Use `CharField`, `EmailField`, `IntegerField`, and `ChoiceField`.
- Handle submitted form data using GET and POST requests.
- Validate submitted data using `form.is_valid()`.
- Access validated data using `form.cleaned_data`.
- Display validation errors in Django templates.
- Understand the difference between a choice value and its display label.

## 2. Important Concepts

### Django Forms

Django Forms provide a structured way to collect and validate user input.

### forms.Form

`forms.Form` is used to define a form manually using Python.

### Field Validation

Django validates input according to the field type and configured rules.

Examples:

- `CharField`: Validates text.
- `EmailField`: Validates email format.
- `IntegerField`: Validates integer values.
- `ChoiceField`: Restricts input to predefined choices.

### form.is_valid()

Checks whether submitted data passes the configured validation rules.

### form.cleaned_data

Contains validated and converted form data after successful validation.

### ChoiceField: Value vs Display Label

A Django choice is defined as:

```python
('bio', 'Data Science')
```

- `bio` is the stored/submitted value.
- `Data Science` is the human-readable label.

To retrieve the display label:

```python
department_value = form.cleaned_data['department']

department_label = dict(
    form.fields['department'].choices
).get(department_value, department_value)
```

## 3. Practical Implementation

**Project:** Student Registration Form

**App:** `students`

Files involved:

```text
students/
├── forms.py
├── views.py
└── templates/
    └── students/
        ├── register.html
        └── success.html
```

### Main implementation

1. Created `students/forms.py`.
2. Defined a `StudentForm` using `forms.Form`.
3. Added student name, email, age, and department fields.
4. Configured field-level validation.
5. Updated the view to process POST requests.
6. Used `form.is_valid()` to validate submissions.
7. Accessed validated values through `cleaned_data`.
8. Updated the registration template using `{{ form.as_p }}`.

## 4. Testing

Test the following cases:

| Test case | Expected result |
|---|---|
| Valid student details | Registration succeeds |
| Invalid email | Validation error |
| Age below minimum | Validation error |
| Empty required field | Validation error |
| Valid department choice | Correct department value |
| Invalid department choice | Validation error |

## 5. Key Takeaways

- Django Forms reduce manual form-processing code.
- Server-side validation is essential.
- `cleaned_data` should be used after successful validation.
- ChoiceField values and labels are different.
- `{{ form.as_p }}` provides a quick way to render fields and errors.

## 6. Next Learning Topic

**ModelForm and Database Integration**

Learn how to connect Django forms with database models and save validated student records using `ModelForm`.