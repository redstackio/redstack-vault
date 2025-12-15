---
id: c2e3f4g5-h6i7-8902-defg-901234567890
data: python manage.py create_seeded_users
tags:
  - django
  - users
type: command
output: Seeded users created
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:28.813Z'
verified: false
validated: true
submitted: true
---
# django-create-seeded-users

## Command

```bash
python manage.py create_seeded_users
```

## Description

Runs the Django command to generate predefined seeded test users in the database for testing purposes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| manage.py | Django management script | Yes |
| create_seeded_users | Command for seeded accounts | Yes |

## Examples

### Basic Usage

```bash
python manage.py create_seeded_users
```

### Advanced Usage

No params needed.

## Expected Output

"Seeded users created" confirmation.

## Related

- [[commands/django-create-demo-environment]]
- [[procedures/Create-Demo-Environment-and-Seeded-Users]]
