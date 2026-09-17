# 🚀 Django Development — Day 1 Roadmap

> **Goal:** Build a strong Django foundation before moving into advanced development.
>
> **Day:** 1  
> **Focus:** Django fundamentals, project structure, setup, and the request/response flow  
> **Study target:** ~9–9.5 focused hours, split into learning + practice blocks

---

## 🎯 Day 1 Outcome

By the end of Day 1, you should be able to:

- Explain what Django is and why it is used.
- Set up a Django development environment.
- Create and run a Django project.
- Understand Django's project/app structure.
- Understand the basic request → URL → view → response flow.
- Create a basic app and connect it to the project.
- Create simple views and URL routes.
- Understand the role of `settings.py`, `urls.py`, `manage.py`, and `views.py`.
- Build a small first Django project instead of only watching tutorials.

---

## ⏱️ Day 1 Timetable

| Block | Time | Focus |
|---|---:|---|
| 🧠 Block 1 | 60 min | Python/Django prerequisites + Django overview |
| ⚙️ Block 2 | 90 min | Environment setup + Django installation |
| 🏗️ Block 3 | 90 min | Project creation + Django structure |
| 🔗 Block 4 | 90 min | URLs, views, request/response cycle |
| 💻 Block 5 | 120 min | Hands-on mini project |
| 🧪 Block 6 | 90 min | Practice, debugging + revision |
| **Total** | **~9 hrs** | **Focused learning + implementation** |

> **Rule:** Keep breaks between blocks. The target is focused study time, not sitting continuously for 9 hours.

---

# 1. 🧠 Django Fundamentals

### Concepts

- What is Django?
- Why Django is used for backend/web development
- Django as a Python web framework
- MVT architecture:
  - Model
  - View
  - Template
- Django's batteries-included philosophy
- Django project vs Django application
- Development server
- Basic Django terminology

### Practice

Write short answers for:

1. What problem does Django solve?
2. What is the difference between a project and an app?
3. What does MVT mean?
4. What happens when a user opens a Django URL?

---

# 2. ⚙️ Environment Setup

### Concepts

- Python environment
- Virtual environment
- Installing Django
- Checking Django version
- Creating a project
- Running the development server

### Commands to practice

```bash
python -m venv venv
```

Activate the virtual environment according to your operating system, then:

```bash
pip install django
django-admin --version
django-admin startproject config .
python manage.py runserver
```

### Checkpoint

You should be able to open the Django development server in your browser and understand that the server is running your Django project.

---

# 3. 🏗️ Understand Django Project Structure

After creating the project, inspect the files carefully.

Typical structure:

```text
project/
├── manage.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── venv/
```

### Understand each file

| File | Purpose |
|---|---|
| `manage.py` | Command-line utility for working with the Django project |
| `settings.py` | Project configuration |
| `urls.py` | Main URL routing configuration |
| `asgi.py` | ASGI application entry point |
| `wsgi.py` | WSGI application entry point |
| `__init__.py` | Marks the package |

### Important

Do not just memorize the filenames. Open each important file and understand what Django generated automatically.

---

# 4. 🔗 Django Apps

Create your first application:

```bash
python manage.py startapp core
```

Expected structure:

```text
core/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
├── models.py
├── tests.py
└── views.py
```

### Learn the role of:

- `views.py`
- `models.py`
- `admin.py`
- `apps.py`
- `tests.py`
- `migrations/`

### Register the app

Understand how an application is added to:

```python
INSTALLED_APPS
```

inside `settings.py`.

---

# 5. 🌐 URLs + Views

This is one of the most important Day 1 concepts.

Understand:

```text
Browser
   ↓
URL
   ↓
URL configuration
   ↓
View
   ↓
Response
   ↓
Browser
```

### Create a simple view

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django!")
```

### Connect the view to a URL

Understand how a URL pattern points to the view.

Example:

```python
from django.urls import path
from core import views

urlpatterns = [
    path("", views.home, name="home"),
]
```

### Practice

Create at least:

- `/`
- `/about/`
- `/contact/`

Each route should return a different response.

---

# 6. 🔄 Request → Response Cycle

Understand this flow clearly:

```text
User enters URL
       ↓
Browser sends HTTP request
       ↓
Django receives request
       ↓
URL dispatcher checks urlpatterns
       ↓
Matching view is selected
       ↓
View processes request
       ↓
View returns HttpResponse
       ↓
Django sends HTTP response
       ↓
Browser displays result
```

### Key terms

- HTTP request
- HTTP response
- URL
- route/path
- view
- `request`
- `HttpResponse`
- URL dispatcher

### Checkpoint

Explain the complete flow in your own words without looking at notes.

---

# 7. 💻 Day 1 Mini Project

## Project: Django Personal Home Page

Build a small Django website with:

```text
/
├── Home
├── About
├── Skills
└── Contact
```

### Requirements

- Create a Django project.
- Create a `core` app.
- Register the app.
- Create views for each page.
- Create URL routes.
- Return different responses for each page.
- Run the project locally.
- Test every URL manually.

### Suggested route structure

```text
/           → Home
/about/     → About
/skills/    → Skills
/contact/   → Contact
```

### Goal

Do this yourself first. Use notes/tutorials only when you are stuck.

---

# 8. 🧪 Practice & Debugging

Spend dedicated time intentionally breaking and fixing the project.

Try:

- Remove an import.
- Change a URL path.
- Rename a view.
- Forget to register the app.
- Create an incorrect URL pattern.
- Stop and restart the development server.
- Read Django's error page.
- Identify where the error originated.

### Debugging habit

When something breaks:

```text
Read the error
   ↓
Find the file
   ↓
Find the line
   ↓
Understand the error
   ↓
Fix it
   ↓
Run again
```

Do not immediately copy a solution.

---

# 9. 🔁 Day 1 Revision

At the end of the day, revise these concepts:

### Must Know

- [ ] What Django is
- [ ] Django project vs app
- [ ] MVT concept
- [ ] Virtual environment
- [ ] Django installation
- [ ] `manage.py`
- [ ] `settings.py`
- [ ] `urls.py`
- [ ] `views.py`
- [ ] `models.py`
- [ ] `admin.py`
- [ ] `startproject`
- [ ] `startapp`
- [ ] `runserver`
- [ ] URL routing
- [ ] Views
- [ ] HTTP request/response
- [ ] Request → URL → View → Response flow

---

# 🧠 Day 1 Self-Test

Answer these without notes:

1. What is Django?
2. What is the difference between a Django project and app?
3. What does MVT stand for?
4. What is the purpose of `manage.py`?
5. What is `settings.py` used for?
6. What is `urls.py` responsible for?
7. What is a Django view?
8. What does `HttpResponse` do?
9. Explain the Django request/response flow.
10. How do you create a Django project?
11. How do you create an app?
12. How do you run the development server?
13. How does a URL reach a view?
14. Why do we use a virtual environment?

**Target:** Be able to answer conceptually, not just reproduce commands.

---

# 🏆 Day 1 Completion Criteria

Day 1 is complete when you can independently:

- ✅ Set up a Django environment.
- ✅ Create a project.
- ✅ Create an app.
- ✅ Register an app.
- ✅ Run the server.
- ✅ Create multiple views.
- ✅ Connect URLs to views.
- ✅ Explain the request/response cycle.
- ✅ Build the mini project.
- ✅ Debug at least a few intentional errors.
- ✅ Explain the core concepts without relying on notes.

---

## 📌 Day 1 Principle

> **Don't measure Day 1 by how many Django topics you watched. Measure it by how much Django you can build without copying.**

**Next:** Day 2 should continue from this foundation rather than repeating Day 1.
