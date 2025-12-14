---
id: p3c4d5e6-f7g8-9012-cdef-345678901234
name: Create-Management-Command-Structure
tags:
  - django
  - management
  - structure
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
updated_at: '2025-12-14T03:46:19.984Z'
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
# Create-Management-Command-Structure

## Summary

Establishes the directory hierarchy for custom Django management commands to host the POC script.

## Description

Django management commands require a specific structure under the app: management/commands/. This allows running the POC via python manage.py poc, simulating a backend process vulnerable to user-controlled filter dictionaries.

## Requirements

1. Existing 'webapp' directory
2. File system access for folder creation
3. Empty __init__.py files

## Defense

Defensive measures and detection strategies:

- Restrict custom command execution in production
- Audit management command directories for malicious code

## Objectives

1. Enable custom POC command
2. Organize code for easy execution
3. Simulate real app backend

## Instructions

### Step 1: Create Directories and Files

**Context**: Build the nested structure manually.

**Command** (Manual Creation):
No command; use mkdir and touch.

> Run: mkdir -p webapp/management/commands; touch webapp/management/__init__.py webapp/management/commands/__init__.py. Expected output: Structure ready for poc.py.

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
- management
- structure
