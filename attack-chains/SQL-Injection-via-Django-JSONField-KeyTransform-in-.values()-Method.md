---
tags:
  - sqli
  - django
  - jsonfield
  - python
  - web
  - database
type: attack_chain
tools: []
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
  - '[[procedures/Create-Test-Data-in-Django-Database]]'
  - '[[procedures/Execute-Query-with-User-Controlled-Field-Name]]'
  - '[[procedures/Inject-Special-Characters-to-Trigger-SQL-Error]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.779Z'
description: >-
  Demonstrates SQL injection vulnerability in Django's JSONField when user input
  is concatenated into KeyTransform lookups in .values() methods, allowing
  arbitrary SQL execution through unsanitized field aliases.
skill_level: intermediate
impact_level: high
id: f0176da4-d87c-4ead-ae77-25a34d7f48bd
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection via Django JSONField KeyTransform in .values() Method

Multi-stage attack chain demonstrating a complete attack workflow exploiting SQL injection in Django's JSONField handling.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Test Data] --> B[Execute Vulnerable Query]
    B --> C[Inject Payload for SQL Error]
    C --> D[Arbitrary SQL Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Django development environment
- Database with JSON support (e.g., PostgreSQL, MySQL)

### Target Environment

- Django application using JSONField
- Python 3.x with Django installed
- SQL database backend supporting JSON operations

### Initial Access Requirements

- Access to Django codebase or test environment
- Ability to modify ORM queries with user input
- No network access beyond local development setup

## Detailed Attack Procedures

### Step 1: Setup Test Data
procedure: [[procedures/Create-Test-Data-in-Django-Database]]

**Objective**: Prepare database with sample JSON data to test JSONField lookups.

**Instructions**: Use Django ORM to insert records into a model with NullableJSONField.

**Expected Output**: Database populated with JSON objects like {'a': 'b'} and {'b': 'c'}.

**Success Indicators**:
- Records created without errors
- Querying the model returns the inserted data

### Step 2: Execute Vulnerable Query
procedure: [[procedures/Execute-Query-with-User-Controlled-Field-Name]]

**Objective**: Run a query that concatenates user input into the JSONField KeyTransform lookup in .values().

**Instructions**: Filter non-null values and use .values('value_custom__' + user_input) with Count annotation, then access results.

**Expected Output**: Query results with annotated counts and JSON-extracted values.

**Success Indicators**:
- Query executes successfully with benign input
- Results include expected JSON data

### Step 3: Inject Payload
procedure: [[procedures/Inject-Special-Characters-to-Trigger-SQL-Error]]

**Objective**: Introduce special characters in user_input to break SQL syntax and demonstrate injection.

**Instructions**: Set user_input to include double quotes (e.g., 'beeeee"') and execute the test via [[commands/run-django-sqli-test]].

**Expected Output**: SQL syntax error due to malformed JSON_EXTRACT clause.

**Success Indicators**:
- Error message indicating SQL syntax failure
- Generated SQL shows injected quote in field alias

## Attack Chain Summary

### Key Achievements

1. Established vulnerable setup with JSONField data
2. Demonstrated query execution with dynamic field names
3. Confirmed SQL injection via special character payload leading to syntax errors and potential arbitrary execution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
