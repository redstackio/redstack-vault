---
id: t1i2j3k4-l5m6-7892-ijkl-012345678901
url: 'https://docs.djangoproject.com/en/stable/ref/django-admin/'
name: django-admin
tags:
  - django
  - admin
type: tool
verified: false
platforms:
  - Python
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:19.944Z'
validated: true
submitted: true
---
# django-admin

**Status**: Unverified

## Overview

Command-line utility for administrative tasks in Django, such as starting projects and running checks.

## Description

django-admin is Django's primary CLI tool for project initialization and management, essential for setting up environments to test vulnerabilities like SQL injection in ORM components.

## Features

- Feature 1: Project creation with startproject
- Feature 2: System checks with check
- Feature 3: Extension via custom commands

## Installation

### Requirements

- Python 3.x
- Django installed (pip install django)

### Install Commands

```bash
# Already available post-Django install
pip install django
```

## Basic Usage

```bash
django-admin --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| --version | Display version |

## Examples

### Example 1: Basic Usage

```bash
django-admin startproject mysite
```

### Example 2: Advanced Usage

```bash
django-admin check --deploy
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for django-admin executions
- Log reviews in development pipelines

## Related Procedures

- [[procedures/Set-Up-Django-Project-and-App]]

## Related Tools

- [[tools/manage-py]]

## References

- Official documentation: https://docs.djangoproject.com/en/stable/ref/django-admin/
