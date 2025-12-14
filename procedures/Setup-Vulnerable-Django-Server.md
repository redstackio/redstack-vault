---
tags:
  - setup
  - django
  - windows
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.794Z'
sub_techniques: []
id: ba772ad7-45d8-41be-9b8e-ea5f868b0a54
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Vulnerable-Django-Server

## Summary

This procedure sets up a local Django web server on Windows using vulnerable versions to demonstrate the UsernameField DoS vulnerability.

## Description

The attack targets Django's slow NFKC normalization in UsernameField on Windows. Start by installing a vulnerable Django version (before 4.2.7, 4.1.13, or 3.2.23) and enabling the admin interface. This creates an environment where large Unicode inputs cause resource exhaustion during validation.

## Requirements

1. Windows operating system
2. Python 3.x installed
3. Access to pip for package installation
4. Basic Django project setup knowledge

## Defense

Defensive measures and detection strategies:

- Upgrade to Django 4.2.7, 4.1.13, or 3.2.23 or later
- Implement input length limits before normalization
- Monitor for unusual CPU spikes on login endpoints

## Objectives

1. Establish a testable vulnerable Django instance
2. Expose the admin login for payload targeting
3. Verify normal functionality before exploitation

## Instructions

### Step 1: Install Vulnerable Django

**Context**: Create a new Django project with a vulnerable version.

Install Django via pip:

```bash
pip install "Django<4.2.7"
```

> This installs a version affected by the normalization issue. Expected output: Django package installed successfully.

### Step 2: Create and Configure Project

**Context**: Set up the project and enable admin.

Create project and add admin to settings:

```bash
django-admin startproject mysite
cd mysite
python manage.py startapp myapp
```

Edit settings.py to include 'django.contrib.admin' in INSTALLED_APPS, then migrate and runserver:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

> Server runs on http://127.0.0.1:8000/. Expected output: Admin site accessible at /admin/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- setup
- django
- windows
