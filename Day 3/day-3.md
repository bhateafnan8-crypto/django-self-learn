# Django Day 3 — Models & Database

## 📚 Concepts

- [ ] Django Models
- [ ] Model ↔ Database relationship
- [ ] Model fields
- [ ] Primary Key & default `id`
- [ ] `CharField`
- [ ] `TextField`
- [ ] `IntegerField`
- [ ] `FloatField`
- [ ] `BooleanField`
- [ ] `EmailField`
- [ ] `DateField`
- [ ] `makemigrations`
- [ ] `migrate`
- [ ] `null`
- [ ] `blank`

---

## 1. Django Models

A **Model** is a Python class used to define the structure of data in a Django application.

Example:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

Django uses the model definition to create and manage database tables.

### Easy definition

> **Model = Database Table**

---

## 2. Model ↔ Database Relationship

Django ORM connects Python models with database tables.

| Django | Database |
|---|---|
| Model | Table |
| Field | Column |
| Object / Instance | Record / Row |
| Model attribute | Column value |

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

This represents a database table similar to:

```text
Student
--------------------------------
id | name       | age
--------------------------------
1  | Rahul      | 21
2  | Priya      | 22
```

---

## 3. Model Fields

Fields define what type of data a model stores.

Example:

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    available = models.BooleanField()
```

### Easy definition

> **Field = Database Column**

---

## 4. Primary Key & Default `id`

A **primary key** uniquely identifies each record in a table.

If you do not define a primary key, Django automatically creates an `id` field as the primary key.

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
```

Conceptually, Django creates:

```text
id | name
---|------
1  | Rahul
2  | Priya
```

### Important

> Django automatically provides an `id` primary key unless you define one yourself.

---

## 5. `CharField`

`CharField` is used for **short text**.

```python
name = models.CharField(max_length=100)
```

`max_length` defines the maximum length of the text.

### Example

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
```

---

## 6. `TextField`

`TextField` is used for **long text**.

```python
description = models.TextField()
```

### Example

```python
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
```

### Difference

- `CharField` → short text
- `TextField` → long text

---

## 7. `IntegerField`

`IntegerField` stores **whole numbers**.

```python
age = models.IntegerField()
```

Examples:

```text
10
25
100
-5
```

---

## 8. `FloatField`

`FloatField` stores **floating-point numbers**.

```python
price = models.FloatField()
```

Examples:

```text
10.5
99.99
3.14
```

---

## 9. `BooleanField`

`BooleanField` stores either `True` or `False`.

```python
is_active = models.BooleanField()
```

Example:

```python
class User(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField()
```

---

## 10. `EmailField`

`EmailField` is used for storing email addresses.

```python
email = models.EmailField()
```

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

It provides email-oriented validation when used through Django forms/model validation.

---

## 11. `DateField`

`DateField` stores dates.

```python
birth_date = models.DateField()
```

Example:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
```

A date can look like:

```text
2026-09-19
```

---

# 🔧 Database Migrations

Migrations are Django's way of tracking changes to database structure.

Typical workflow:

```text
Create / modify Model
        ↓
python manage.py makemigrations
        ↓
Migration file created
        ↓
python manage.py migrate
        ↓
Changes applied to database
```

---

## 12. `makemigrations`

`makemigrations` creates migration files based on changes made to models.

Command:

```bash
python manage.py makemigrations
```

### Easy definition

> **makemigrations = Create migration files**

It does **not** directly apply the changes to the database.

---

## 13. `migrate`

`migrate` applies migration files to the database.

Command:

```bash
python manage.py migrate
```

### Easy definition

> **migrate = Apply migrations to the database**

---

## 14. `null`

`null` controls whether the database column can store SQL `NULL`.

Example:

```python
age = models.IntegerField(null=True)
```

This allows the database value to be `NULL`.

### Easy definition

> **null = Database-level NULL**

---

## 15. `blank`

`blank` controls whether a field is allowed to be empty during validation, especially in forms.

Example:

```python
description = models.TextField(blank=True)
```

### Easy definition

> **blank = Validation/form-level empty value**

---

## ⭐ `null` vs `blank`

| Option | Meaning |
|---|---|
| `null=True` | Database can store `NULL` |
| `blank=True` | Validation can allow an empty value |

They solve different problems.

---

# 🧠 Quick Revision

- **Model** → Database table
- **Field** → Database column
- **Object / Instance** → Database record
- **Primary Key** → Uniquely identifies a record
- **Default `id`** → Django automatically creates it when no primary key is defined
- **CharField** → Short text
- **TextField** → Long text
- **IntegerField** → Whole numbers
- **FloatField** → Floating-point numbers
- **BooleanField** → `True` / `False`
- **EmailField** → Email values
- **DateField** → Dates
- **makemigrations** → Creates migration files
- **migrate** → Applies migrations
- **null** → Database-level `NULL`
- **blank** → Validation/form-level empty value

---

# 📝 Basic Practice Model

Create a model containing different field types:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    age = models.IntegerField()
    percentage = models.FloatField()
    is_active = models.BooleanField()
    email = models.EmailField()
    birth_date = models.DateField()
```

Then run:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# ✅ Day 3 Completion Checklist

- [ ] Django Models
- [ ] Model ↔ Database relationship
- [ ] Model fields
- [ ] Primary Key & default `id`
- [ ] `CharField`
- [ ] `TextField`
- [ ] `IntegerField`
- [ ] `FloatField`
- [ ] `BooleanField`
- [ ] `EmailField`
- [ ] `DateField`
- [ ] `makemigrations`
- [ ] `migrate`
- [ ] `null`
- [ ] `blank`
- [ ] Practice model created
- [ ] Migrations created
- [ ] Migrations applied
