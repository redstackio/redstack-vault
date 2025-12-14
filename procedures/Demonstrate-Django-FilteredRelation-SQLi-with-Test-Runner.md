---
tags:
  - sqli
  - django
  - test
type: procedure
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/run-django-filteredrelation-sqli-test]]'
verified: false
platforms:
  - Python
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.058Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 28db8870-4895-4140-b70c-f44e74b88945
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Django-FilteredRelation-SQLi-with-Test-Runner

## Summary

This procedure uses Django's test runner to reproduce and demonstrate the SQLi vulnerability in the FilteredRelation tests.

## Description

Django's test suite includes a POC for this vuln. Running the specific test executes the injection payload, showing the malformed SQL and confirming exploitability in development or audit scenarios.

## Requirements

1. Django source or test environment
2. Python 3 and test dependencies
3. Access to runtests.py

## Defense

Defensive measures and detection strategies:

- Patch Django to fixed version
- Review test outputs in CI/CD for vulns
- Static analysis on ORM usage

## Objectives

1. Reproduce the SQLi POC
2. Validate vulnerability presence
3. Document impact for reporting

## Instructions

### Step 1: Run the Test

**Context**: Execute the test case via the runner to trigger and show the injection.

**Command** ([[commands/run-django-filteredrelation-sqli-test]]):
```bash
python3 django/tests/runtests.py filtered_relation.tests.FilteredRelationTests.test_select_related_foreign_key_sqli
```

> This runs the test. Expected output: SQL query printout with injection, errors, or success indicating malformed JOIN.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/run-django-filteredrelation-sqli-test]]

## Tools Used


## Tags

- sqli
- django
- test
