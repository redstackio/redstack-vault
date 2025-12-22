---
id: c1d2e3f4-g5h6-7891-cdef-012345678901
data: django-admin startproject sqli .
tags:
  - django
  - setup
type: command
output: Generates project files including manage.py and settings.py
executor: bash
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.953Z'
verified: false
validated: true
submitted: true
---
# django-admin-startproject

## Command

```bash
django-admin startproject sqli .
```

## Description

Creates a new Django project named 'sqli' in the current directory, setting up the initial structure for development and POC reproduction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sqli | Project name | Yes |
| . | Target directory (current) | Yes |

## Examples

### Basic Usage

```bash
django-admin startproject mysite .
```

### Advanced Usage

```bash
django-admin startproject --template=/path/to/template sqli .
```

## Expected Output

Directory 'sqli' with manage.py, sqli/ folder containing __init__.py, settings.py, urls.py, wsgi.py.

## Related

- [[commands/python-manage-py-startapp]]
- [[procedures/Set-Up-Django-Project-and-App]]
