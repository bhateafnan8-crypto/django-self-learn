# Django Day 4 — URLs, Views & Templates

## Day 4 Goal

Understand how a Django request moves through:

**Browser → URL → View → Template → Response**

By the end of Day 4, you should be able to create URL routes, write function-based views, render HTML templates, pass data from views to templates, and use dynamic URL parameters.

---

## 1. Django Request Flow

A basic Django page request follows this flow:

```text
User enters URL
      ↓
Project URL configuration
      ↓
App URL configuration
      ↓
View function
      ↓
Template
      ↓
HTTP Response
      ↓
Browser
```

### Key idea

- **URL** decides which view should handle the request.
- **View** contains the Python logic.
- **Template** contains the HTML presentation.
- **Response** is sent back to the browser.

---

## 2. Project URL Configuration

The main URL configuration is usually located at:

```text
project_name/urls.py
```

Example:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
]
```

### `path()`

`path()` connects a URL pattern to a view or another URL configuration.

```python
path("about/", views.about)
```

### `include()`

`include()` allows an app to maintain its own URL patterns.

```python
path("", include("myapp.urls"))
```

This keeps the project structure clean and scalable.

---

## 3. App-Level URLs

Create:

```text
myapp/urls.py
```

Example:

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
```

### Why use app-level URLs?

Instead of putting every route inside the project's `urls.py`, each app can manage its own routes.

```text
project/
├── urls.py
│
└── myapp/
    ├── urls.py
    ├── views.py
    └── models.py
```

---

## 4. Function-Based Views

A view is a Python function that receives a request and returns a response.

Example:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Django!")
```

URL:

```python
path("", views.home, name="home")
```

When the user visits `/`, Django calls:

```python
home(request)
```

---

## 5. `HttpResponse`

`HttpResponse` can return a simple response directly.

```python
from django.http import HttpResponse

def about(request):
    return HttpResponse("This is the About page.")
```

This is useful for learning and simple responses, but real applications usually use templates for HTML pages.

---

## 6. Django Templates

Templates allow you to separate HTML presentation from Python logic.

Recommended structure:

```text
myapp/
├── templates/
│   └── myapp/
│       ├── home.html
│       └── about.html
├── views.py
└── urls.py
```

Example `home.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to Django</h1>
    <p>This is my home page.</p>
</body>
</html>
```

---

## 7. Rendering a Template

Instead of returning raw HTML with `HttpResponse`, use `render()`.

```python
from django.shortcuts import render

def home(request):
    return render(request, "myapp/home.html")
```

`render()` combines:

- the request
- the template
- optional context data

and returns an HTTP response.

---

## 8. Passing Data from View to Template

A view can send Python data to a template.

### View

```python
from django.shortcuts import render

def home(request):
    context = {
        "name": "Django Developer",
        "course": "Django",
    }

    return render(request, "myapp/home.html", context)
```

### Template

```html
<h1>Hello {{ name }}</h1>
<p>You are learning {{ course }}.</p>
```

Output:

```text
Hello Django Developer
You are learning Django.
```

---

## 9. Template Variables

Django template variables use:

```text
{{ variable }}
```

Example:

```html
<h1>{{ name }}</h1>
```

If the context contains:

```python
{"name": "Alex"}
```

the template displays:

```text
Alex
```

---

## 10. Template Tags

Template tags use:

```text
{% ... %}
```

They are used for logic and template operations.

Example:

```html
{% if user_name %}
    <h1>Hello {{ user_name }}</h1>
{% else %}
    <h1>Hello Guest</h1>
{% endif %}
```

---

## 11. Template `if` Statement

Example:

```html
{% if age >= 18 %}
    <p>Adult</p>
{% else %}
    <p>Minor</p>
{% endif %}
```

Template conditions help control what is displayed.

---

## 12. Template `for` Loop

A list can be passed from the view:

```python
def students(request):
    context = {
        "students": ["Aman", "Rahul", "Priya"]
    }

    return render(request, "myapp/students.html", context)
```

Template:

```html
<h1>Students</h1>

