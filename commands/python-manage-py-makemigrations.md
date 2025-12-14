---
id: c3f4g5h6-i7j8-9013-ef01-234567890123
data: python manage.py makemigrations
tags:
  - django
  - migrations
type: command
output: Detects User model and generates migration script
executor: bash
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.950Z'
verified: false
validated: true
submitted: true
---
# python-manage-py-makemigrations

## Command

```bash
python manage.py makemigrations
```

## Description

Detects changes in models and generates migration files to track database schema updates.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Default behavior | No |

## Examples

### Basic Usage

```bash
python manage.py makemigrations
```

### Advanced Usage

```bash
python manage.py makemigrations webapp
```

## Expected Output

'Migrations for 'webapp': webapp/migrations/0001_initial.py - Create model User'.

## Related

- [[commands/python-manage-py-migrate]]
- [[procedures/Run-Migrations-and-Execute-POC]]
