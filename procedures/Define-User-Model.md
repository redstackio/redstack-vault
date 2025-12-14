---
id: p5e6f7g8-h9i0-1234-efgh-567890123456
name: Define-User-Model
tags:
  - django
  - model
  - user
type: procedure
tools:
  - '[[tools/manage-py]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Python
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.968Z'
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
# Define-User-Model

## Summary

Creates a basic User model to serve as the target for the SQL injection exploitation.

## Description

The model includes fields relevant to the filter bypass demo: username and is_admin. This allows testing the Q filter on a realistic dataset, where the injection returns all users despite the 'is_admin=False' condition.

## Requirements

1. Django app directory with models.py
2. Basic Django model knowledge
3. Text editor

## Defense

Defensive measures and detection strategies:

- Implement model-level access controls
- Validate model fields against injection patterns

## Objectives

1. Provide data structure for POC
2. Enable user creation and filtering
3. Support migration to database

## Instructions

### Step 1: Add Model to models.py

**Context**: Define the class with fields.

**Command** (Manual Edit):
No command; edit webapp/models.py.

> from django.db import models; class User(models.Model): username = models.CharField(max_length=100); is_admin = models.BooleanField(default=False). Expected output: Model defined without syntax errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/manage-py]]

## Tags

- django
- model
- user
