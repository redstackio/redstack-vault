---
tags:
  - sqli
  - django
  - annotate
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Python
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.072Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6621b208-a3c8-4bc8-b430-8515f29d70ff
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Annotate-Queryset-with-Malicious-FilteredRelation

## Summary

This procedure injects the malicious alias into a Django queryset's annotate() method using FilteredRelation, embedding the payload in the SQL JOIN alias generation.

## Description

Django's annotate() with dynamic keys from user input allows the payload to be inserted directly into the SQL query builder. The unescaped quote causes the JOIN alias to be malformed, setting up the injection. This targets apps where aliases are built dynamically, leading to SQLi in the JOIN clause.

## Requirements

1. Django model with relations (e.g., Book with author ForeignKey)
2. Malicious alias variable prepared
3. ORM query context

## Defense

Defensive measures and detection strategies:

- Avoid dynamic aliases in annotate(); use static names
- Quote and escape alias strings manually if dynamic
- Audit ORM queries for user-controlled annotations

## Objectives

1. Insert payload into SQL via FilteredRelation
2. Malform the JOIN clause
3. Prepare for query chaining

## Instructions

### Step 1: Import and Annotate

**Context**: Import FilteredRelation and apply annotate with the dynamic malicious key.

**Command** (Python code):
```python
from django.db.models import FilteredRelation
qs = Book.objects.annotate(**{user_data: FilteredRelation('author')})
```

> This builds the queryset, inserting the payload as the alias. Expected output: Queryset object; check .query for injected SQL snippet.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sqli
- django
- annotate
