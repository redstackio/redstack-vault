---
tags:
  - ssti
  - gadget-chain
  - python
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/jinja2-enumerate-subclasses]]'
verified: false
platforms:
  - AWS
  - Cloud
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Python]]'
updated_at: '2025-12-14T17:23:37.039Z'
sub_techniques: []
id: 926a0c14-9473-4e26-b96c-54cfe70d9260
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
---
# Enumerate-Subclasses-for-Gadget-Chain-Discovery

## Summary

This procedure exploits confirmed SSTI to enumerate all subclasses of the object type in the Python runtime, revealing available gadgets like subprocess.Popen for building an RCE chain.

## Description

Following SSTI confirmation, inject a Jinja2 expression that traverses the Python class hierarchy via __mro__ and __subclasses__() to list loaded classes. This output, rendered in Airflow UI, allows identification of exploitable modules in the MWAA worker's Python environment (Airflow 2.9.2).

## Requirements

1. Confirmed SSTI from prior procedure
2. S3 write access and Airflow UI
3. Text editor for output analysis

## Defense

Defensive measures and detection strategies:

- Restrict template access to safe expressions only
- Log and alert on __class__ or __subclasses__ accesses in template evals
- Use MWAA execution roles with least privilege to limit RCE impact

## Objectives

1. List runtime subclasses
2. Locate RCE-enabling classes
3. Prepare for index-based exploitation

## Instructions

### Step 1: Create Enumeration DAG

**Context**: Embed subclass enumeration in doc_md.

**Command** ([[commands/jinja2-enumerate-subclasses]]):
```python
doc_md = "{{ ''.__class__.__mro__[1].__subclasses__() }}"
```

> Save as test_2.py with basic DAG structure.

### Step 2: Upload and Execute

**Context**: Trigger rendering to capture output.

**Command** (S3 upload):
```bash
aws s3 cp test_2.py s3://your-mwaa-dags-bucket/
```

> Sync, trigger DAG, view doc_md in UI.

### Step 3: Capture and Review Output

**Context**: Extract the class list for analysis.

Copy rendered string from UI.

> Expect ~300+ classes; search for 'Popen'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Python]]

### Sub-Techniques

-

## Commands Used

- [[commands/jinja2-enumerate-subclasses]]

## Tools Used

-

## Tags

- [[gadget-chain]]
- [[Python]]
