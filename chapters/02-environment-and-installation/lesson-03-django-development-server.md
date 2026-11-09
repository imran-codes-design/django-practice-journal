# Lesson 03 — Django Development Server

## 1. Introduction

The Django development server is a lightweight web server included with Django.

It allows developers to run and test Django applications locally during development without configuring a separate web server such as Nginx or Apache.

By default, Django runs on:

```text
http://127.0.0.1:8000/
```

## 2. What Is a Development Server?

A development server receives HTTP requests from a browser, processes them through the Django application, and returns HTTP responses.

For example:

1. A user opens a Django website in a browser.
2. The browser sends an HTTP request.
3. Django processes the request.
4. Django returns an HTTP response.
5. The browser displays the result.

## 3. Starting the Django Development Server

First, open PowerShell inside the directory containing `manage.py`.

Activate the virtual environment if it is not already active:

```powershell
.\venv\Scripts\Activate.ps1
```

Start the server:

```powershell
python manage.py runserver
```

Example terminal output:

```text
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

Django will display the response configured for your project's root URL.

**Important:** If no URL pattern is configured for `/`, Django may display a 404 page. This does not necessarily mean the development server has failed.

## 4. Understanding the runserver Command

```powershell
python manage.py runserver
```

| Part | Explanation |
|---|---|
| `python` | Executes the Python interpreter. |
| `manage.py` | Django project management script. |
| `runserver` | Starts the development server. |

## 5. Understanding the Localhost Address

The default development server address is:

```text
http://127.0.0.1:8000/
```

| Component | Meaning |
|---|---|
| `http` | Hypertext Transfer Protocol |
| `127.0.0.1` | Loopback IP address (localhost) |
| `8000` | Default development server port |

**What is localhost?**

Localhost refers to the computer on which the application is running.

It allows developers to test their applications locally.

## 6. Running Django on a Different Port

Django uses port `8000` by default.

To use another port, provide it as an argument:

```powershell
python manage.py runserver 8080
```

Now open:

```text
http://127.0.0.1:8080/
```

You can also specify a different local address and port:

```powershell
python manage.py runserver 127.0.0.1:9000
```

## 7. Accessing Django from Another Device on the Local Network

To make the development server listen on all network interfaces:

```powershell
python manage.py runserver 0.0.0.0:8000
```

Another device on the same network can access it using the development computer's LAN IP address, provided the firewall and network configuration allow access.

For example:

```text
http://192.168.1.10:8000/
```

Replace the example IP with your computer's actual local IP address.

**Security note:** Do not expose the development server to an untrusted network or use it as a production server.

## 8. Stopping the Development Server

To stop the server, press:

```text
CTRL + C
```

This terminates the running development server and returns control to the terminal.

## 9. Django System Checks

Before running the application, Django can check the project for common configuration problems.

Run:

```powershell
python manage.py check
```

Example output:

```text
System check identified no issues (0 silenced).
```

This confirms that Django's system checks did not identify any issues.

It does not guarantee that every feature of the application works correctly.

## 10. Common Development Server Problems

### Problem 1 — Port Already in Use

If port `8000` is already being used by another process, Django cannot bind to that port.

Use another port:

```powershell
python manage.py runserver 8080
```

### Problem 2 — manage.py Not Found

Possible reason: You are running the command from the wrong directory.

Move to the project directory containing `manage.py`:

```powershell
cd path\to\your\project
```

Then run:

```powershell
python manage.py runserver
```

### Problem 3 — Django Module Not Found

Possible reason: The virtual environment is not activated, or Django is not installed in the active Python environment.

Activate the environment and verify Django:

```powershell
.\venv\Scripts\Activate.ps1
python -m django --version
```

### Problem 4 — Page Not Found (404)

A running server does not guarantee that every URL exists.

Check the project's URL configuration, usually:

```text
myproject/urls.py
```

Make sure the requested URL has a matching URL pattern.

## 11. Development Server vs Production Server

| Development Server | Production Server |
|---|---|
| Used during development | Used to serve deployed applications |
| Intended for local testing | Designed for production deployment |
| Included with Django | Uses production server infrastructure |
| Not designed for production security and performance requirements | Configured for production reliability and security |

Common production components include:

- Gunicorn
- Nginx
- A production database
- Environment variables
- HTTPS configuration

## 12. Practical Workflow

Use the following commands to run a Django project:

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Check Django version
python -m django --version

# Check project configuration
python manage.py check

# Start development server
python manage.py runserver
```

Open the local URL in your browser and test the application.

Stop the server with `CTRL + C`.

## 13. Knowledge Check

1. What is the Django development server?
2. Which command starts the development server?
3. What is the default port used by Django?
4. What does `127.0.0.1` represent?
5. How can you run Django on port `8080`?
6. What is the purpose of `0.0.0.0`?
7. How do you stop the development server?
8. What does `python manage.py check` do?
9. Why should Django's development server not be used in production?
10. What is the difference between a development server and a production server?

## 14. Practical Task

Using your existing Django project:

1. Activate your virtual environment.
2. Check the installed Django version.
3. Run the Django system check.
4. Start the development server.
5. Open your project in the browser.
6. Run the server on port `8080`.
7. Stop the server using `CTRL + C`.

## Key Takeaways

- Django includes a development server for local testing.
- `python manage.py runserver` starts the server.
- The default address is `127.0.0.1:8000`.
- You can change the port when required.
- `python manage.py check` checks common project configuration issues.
- The development server is not suitable for production deployment.

---

**Lesson Status:** Completed

**Chapter Status:** Completed

**Next Chapter:** Chapter 03 — Django Projects and Applications