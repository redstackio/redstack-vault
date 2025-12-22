---
id: p2b3c4d5-e6f7-8901-bcde-f23456789012
tags:
  - django
  - database
  - setup
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/django-create-demo-environment]]'
  - '[[commands/django-create-seeded-users]]'
verified: false
platforms:
  - Linux
  - Docker
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:28.858Z'
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
# Create-Demo-Environment-and-Seeded-Users

## Summary

This procedure initializes a demo environment in the Django-based TalentMAP API and creates predefined seeded users to populate the database for vulnerability reproduction.

## Description

After setting up the Docker container, Django management commands are executed to create base configurations and test users. This simulates a populated user database, essential for demonstrating IDOR by providing multiple accounts to enumerate. The commands run inside the container to interact with the application's database.

## Requirements

1. Running TalentMAP API container
2. Access to the container shell (e.g., docker exec)
3. Django management scripts available

## Defense

Defensive measures and detection strategies:

- Restrict management command execution to admin roles
- Log database population activities
- Use database access controls to prevent unauthorized seeding

## Objectives

1. Set up initial demo configurations
2. Add seeded test users to the database
3. Verify data availability for testing

## Instructions

### Step 1: Create Demo Environment

**Context**: Run the command to initialize base demo data and configurations.

**Command** ([[commands/django-create-demo-environment]]):
```bash
python manage.py create_demo_environment
```

> This command sets up the demo environment, creating necessary tables and initial data. Expected output: "Demo environment created successfully".

### Step 2: Create Seeded Users

**Context**: Generate predefined test users for the database.

**Command** ([[commands/django-create-seeded-users]]):
```bash
python manage.py create_seeded_users
```

> Adds seeded accounts with known credentials. Expected output: "Seeded users created".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/django-create-demo-environment]]
- [[commands/django-create-seeded-users]]

## Tools Used


## Tags

- django
- database
- seeding