<ul>
{% for student in students %}
    <li>{{ student }}</li>
{% endfor %}
</ul>
```

---

## 13. Dynamic URLs

Django can capture values directly from a URL.

Example:

```python
path("student/<int:id>/", views.student_detail, name="student_detail")
```

The `<int:id>` part captures an integer.

View:

```python
def student_detail(request, id):
    return HttpResponse(f"Student ID: {id}")
```

URL:

```text
/student/10/
```

The view receives:

```python
id = 10
```

---

## 14. Common Path Converters

### `str`

```python
path("user/<str:username>/", views.user)
```

Captures a non-empty string excluding `/`.

### `int`

```python
path("student/<int:id>/", views.student_detail)
```

Captures an integer.

### `slug`

```python
path("post/<slug:slug>/", views.post)
```

Captures slug-style text such as:

```text
django-basics
```

### `uuid`

```python
path("item/<uuid:id>/", views.item)
```

Captures a UUID.

---

## 15. URL Names

Give URLs names so they can be referenced without hard-coding URL strings.

```python
path("about/", views.about, name="about")
```

The name is:

```text
about
```

---

## 16. URL Namespaces

For larger projects, use an app namespace.

In `myapp/urls.py`:

```python
app_name = "myapp"

urlpatterns = [
    path("", views.home, name="home"),
]
```

Then the URL name becomes:

```text
myapp:home
```

---

## 17. Using `{% url %}` in Templates

Instead of hard-coding:

```html
<a href="/about/">About</a>
```

use:

```html
<a href="{% url 'about' %}">About</a>
```

If using an app namespace:

```html
<a href="{% url 'myapp:home' %}">Home</a>
```

This makes URL changes easier to manage.

---

## 18. Passing Multiple Types of Data

A view can pass strings, numbers, lists, dictionaries, and other Python objects.

Example:

```python
def profile(request):
    context = {
        "name": "Alex",
        "age": 22,
        "skills": ["Python", "Django", "SQL"],
    }

    return render(request, "myapp/profile.html", context)
```

Template:

```html
<h1>{{ name }}</h1>
<p>Age: {{ age }}</p>

<h2>Skills</h2>

<ul>
{% for skill in skills %}
    <li>{{ skill }}</li>
{% endfor %}
</ul>
```

---

## 19. Template Comments

Django template comments can be written as:

```html
{# This is a template comment #}
```

For multi-line template comments:

```html
{% comment %}
This section is temporarily disabled.
{% endcomment %}
```

---

## 20. Recommended Day 4 Project Structure

After Day 4, your project can look like:

```text
django_project/
│
├── manage.py
│
├── django_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── myapp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    │
    └── templates/
        └── myapp/
            ├── home.html
            ├── about.html
            └── student.html
```

---

# Day 4 Practical Project

## Project: Student Information Pages

Create a small Django application with:

1. Home page
2. About page
3. Student list page
4. Dynamic student detail page

---

## Step 1 — Create App URLs

`myapp/urls.py`

```python
from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("students/", views.students, name="students"),
    path("students/<int:id>/", views.student_detail, name="student_detail"),
]
```

---

## Step 2 — Create Views

`myapp/views.py`

```python
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "myapp/home.html")


def about(request):
    return HttpResponse("About Django Student App")


def students(request):
    students_data = [
        {"id": 1, "name": "Aman"},
        {"id": 2, "name": "Rahul"},
        {"id": 3, "name": "Priya"},
    ]

    context = {
        "students": students_data
    }

    return render(request, "myapp/students.html", context)


def student_detail(request, id):
    context = {
        "student_id": id
    }

    return render(request, "myapp/student.html", context)
```

---

## Step 3 — Connect App URLs

Project `urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
]
```

---

## Step 4 — Create Home Template

`templates/myapp/home.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>

<h1>Student Information System</h1>

<a href="{% url 'myapp:about' %}">About</a>
<a href="{% url 'myapp:students' %}">Students</a>

</body>
</html>
```

---

## Step 5 — Create Students Template

`templates/myapp/students.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Students</title>
</head>
<body>

<h1>Students</h1>

