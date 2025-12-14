---
id: c2e3f4g5-h6i7-8902-def0-123456789012
data: python manage.py startapp webapp
tags:
  - django
  - app
type: command
output: 'Generates app directory with models.py, views.py, etc.'
executor: bash
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.951Z'
verified: false
validated: true
submitted: true
---
# python-manage-py-startapp

## Command

```bash
python manage.py startapp webapp
```

## Description

Creates a new Django app named 'webapp' within the project, providing boilerplate files for models and commands.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| webapp | App name | Yes |

## Examples

### Basic Usage

```bash
python manage.py startapp myapp
```

### Advanced Usage

```bash
python manage.py startapp --template=/path webapp
```

## Expected Output

'webapp' directory with __init__.py, admin.py, apps.py, models.py, tests.py, views.py.

## Related

- [[commands/django-admin-startproject]]
- [[procedures/Set-Up-Django-Project-and-App]]
