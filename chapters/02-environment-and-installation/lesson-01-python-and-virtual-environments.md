# Lesson 01 — Python and Virtual Environments

## 1. Introduction

Python is a high-level, interpreted programming language widely used for web development, automation, data science, artificial intelligence, and machine learning.

Django is a Python-based web framework. Therefore, Python must be installed before we can develop Django applications.

## 2. What Is Python?

Python provides the programming language and runtime environment required to execute Django applications.

Before working with Django, we should understand how to check the Python installation.

### Check Python Version

```powershell
python --version
```

Example output:

```text
Python 3.14.3
```

### Check pip Version

```powershell
pip --version
```

**What is pip?**

pip is Python's package installer. It allows developers to install and manage external Python libraries and frameworks.

## 3. What Is a Virtual Environment?

A virtual environment is an isolated Python environment that maintains project-specific packages and dependencies.

For example, suppose we have two Django projects:

- Project A requires Django version X.
- Project B requires Django version Y.

Installing different dependencies globally can create conflicts.

Virtual environments allow each project to maintain its own dependencies independently.

## 4. Why Do We Use Virtual Environments?

1. Dependency isolation between projects.
2. Better package management.
3. Reduced version conflicts.
4. Cleaner development environments.
5. Easier project setup and deployment.

## 5. Creating a Virtual Environment

Open PowerShell inside your Django project directory.

Run:

```powershell
python -m venv venv
```

### Command Explanation

| Part | Meaning |
|---|---|
| `python` | Runs the Python interpreter. |
| `-m` | Executes a Python module. |
| `venv` | Python's built-in virtual environment module. |
| `venv` | Name of the environment directory. |

After execution, Python creates a `venv` directory containing the isolated environment.

## 6. Activating a Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

After successful activation, the terminal displays the environment name:

```text
(venv) PS C:\project>
```

The `(venv)` prefix indicates that the virtual environment is active.

**Note:** If PowerShell blocks script execution, review the execution policy before changing it. Do not disable security protections unnecessarily.

## 7. Deactivating a Virtual Environment

To leave the active environment:

```powershell
deactivate
```

The `(venv)` prefix disappears from the terminal.

## 8. Installing Packages Inside a Virtual Environment

After activating the environment, install packages using pip.

Example:

```powershell
pip install django
```

The installed package is available within the active environment.

## 9. Verifying the Environment

Use the following command:

```powershell
python -m pip list
```

It displays the packages installed in the active environment.

To identify the Python executable being used:

```powershell
python -c "import sys; print(sys.executable)"
```

This helps verify that Python is running from the expected virtual environment.

## 10. Practical Workflow

A typical workflow for a new Django project:

```powershell
# Create project directory
mkdir my-django-project

# Enter project directory
cd my-django-project

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Upgrade pip
python -m pip install --upgrade pip

# Install Django
pip install django

# Verify Python environment
python -c "import sys; print(sys.executable)"
```

## 11. Important Commands Cheat Sheet

| Command | Purpose |
|---|---|
| `python --version` | Check Python version |
| `pip --version` | Check pip version |
| `python -m venv venv` | Create virtual environment |
| `.\venv\Scripts\Activate.ps1` | Activate environment |
| `deactivate` | Deactivate environment |
| `pip install package_name` | Install a package |
| `pip list` | List installed packages |
| `python -m pip freeze` | Display installed packages and versions |

## 12. Knowledge Check

1. What is Python?
2. Why does Django require Python?
3. What is a virtual environment?
4. Why should every Django project use an isolated environment?
5. What is the purpose of pip?
6. Which command creates a virtual environment?
7. How do you activate a virtual environment in Windows PowerShell?
8. How do you deactivate an active environment?

## 13. Practical Task

Create a new directory and perform the following tasks:

1. Create a Python virtual environment named `venv`.
2. Activate the environment.
3. Check the Python version.
4. Check the pip version.
5. Install a Python package.
6. Display installed packages.
7. Deactivate the environment.

## Key Takeaways

- Python is the foundation of Django development.
- pip manages Python package installations.
- Virtual environments isolate project dependencies.
- Each Django project can maintain its own package versions.
- Activating the environment ensures commands use its Python interpreter and installed packages.

---

**Lesson Status:** Completed

**Next Lesson:** Installing Django