<ul>
{% for student in students %}
    <li>
        <a href="{% url 'myapp:student_detail' student.id %}">
            {{ student.name }}
        </a>
    </li>
{% endfor %}
</ul>

<a href="{% url 'myapp:home' %}">Home</a>

</body>
</html>
```

---

## Step 6 — Create Student Detail Template

`templates/myapp/student.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Detail</title>
</head>
<body>

<h1>Student Detail</h1>

<p>Student ID: {{ student_id }}</p>

<a href="{% url 'myapp:students' %}">Back to Students</a>

</body>
</html>
```

---

# Day 4 Practice Tasks

## Task 1 — Basic Views

Create:

```text
/home/
/about/
/contact/
```

Each URL should have its own view.

---

## Task 2 — Template Rendering

Create a page:

```text
/profile/
```

Pass these values from the view:

```python
name
age
city
```

Display them in the template.

---

## Task 3 — Loop

Create a list of five courses:

```python
courses = [
    "Python",
    "Django",
    "SQL",
    "HTML",
    "CSS",
]
```

Display them using a Django template `for` loop.

---

## Task 4 — Dynamic URL

Create:

```text
/product/<int:id>/
```

Display the product ID received from the URL.

Example:

```text
/product/25/
```

Output:

```text
Product ID: 25
```

---

## Task 5 — URL Naming

Create named URLs for:

```text
home
about
products
```

Use `{% url %}` inside templates instead of hard-coded paths.

---

# Day 4 Key Concepts

| Concept | Meaning |
|---|---|
| URL | Maps a browser path to a view |
| `path()` | Defines a URL pattern |
| `include()` | Includes another URL configuration |
| View | Python function that handles a request |
| `HttpResponse` | Returns a direct HTTP response |
| `render()` | Renders a template and returns a response |
| Template | HTML presentation layer |
| Context | Data passed from view to template |
| `{{ }}` | Displays template variables |
| `{% %}` | Executes template tags |
| Dynamic URL | URL containing a captured value |
| Path converter | Defines the type of captured URL value |
| URL name | Identifier used to reference a URL |

---

# Day 4 Important Syntax

### URL

```python
path("about/", views.about, name="about")
```

### View

```python
def about(request):
    return render(request, "myapp/about.html")
```

### Context

```python
context = {
    "name": "Alex"
}
```

### Template variable

```html
{{ name }}
```

### Template condition

```html
{% if condition %}
{% endif %}
```

### Template loop

```html
{% for item in items %}
{% endfor %}
```

### Dynamic URL

```python
path("student/<int:id>/", views.student_detail)
```

### Named URL in template

```html
{% url 'myapp:home' %}
```

---

# Day 4 Checklist

- [ ] Understand Django request flow
- [ ] Understand project-level `urls.py`
- [ ] Create app-level `urls.py`
- [ ] Use `path()`
- [ ] Use `include()`
- [ ] Create function-based views
- [ ] Use `HttpResponse`
- [ ] Use `render()`
- [ ] Create template folders
- [ ] Create HTML templates
- [ ] Pass context from view to template
- [ ] Use template variables
- [ ] Use `{% if %}`
- [ ] Use `{% for %}`
- [ ] Create dynamic URLs
- [ ] Understand path converters
- [ ] Name URL patterns
- [ ] Use `{% url %}`
- [ ] Build the Student Information mini-project
- [ ] Complete all practice tasks

---

# Day 4 Completion Criteria

You can consider Day 4 complete when you can independently build this flow:

```text
URL
 ↓
View
 ↓
Context
 ↓
Template
 ↓
HTML Response
```

and can create a dynamic route such as:

```text
/students/10/
```

that reaches the correct view and displays the captured ID.

---

# Quick Revision

```text
urls.py       → URL routing
views.py      → Python request logic
templates/    → HTML presentation
context       → Data sent to templates
{{ variable }} → Display data
{% tag %}     → Template logic
render()      → View + Template → Response
path()        → Define URL route
include()     → Include app URLs
<int:id>      → Dynamic integer URL parameter
name="..."    → Give URL a reusable name
{% url ... %} → Generate URL from its name
```
