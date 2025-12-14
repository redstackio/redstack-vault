---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Set-Up-Django-Project-and-App
tags:
  - django
  - setup
  - python
type: procedure
tools:
  - '[[tools/django-admin]]'
  - '[[tools/manage-py]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/django-admin-startproject]]'
  - '[[commands/python-manage-py-startapp]]'
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.992Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Set-Up-Django-Project-and-App

## Summary

This procedure initializes a new Django project and application to create a controlled environment for reproducing the SQL injection vulnerability in the ORM.

## Description

In a Django-based web application, the vulnerability arises from unvalidated user input unpacked into Q objects. To demonstrate, start by setting up a minimal project structure. This step ensures a clean slate for model definition and custom command execution, simulating a real application where filter dictionaries are user-controlled.

## Requirements

1. Python 3.x installed with Django (pip install django)
2. Local directory for project creation
3. Command-line access

## Defense

Defensive measures and detection strategies:

- Use virtual environments to isolate project dependencies
- Scan for outdated Django versions vulnerable to this issue

## Objectives

1. Establish project foundation for vulnerability reproduction
2. Prepare app for model and command integration
3. Enable subsequent migration and execution steps

## Instructions

### Step 1: Create Django Project

**Context**: Generates the base project files including manage.py and settings.py.

**Command** ([[commands/django-admin-startproject]]):
```bash
django-admin startproject sqli .
```

> Creates a project named 'sqli' in the current directory. Expected output: Directory structure with sqli/ containing settings.py, urls.py, etc., and manage.py at root.

### Step 2: Create Django App

**Context**: Adds an app directory for custom models and commands.

**Command** ([[commands/python-manage-py-startapp]]):
```bash
python manage.py startapp webapp
```

> Creates 'webapp' app with files like models.py. Expected output: webapp/ directory with __init__.py, admin.py, models.py, etc.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/django-admin-startproject]]
- [[commands/python-manage-py-startapp]]

## Tools Used

- [[tools/django-admin]]
- [[tools/manage-py]]

## Tags

- django
- setup
- python
