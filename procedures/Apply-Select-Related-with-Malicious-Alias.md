---
tags:
  - sqli
  - django
  - select_related
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
updated_at: '2025-12-14T03:15:05.068Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: f8864ab4-5005-4472-be91-909ec04668cb
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Apply-Select-Related-with-Malicious-Alias

## Summary

This procedure chains select_related() with the malicious alias to reference the injected alias, ensuring the malformed SQL is included in the final query.

## Description

By calling select_related on the dynamic alias, the ORM incorporates the injected string into the FROM/JOIN sections, finalizing the SQLi setup. This step is crucial for triggering the injection during execution in vulnerable Django apps.

## Requirements

1. Annotated queryset from previous step
2. Malicious alias variable
3. Django ORM environment

## Defense

Defensive measures and detection strategies:

- Validate select_related arguments against allowlist
- Log and inspect dynamic select_related calls
- Use ORM prefetch alternatives to avoid dynamic relations

## Objectives

1. Reference injected alias in query chain
2. Build complete malformed SQL
3. Set up for execution

## Instructions

### Step 1: Chain Select Related

**Context**: Apply select_related using the payload variable to the queryset.

**Command** (Python code):
```python
qs = qs.select_related(user_data)
```

> This chains the method, embedding the payload. Expected output: Updated queryset; inspect .query to see full injection in SQL.

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
- select_related
