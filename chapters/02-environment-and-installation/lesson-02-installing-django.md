# Lesson 02 — Installing Django

## 1. Introduction

Django is a high-level Python web framework used to develop secure, scalable, and maintainable web applications.

Before creating a Django project, we need to install the Django framework in our Python development environment.

## 2. Prerequisites

Before installing Django, make sure you have:

- Python installed.
- pip available.
- A project directory.
- A virtual environment created and activated.

Check Python:

```powershell
python --version
```

Check pip:

```powershell
python -m pip --version
```

## 3. Installing Django

Django can be installed using Python's package installer, pip.

First, activate your virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

Then install Django:

```powershell
python -m pip install django
```

Using `python -m pip` ensures that pip belongs to the Python interpreter currently being used.

## 4. Verifying Django Installation

After installation, check the Django version:

```powershell
django-admin --version
```

You can also use:

```powershell
python -m django --version
```

Both commands help verify that Django is installed and accessible.

## 5. Understanding Django Package Installation

When Django is installed, pip also installs its required dependencies.

To see the installed packages:

```powershell
python -m pip list
```

To display package details:

```powershell
python -m pip show django
```

This displays information such as the installed version and installation location.

## 6. Understanding requirements.txt

A Django project often uses a `requirements.txt` file to record its Python dependencies.

Generate the file:

```powershell
python -m pip freeze > requirements.txt
```

Example:

```text
Django==6.1.2
```

The actual contents depend on the packages and versions installed in your environment.

### Installing Dependencies from requirements.txt

When setting up the project on another machine:

```powershell
python -m pip install -r requirements.txt
```

This installs the listed dependencies.

## 7. Updating Django

To upgrade Django to the latest compatible release available from your configured package index:

```powershell
python -m pip install --upgrade django
```

Check the installed version afterward:

```powershell
python -m django --version
```

**Important:** Before upgrading an existing project, check Django's supported Python versions and release compatibility.

## 8. Common Installation Problems

### Problem 1 — Python Is Not Recognized

Possible reason: Python is not installed correctly or its executable directory is not available through PATH.

Check:

```powershell
python --version
```

On Windows, you can also try:

```powershell
py --version
```

### Problem 2 — pip Is Not Recognized

Use:

```powershell
python -m pip --version
```

This invokes pip through the active Python interpreter.

### Problem 3 — Django Is Not Recognized

Make sure the virtual environment is activated and Django is installed in it.

Run:

```powershell
python -m pip show django
```

Then verify:

```powershell
python -m django --version
```

### Problem 4 — Wrong Django Version

Check the version installed in the active environment:

```powershell
python -m django --version
```

If necessary, install a specific version:

```powershell
python -m pip install django==6.1.2
```

Use a version compatible with your Python version and project requirements.

## 9. Complete Installation Workflow

```powershell
# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install Django
python -m pip install django

# Verify Django version
python -m django --version

# View installed packages
python -m pip list

# Save dependencies
python -m pip freeze > requirements.txt
```

## 10. Knowledge Check

1. What is Django?
2. Which tool is used to install Django?
3. Why should Django be installed inside a virtual environment?
4. What does `python -m pip install django` do?
5. How can you verify the installed Django version?
6. What is the purpose of `requirements.txt`?
7. Which command installs dependencies from `requirements.txt`?
8. What is the difference between installing and upgrading Django?

## 11. Practical Task

Inside your active virtual environment:

1. Install Django.
2. Verify the installed version.
3. Display Django package information.
4. List all installed packages.
5. Generate a `requirements.txt` file.
6. Open the file and inspect its contents.

## Key Takeaways

- Django is installed using pip.
- Installing Django inside a virtual environment keeps dependencies isolated.
- Django's version can be checked using `python -m django --version`.
- `requirements.txt` records project dependencies.
- Dependencies can be installed on another machine using `pip install -r requirements.txt`.

---

**Lesson Status:** Completed

**Next Lesson:** Django Development Server