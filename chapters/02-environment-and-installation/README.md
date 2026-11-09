# Chapter 02 â€” Django Environment and Installation

## Overview

Before developing Django applications, we need to prepare a Python development environment.

This chapter covers Python, virtual environments, Django installation, and the Django development server. It provides the foundation required to start building Django projects.

## Learning Objectives

By completing this chapter, you will understand how to:

- Check Python and pip versions.
- Understand Python virtual environments.
- Create and activate a virtual environment.
- Install Django using pip.
- Verify the Django installation.
- Run and stop the Django development server.
- Understand why isolated project dependencies are important.

## Lessons

| Lesson | Topic | Status |
|---|---|---|
| 01 | Python and Virtual Environments | Completed |
| 02 | Installing Django | Completed |
| 03 | Django Development Server | completed |

## Practical Commands

```powershell
# Check Python version
python --version

# Check pip version
pip --version

# Create a virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install Django
pip install django

# Check Django version
django-admin --version

# Start Django development server
python manage.py runserver
```

## Key Concepts

- **Python:** The programming language used to develop Django applications.
- **Virtual Environment:** An isolated Python environment for managing project-specific dependencies.
- **pip:** Python's package installer.
- **Django Installation:** Installing the Django framework using pip.
- **Development Server:** A local server used to run and test Django applications during development.

## Key Takeaways

- Every Django project should have an appropriately configured Python environment.
- Virtual environments help prevent dependency conflicts between projects.
- Django can be installed through pip.
- The development server allows developers to test applications locally.

## Chapter Progress

**Chapter Status:** Completed

## Next Chapter

**Chapter 03 â€” Django Projects and Applications**
