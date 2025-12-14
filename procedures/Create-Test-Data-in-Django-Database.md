---
tags:
  - django
  - orm
  - setup
  - database
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.777Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: fae32907-16e0-4f9d-bb77-6d3737be356f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Data-in-Django-Database

## Summary

This procedure sets up test data in a Django model using NullableJSONField to prepare for demonstrating SQL injection in JSON lookups.

## Description

In a Django application, create instances of a model like NullableJSONModel with JSON data in the value_custom field. This simulates a real-world scenario where user data is stored in JSONFields and queried dynamically. The setup ensures the database has non-null JSON values for subsequent lookup tests. Prerequisites include a running Django project with a JSONField model and a database backend supporting JSON (e.g., PostgreSQL).

## Requirements

1. Django project with models.py defining NullableJSONField (e.g., class NullableJSONModel(models.Model): value_custom = models.JSONField(null=True))
2. Database migrations applied (python manage.py makemigrations && python manage.py migrate)
3. Django shell access (python manage.py shell)

## Defense

Defensive measures and detection strategies:

- Use database auditing to monitor INSERT operations on sensitive models
- Enforce model validation to restrict JSON content

## Objectives

1. Populate database with sample JSON data for testing
2. Verify data integrity before injection tests
3. Establish baseline for query behavior

## Instructions

### Step 1: Access Django Shell

**Context**: Launch the Django shell to interact with the ORM.

**Command** (Django Shell):
```bash
python manage.py shell
```

> Opens an interactive Python shell with Django models loaded.

### Step 2: Create JSON Records

**Context**: Use ORM to insert two sample records with JSON data.

**Command** (Python in Shell):
```python
from myapp.models import NullableJSONModel

NullableJSONModel.objects.create(value_custom={'a': 'b'})
NullableJSONModel.objects.create(value_custom={'b': 'c'})
```

> Inserts records; expected output is the created model instances with IDs.

### Step 3: Verify Insertion

**Context**: Query the model to confirm data is present.

**Command** (Python in Shell):
```python
NullableJSONModel.objects.filter(value_custom__isnull=False).count()
```

> Returns 2, indicating successful setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- django
- orm
- setup
