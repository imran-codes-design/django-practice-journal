# Chapter 04 — Django URLs and Views

## Overview

This chapter explains how Django handles URL routing and connects incoming HTTP requests to views.

Django uses URL configurations to determine which view should process a particular request. Views contain application logic and return HTTP responses to clients.

This chapter covers URL patterns, project-level and application-level URL configurations, function-based views, dynamic URL parameters, URL naming, namespaces, and URL reversing.

## Learning Objectives

By completing this chapter, I have learned how to:

- Understand Django URL routing.
- Explain the difference between project-level and app-level URLs.
- Create and connect URL configurations.
- Define and use function-based views.
- Pass dynamic parameters through URLs.
- Name URL patterns and use them in templates.
- Understand URL namespaces and the `reverse()` function.
- Understand how Django processes incoming requests.

## Lessons

| Lesson | Topic | Status |
|---|---|---|
| 01 | Understanding Django URL Routing | Completed |
| 02 | Project-Level vs App-Level URLs | Completed |
| 03 | Creating and Connecting URL Patterns | Completed |
| 04 | Function-Based Views (FBVs) | Completed |
| 05 | Dynamic URLs and URL Parameters | Completed |
| 06 | URL Names, Namespaces and `reverse()` | Completed |

## Key Concepts

- URL Dispatcher
- URLconf
- `urlpatterns`
- `path()`
- `include()`
- Project-level `urls.py`
- App-level `urls.py`
- Function-Based Views
- `HttpResponse()`
- `render()`
- `redirect()`
- HTTP request object
- Dynamic URL parameters
- Path converters
- Named URL patterns
- URL namespaces
- `reverse()`
- Request-response flow

## Important Django Files

| File | Purpose |
|---|---|
| `manage.py` | Runs Django management commands. |
| `settings.py` | Defines `ROOT_URLCONF` and project settings. |
| Project `urls.py` | Defines the main URL configuration. |
| App `urls.py` | Defines application-specific URL patterns. |
| `views.py` | Contains view functions and application logic. |

## Practical Commands

```bash
python manage.py runserver
python manage.py check
```

## Chapter Progress

**Total Lessons:** 6

**Completed Lessons:** 6

**Pending Lessons:** 0

**Chapter Status:** Completed

## Key Takeaways

- URL routing connects incoming requests to views.
- Project-level and app-level URL configurations organize application routes.
- `include()` connects URL configurations.
- Function-Based Views handle HTTP requests and return responses.
- Dynamic URLs accept variable values through path converters.
- Named URLs reduce hardcoded URL paths.
- Namespaces organize URL names across applications.
- `reverse()` generates URLs inside Python code.

## Next Chapter

Chapter 05 — Django Templates and Static Files

---

This chapter is part of my Django learning journey, documenting Django concepts through practical implementation and structured notes.