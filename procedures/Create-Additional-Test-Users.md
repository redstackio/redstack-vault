---
id: p3c4d5e6-f7g8-9012-cdef-345678901234
tags:
  - django
  - user-creation
  - test-data
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/django-create-user]]'
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:28.854Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Create-Additional-Test-Users

## Summary

This procedure adds specific test user accounts to the TalentMAP database using Django's create_user command, expanding the dataset for IDOR enumeration testing.

## Description

To thoroughly test the IDOR, additional users with distinct identifiers are created. Each command specifies username, email, password, and full name, allowing verification of data leakage by targeting their IDs. This is run inside the Docker container to maintain isolation.

## Requirements

1. Active Django application in container
2. Container shell access
3. Known password policy compliance

## Defense

Defensive measures and detection strategies:

- Audit user creation logs for anomalies
- Enforce CAPTCHA or admin approval for new accounts
- Monitor for bulk user additions in test environments

## Objectives

1. Insert multiple test users with traceable details
2. Ensure sequential ID assignment
3. Prepare targets for unauthorized access

## Instructions

### Step 1: Create First Test User

**Context**: Add a normal user account for basic testing.

**Command** ([[commands/django-create-user]]):
```bash
python manage.py create_user normalUser normaluser@gmail.com normalUser123 Normal User
```

> Creates user with specified params. Expected output: "User created successfully".

### Step 2: Create Second Test User

**Context**: Add another user to increase enumeration scope.

**Command** ([[commands/django-create-user]]):
```bash
python manage.py create_user normalUser1 normaluser1@gmail.com normalUser123 Normal User
```

> Similar to Step 1. Expected output: "User created successfully".

### Step 3: Create Third Test User

**Context**: Final addition for comprehensive testing.

**Command** ([[commands/django-create-user]]):
```bash
python manage.py create_user normalUser2 normaluser2@gmail.com normalUser123 Normal User
```

> Completes the set. Expected output: "User created successfully".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/django-create-user]]

## Tools Used


## Tags

- django
- user-creation
- test-data
