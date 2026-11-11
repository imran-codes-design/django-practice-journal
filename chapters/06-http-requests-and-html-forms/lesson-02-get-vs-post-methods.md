# Lesson 02 — GET vs POST Methods

## Learning Objectives
- Explain the purpose of GET and POST.
- Identify where submitted data is carried.
- Select an appropriate method for a form.

## 1. GET
GET requests retrieve information. Data may appear in the URL as a query string.

Example:
```text
/search/?q=django
```
Django reads query-string values through `request.GET`.

## 2. POST
POST requests send data to the server for processing, such as creating a record or submitting a form. Form values are commonly available through `request.POST`.

## 3. Comparison
| GET | POST |
|---|---|
| Commonly retrieves data | Commonly submits data for processing |
| Parameters appear in URL | Form data is normally in request body |
| Can be bookmarked with query parameters | Not represented as a normal query URL |
| Should not change server state | Often used for state-changing actions |

POST is not encryption. Use HTTPS to protect data in transit. Sensitive values should not be placed in a URL.

## 4. Check the Method in a View
```python
from django.http import HttpResponse

def method_check(request):
    if request.method == "POST":
        return HttpResponse("POST request received")
    return HttpResponse("GET request received")
```

## Practical Task
Create a view that displays different messages for GET and POST requests. Use a browser address bar for GET and a form for POST.

## Common Mistakes
- Using GET for actions that change data.
- Assuming POST automatically makes data secure.
- Forgetting to check `request.method`.

## Key Takeaways
Choose the method according to the purpose of the request. Use HTTPS for transport security.

## Review Questions
1. Which method is normally used to retrieve a page?
2. Where does Django expose query-string parameters?
3. Does POST encrypt submitted data?
