# Chapter 06 — HTTP Requests and HTML Forms

## Overview
This chapter explains how a browser communicates with a Django application and how Django receives, validates, and processes data submitted through HTML forms. Documentation is separate from executable Django source code.

## Learning Objectives
- Explain the HTTP request-response cycle.
- Distinguish GET and POST requests and choose the appropriate method.
- Build HTML forms that submit data to Django views.
- Read submitted values using `request.GET` and `request.POST`.
- Understand CSRF protection and use `{% csrf_token %}`.
- Validate submitted data and return useful errors.
- Use redirects and the POST-Redirect-GET pattern.
- Build a practical student registration form.

## Lessons
| Lesson | Topic | Status |
|---|---|---|
| 01 | Understanding HTTP Requests and Responses | Planned |
| 02 | GET vs POST Methods | Planned |
| 03 | Creating HTML Forms in Django | Planned |
| 04 | Handling Form Data in Views | Planned |
| 05 | CSRF Protection in Django Forms | Planned |
| 06 | Form Validation and Error Handling | Planned |
| 07 | Redirects and the POST-Redirect-GET Pattern | Planned |
| 08 | Practical Project: Student Registration Form | Planned |

## Key Concepts
- HTTP methods, request headers, response status codes
- Request-response lifecycle
- GET query strings and POST form data
- HTML form attributes: action, method, name, and input types
- `request.GET`, `request.POST`, and `request.method`
- CSRF tokens and Django middleware
- Server-side validation and cleaned data
- Redirect responses and duplicate form submissions

## Practical Workflow
1. Trace a browser request from URL to Django view and response.
2. Compare GET and POST using a small example.
3. Create an HTML form and connect its action to a named URL.
4. Process submitted values in a view.
5. enable CSRF protection and test a valid POST request.
6. Add validation for required fields and invalid input.
7. Redirect after successful submission.
8. Build and test a student registration form.

## Useful Commands
```powershell
python manage.py runserver
python manage.py check
```

## Chapter Progress
**Total Lessons:** 8  
**Completed Lessons:** 8  
**Pending Lessons:** 0
**Chapter Status:** completed

## Next Chapter
To be decided after completing this chapter.

---
This chapter is part of my Django Practice Journal. Practical implementation and lesson notes will be added progressively as each lesson is studied and verified.
