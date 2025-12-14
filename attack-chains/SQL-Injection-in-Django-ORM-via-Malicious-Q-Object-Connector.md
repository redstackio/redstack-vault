---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: SQL Injection in Django ORM via Malicious Q Object Connector
tags:
  - sqli
  - django
  - orm
  - q-objects
  - python
  - web
  - database
type: attack_chain
tools:
  - '[[tools/django-admin]]'
  - '[[tools/manage-py]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Python
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-Django-Project-and-App]]'
  - '[[procedures/Configure-App-in-Settings]]'
  - '[[procedures/Create-Management-Command-Structure]]'
  - '[[procedures/Implement-Vulnerable-POC-Code]]'
  - '[[procedures/Define-User-Model]]'
  - '[[procedures/Run-Migrations-and-Execute-POC]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.002Z'
description: >-
  Demonstrates exploitation of a SQL injection vulnerability in Django's ORM
  WhereNode.as_sql method by injecting arbitrary SQL through the unvalidated
  '_connector' attribute in Q objects, leading to filter bypass and data
  exfiltration.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection in Django ORM via Malicious Q Object Connector

Multi-stage attack chain demonstrating reproduction of a critical SQL injection vulnerability in Django ORM's WhereNode.as_sql method, exploited via malicious '_connector' in Q objects to bypass filters and exfiltrate data.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Project] --> B[Configure App]
    B --> C[Create Structure]
    C --> D[Implement POC]
    D --> E[Define Model]
    E --> F[Run Migrations and Exploit]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/django-admin]]
- [[tools/manage-py]]

### Target Environment

- Python 3.x with Django installed
- Database (e.g., SQLite for POC)
- Local development environment

### Initial Access Requirements

- Local machine with Python and Django
- No network access needed for POC reproduction
- Administrative privileges on local system for setup

## Detailed Attack Procedures

### Step 1: Set Up Django Project and App
procedure: [[procedures/Set-Up-Django-Project-and-App]]

**Objective**: Initialize a new Django project and app to simulate the vulnerable environment.

**Instructions**: Use [[commands/django-admin-startproject]] to create the project, then [[commands/python-manage-py-startapp]] to add the app.

```bash
django-admin startproject sqli .
python manage.py startapp webapp
```

**Expected Output**: Project files generated, including manage.py and webapp directory with models.py.

**Success Indicators**:
- Project directory 'sqli' created
- App 'webapp' directory exists

### Step 2: Configure App in Settings
procedure: [[procedures/Configure-App-in-Settings]]

**Objective**: Register the app in Django settings to enable model usage.

**Instructions**: Edit sqli/settings.py to add 'webapp' to INSTALLED_APPS.

**Expected Output**: Settings file updated with 'webapp' in the list.

**Success Indicators**:
- No syntax errors on import
- App recognized by Django

### Step 3: Create Management Command Structure
procedure: [[procedures/Create-Management-Command-Structure]]

**Objective**: Set up directories for a custom management command to run the POC.

**Instructions**: Create 'management' and 'commands' folders inside webapp, with empty __init__.py files in each.

**Expected Output**: Directory structure: webapp/management/commands/__init__.py.

**Success Indicators**:
- Folders and files created without errors
- Ready for POC script placement

### Step 4: Implement Vulnerable POC Code
procedure: [[procedures/Implement-Vulnerable-POC-Code]]

**Objective**: Write code simulating the vulnerable Q object unpacking with malicious '_connector'.

**Instructions**: Create poc.py in webapp/management/commands, defining a command that creates sample users, uses Q(**search_dict) with payload {'is_admin': False, 'username': 'nonexistent_user', '_connector': ') OR 1=1 OR ('}, filters User.objects.filter(query), and prints SQL and results.

**Expected Output**: POC script ready, demonstrating injection on execution.

**Success Indicators**:
- Script parses without errors
- Malicious payload integrated

### Step 5: Define User Model
procedure: [[procedures/Define-User-Model]]

**Objective**: Create a simple User model for testing the injection.

**Instructions**: In webapp/models.py, define class User with username=CharField and is_admin=BooleanField.

**Expected Output**: Model defined, ready for migration.

**Success Indicators**:
- Model syntax valid
- Fields match POC needs

### Step 6: Run Migrations and Execute POC
procedure: [[procedures/Run-Migrations-and-Execute-POC]]

**Objective**: Apply schema changes and run the exploit to bypass filters and exfiltrate data.

**Instructions**: Execute [[commands/python-manage-py-makemigrations]], [[commands/python-manage-py-migrate]], then [[commands/python-manage-py-poc]].

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py poc
```

**Expected Output**: Tables created; SQL like SELECT ... WHERE (NOT "webapp_user"."is_admin" ) OR 1=1 OR ( "webapp_user"."username" = 'nonexistent_user'); all users returned including admin; 'SUCCESS: The filter was bypassed' printed.

**Success Indicators**:
- All users exfiltrated despite filter
- Injected SQL visible in output

## Attack Chain Summary

### Key Achievements

1. Reproduced SQL injection via unvalidated '_connector' in Q objects
2. Bypassed access controls to retrieve all records
3. Demonstrated potential for full data exfiltration and DoS

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
