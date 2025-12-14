---
id: c3f4g5h6-i7j8-9013-efgh-012345678901
data: 'python manage.py create_user {username} {email} {password} {full_name}'
tags:
  - django
  - user-creation
type: command
output: User created successfully
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:28.811Z'
verified: false
validated: true
submitted: true
---
# django-create-user

## Command

```bash
python manage.py create_user {username} {email} {password} {full_name}
```

## Description

Django management command to create a new user account with specified username, email, password, and full name.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| username | User login name | Yes |
| email | Email address | Yes |
| password | Account password | Yes |
| full_name | Display name | Yes |

## Examples

### Basic Usage

```bash
python manage.py create_user normalUser normaluser@gmail.com normalUser123 Normal User
```

### Advanced Usage

```bash
python manage.py create_user normalUser1 normaluser1@gmail.com normalUser123 Normal User
```

## Expected Output

"User created successfully" for each execution.

## Related

- [[commands/django-create-seeded-users]]
- [[procedures/Create-Additional-Test-Users]]
