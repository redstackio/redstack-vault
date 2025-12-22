---
id: c4g5h6i7-j8k9-0124-fg12-345678901234
data: python manage.py migrate
tags:
  - django
  - migrations
type: command
output: Creates tables including webapp_user
executor: bash
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.948Z'
verified: false
validated: true
submitted: true
---
# python-manage-py-migrate

## Command

```bash
python manage.py migrate
```

## Description

Applies pending migrations to the database, creating or altering tables as needed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Applies all | No |

## Examples

### Basic Usage

```bash
python manage.py migrate
```

### Advanced Usage

```bash
python manage.py migrate webapp 0001
```

## Expected Output

'Applying webapp.0001_initial... OK' and database tables created.

## Related

- [[commands/python-manage-py-makemigrations]]
- [[procedures/Run-Migrations-and-Execute-POC]]
