---
tags:
  - validation
  - sanitization-test
  - xss
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
id: 432fe4c7-ef24-4d46-8a42-d54c98be601c
created_at: '2025-12-14T03:15:26.568Z'
updated_at: '2025-12-14T03:15:26.568Z'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Verify-Parameter-Sanitization

## Summary

This procedure tests additional parameters in the vulnerable endpoints to confirm that only specific ones (city_id, language_id) are affected, scoping the vulnerability.

## Description

By injecting payloads into other parameters, this verifies filtering mechanisms, ensuring the issues are isolated and not systemic. This helps in accurate reporting and remediation focus.

## Requirements

1. Knowledge of all parameters in endpoints
2. Variety of test payloads
3. Response analysis tools

## Defense

Defensive measures and detection strategies:

- Consistent sanitization across all parameters
- Automated fuzzing in CI/CD for new params
- Intrusion detection for injection attempts

## Objectives

1. Isolate vulnerable parameters
2. Confirm sanitization in others
3. Scope remediation efforts

## Instructions

### Step 1: Test Other Parameters

**Context**: Inject into non-vulnerable params.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "https://www.zomato.com/widgets/all_collections.php?other_param=%3Cscript%3Ealert(1)%3C/script%3E" -o test.html
```

> Inspect for escaped or blocked payload.

### Step 2: Compare Responses

**Context**: Validate filtering.

> Successful if no execution in browser load.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- verification
- param-test
