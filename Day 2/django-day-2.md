# Django Day 2 Roadmap

## 🎯 Day 2 Goal

Understand Django's project/app structure and learn the basic request flow:

**URL → View → Template → Response**

---

## 📚 Concepts

### Django Project Structure
- [ ] `manage.py`
- [ ] Project package
- [ ] `settings.py`
- [ ] `urls.py`
- [ ] `asgi.py`
- [ ] `wsgi.py`

### Django Apps
- [ ] What is a Django app?
- [ ] Project vs App
- [ ] Create an app
- [ ] App structure
- [ ] `views.py`
- [ ] `models.py`
- [ ] `admin.py`
- [ ] `apps.py`
- [ ] `tests.py`
- [ ] `migrations/`
- [ ] Register app in `INSTALLED_APPS`

### URL Routing
- [ ] `urls.py`
- [ ] `path()`
- [ ] URL patterns
- [ ] URL parameters
- [ ] Dynamic URLs
- [ ] `include()`

### Django Views
- [ ] What is a view?
- [ ] Function-based views
- [ ] `request`
- [ ] `HttpResponse`
- [ ] `render()`

### Templates
- [ ] What is a template?
- [ ] Templates directory
- [ ] HTML templates
- [ ] Template variables
- [ ] Context
- [ ] Template tags
- [ ] Template inheritance
- [ ] `{% extends %}`
- [ ] `{% block %}`

### Static Files
- [ ] Static files concept
- [ ] `static/` directory
- [ ] CSS
- [ ] JavaScript
- [ ] Images
- [ ] `STATIC_URL`
- [ ] `{% load static %}`

---

## 🔄 Core Django Request Flow

```text
Browser
   ↓
HTTP Request
   ↓
urls.py
   ↓
View
   ↓
Template
   ↓
HTTP Response
   ↓
Browser
```

### Must Understand

**Request → URL → View → Template → Response**

---

## 🛠️ Practical Tasks

- [ ] Create a Django project
- [ ] Create a Django app
- [ ] Register the app
- [ ] Create a home page
- [ ] Create an about page
- [ ] Create a contact page
- [ ] Create a product page
- [ ] Connect URLs to views
- [ ] Return `HttpResponse`
- [ ] Render HTML templates
- [ ] Pass data from view to template
- [ ] Create a dynamic URL
- [ ] Use `include()`
- [ ] Create `base.html`
- [ ] Use template inheritance
- [ ] Add CSS using static files

---

## 💻 Commands to Practice

```bash
django-admin startproject project_name
```

```bash
python manage.py startapp app_name
```

```bash
python manage.py runserver
```

---

## 🧪 Mini Project

### Multi-Page Django Website

Build a simple website containing:

- [ ] Home page
- [ ] About page
- [ ] Contact page
- [ ] Product detail page
- [ ] Navigation menu
- [ ] Shared base template
- [ ] CSS styling
- [ ] Dynamic product URL

---

## 🧠 Problem Solving

Try to complete these without copying:

- [ ] Create 4 different URLs
- [ ] Create 4 different views
- [ ] Connect each URL to its view
- [ ] Render a template from a view
- [ ] Pass dynamic data to a template
- [ ] Create a dynamic product URL using an ID
- [ ] Create and use `base.html`
- [ ] Add a static CSS file
- [ ] Debug URL/view/template errors

---

# ✅ Day 2 Completion Checklist

- [ ] Django project structure
- [ ] Django app structure
- [ ] Project vs App
- [ ] Create and register an app
- [ ] URL routing
- [ ] `path()`
- [ ] `include()`
- [ ] Function-based views
- [ ] `request`
- [ ] `HttpResponse`
- [ ] Templates
- [ ] `render()`
- [ ] Context / template variables
- [ ] Dynamic URL parameters
- [ ] Template inheritance
- [ ] Static files
- [ ] Request → URL → View → Template → Response
- [ ] Complete mini project
- [ ] Complete problem-solving tasks

---

## 🏁 Day 2 Outcome

By the end of Day 2, you should be able to:

> Build a basic multi-page Django website and understand how a browser request moves through Django and becomes a response.

### Core Flow

**Browser → URL → View → Template → Response**
