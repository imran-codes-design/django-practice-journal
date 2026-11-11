# Lesson 01 — Understanding HTTP Requests and Responses

## Learning Objectives
- Define HTTP and explain its role in web applications.
- Identify the main parts of a request and response.
- Describe how a request reaches a Django view.

## 1. What Is HTTP?
HTTP (Hypertext Transfer Protocol) is the communication protocol used by browsers and web servers. A browser sends an HTTP request; the server processes it and returns an HTTP response.

## 2. Request-Response Cycle
1. A user opens a URL or submits a form.
2. The browser sends an HTTP request to the server.
3. Django receives the request through its request handling system.
4. URL configuration matches the requested path to a view.
5. The view performs the required work.
6. Django returns an HTTP response to the browser.

## 3. Parts of an HTTP Request
- Method: what action is being requested, such as GET or POST.
- URL/path: the resource being requested.
- Headers: additional metadata, such as content type.
- Body: optional data sent with the request, commonly used by POST.

## 4. Parts of an HTTP Response
- Status code: indicates the result, such as 200 or 404.
- Headers: metadata about the response.
- Body: returned content, often HTML or JSON.

## 5. A Simple Django View
```python
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, Django!")
```
The `request` parameter contains information about the incoming request. `HttpResponse` creates the response sent back to the browser.

## Practical Task
Create a view that returns a short message. Connect it to a URL and open that URL in the browser.

## Common Mistakes
- Confusing a URL with a view function.
- Forgetting to return an HTTP response from a view.
- Assuming every request is a form submission.

## Key Takeaways
- HTTP follows a request-response model.
- Django routes requests to views.
- A view returns a response.

## Review Questions
1. What does HTTP stand for?
2. What is the difference between a request and a response?
3. What is the role of a Django view?
