---
id: c1d2e3f4-g5h6-7891-cdef-890123456789
data: python manage.py create_demo_environment
tags:
  - django
  - setup
type: command
output: Demo environment created successfully
executor: bash
platforms:
  - Linux
  - Docker
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:28.826Z'
verified: false
validated: true
submitted: true
---
# django-create-demo-environment

## Command

```bash
python manage.py create_demo_environment
```

## Description

Executes the Django management command to initialize a demo environment in the TalentMAP API, setting up initial configurations and base data in the database.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| manage.py | Django management script | Yes |
| create_demo_environment | Command to create demo setup | Yes |

## Examples

### Basic Usage

```bash
python manage.py create_demo_environment
```

### Advanced Usage

No additional options; run as-is inside the container.

## Expected Output

"Demo environment created successfully" or similar confirmation, with database updated.

## Related

- [[commands/django-create-seeded-users]]
- [[procedures/Create-Demo-Environment-and-Seeded-Users]]
