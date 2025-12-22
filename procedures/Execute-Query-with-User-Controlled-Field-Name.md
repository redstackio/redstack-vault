---
tags:
  - sqli
  - django
  - jsonfield
  - query
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:04.774Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 6683f2a1-464d-42fc-9c5b-3b683979178a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Query-with-User-Controlled-Field-Name

## Summary

This procedure executes a Django ORM query that incorporates user-controlled input into a JSONField KeyTransform lookup via the .values() method, setting up the vulnerability for injection.

## Description

The attack involves filtering non-null JSON values and using .values('value_custom__' + user_input) with an annotation like Count('id'). Results are iterated to access the extracted values. This simulates a dynamic query where user input influences the field name, leading to unsanitized SQL alias generation in backends like MySQL or PostgreSQL. Expected outcomes include successful data retrieval with benign input, but vulnerability to injection with malicious input.

## Requirements

1. Django shell or test environment with populated NullableJSONModel
2. User input variable defined (initially benign, e.g., 'a')
3. Database connection configured for JSON operations

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs before ORM concatenation
- Use parameterized queries or whitelisting for field names
- Monitor query logs for anomalous field aliases

## Objectives

1. Demonstrate dynamic field lookup in .values()
2. Retrieve annotated counts and JSON values
3. Highlight lack of input validation in KeyTransform

## Instructions

### Step 1: Define User Input

**Context**: Set a benign user_input to test normal query behavior.

**Command** (Python in Shell):
```python
user_input = 'a'
```

> Prepares the input for concatenation.

### Step 2: Build and Execute Query

**Context**: Filter non-null values, annotate count, and use dynamic .values().

**Command** (Python in Shell):
```python
from django.db.models import Count

from myapp.models import NullableJSONModel

results = (NullableJSONModel.objects
           .filter(value_custom__isnull=False)
           .annotate(count=Count('id'))
           .values('value_custom__' + user_input))

for result in results:
    print(result['value_custom__' + user_input])
```

> Executes the query; expected output is JSON values like 'b' for the first record.

### Step 3: Inspect Generated SQL

**Context**: Enable query logging to observe SQL generation.

**Command** (Python in Shell):
```python
import logging
logging.getLogger('django.db.backends').setLevel(logging.DEBUG)
```

> Rerun the query to log SQL, showing JSON_EXTRACT without injection issues.

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
- query
