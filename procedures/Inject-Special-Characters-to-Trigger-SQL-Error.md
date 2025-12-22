---
tags:
  - sqli
  - injection
  - payload
  - django
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/run-django-sqli-test]]'
verified: false
platforms:
  - Python
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.770Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 466cdf56-3c04-4ac9-8927-2adca17e64f6
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Special-Characters-to-Trigger-SQL-Error

## Summary

This procedure injects special characters like double quotes into the user_input for the JSONField lookup, causing SQL syntax errors in the generated query and proving the injection vulnerability.

## Description

By setting user_input to a payload like 'beeeee"', the concatenation in 'value_custom__' + user_input results in an invalid SQL alias (e.g., "value_custom__beeeee"""), breaking the JSON_EXTRACT clause in the SQL query. This leads to a syntax error, demonstrating how attackers could escalate to arbitrary SQL execution, data leakage, or modification. The procedure uses Django's test runner to reproduce this in a controlled environment.

## Requirements

1. Django test suite modified to include the vulnerable query
2. Test data from previous procedure
3. Access to runtests.py script

## Defense

Defensive measures and detection strategies:

- Validate and escape user inputs in field lookups
- Avoid dynamic field names in ORM; use safe alternatives like extra() with params
- Implement web application firewall (WAF) rules for SQL injection patterns

## Objectives

1. Trigger SQL syntax error via injected quote
2. Observe malformed SQL in logs or error output
3. Confirm potential for arbitrary SQL execution

## Instructions

### Step 1: Modify Test Code

**Context**: Update the test to use the malicious user_input.

**Command** (Edit test file):
```python
user_input = 'beeeee"'
# Then run the query as in previous procedure
```

> Prepares the payload in the test_sqli method.

### Step 2: Run the Test

**Context**: Execute the modified test to generate and run the vulnerable query.

**Command** ([[commands/run-django-sqli-test]]):
```bash
python runtests.py model_fields.test_jsonfield.TestQuerying.test_sqli
```

> Runs the test; expected output is a SQL syntax error like "You have an error in your SQL syntax" due to the malformed alias in JSON_EXTRACT.

### Step 3: Analyze Error

**Context**: Review the generated SQL from logs.

**Command** (Python in Shell with logging):
```python
# Rerun query with payload and capture SQL log
```

> Shows SQL like: SELECT COUNT(...) AS count, (CASE ... ELSE JSON_EXTRACT(..., ?) END) AS "value_custom__beeeee"" ..." confirming injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/run-django-sqli-test]]

## Tools Used


## Tags

- sqli
- injection
- payload
