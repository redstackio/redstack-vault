---
tags:
  - ssti
  - verification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/jinja2-verify-class-name]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:37.023Z'
sub_techniques: []
id: 735ce39f-e943-42d4-b6aa-9d196f8ee226
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Verify-Popen-Class-at-Identified-Index

## Summary

This procedure confirms the subclass index corresponds to subprocess.Popen by injecting a Jinja2 expression to retrieve and render the class name.

## Description

Using the index from analysis, access the subclass array and call __name__ to output 'Popen' if correct. This low-risk step validates the gadget before full RCE, ensuring payload reliability in the MWAA Python context.

## Requirements

1. Known index from analysis (e.g., 292)
2. S3 and Airflow access

## Defense

Defensive measures and detection strategies:

- Block template access to __name__ or subclass attributes
- Monitor for iterative index testing in DAGs

## Objectives

1. Validate Popen accessibility
2. Confirm index accuracy
3. Proceed to RCE with confidence

## Instructions

### Step 1: Build Verification DAG

**Context**: Insert index-specific payload.

**Command** ([[commands/jinja2-verify-class-name]]):
```python
doc_md = "{{ ''.__class__.__mro__[1].__subclasses__()[292].__name__ }}"
```

> Adjust [292] as needed; save as test_3.py.

### Step 2: Deploy and Check

**Context**: Render to confirm name.

**Command** (Upload):
```bash
aws s3 cp test_3.py s3://your-mwaa-dags-bucket/
```

> Trigger and view UI doc_md.

### Step 3: Adjust if Needed

**Context**: If not 'Popen', increment/decrement index and retest.

Repeat upload with updated index.

> Success: 'Popen' displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques

-

## Commands Used

- [[commands/jinja2-verify-class-name]]

## Tools Used

-

## Tags

- [[verification]]
