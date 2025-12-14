---
tags:
  - error-based
  - confirmation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqli-error-based-or1-test]]'
  - '[[commands/sqli-error-based-or-1-equals-2-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.229Z'
sub_techniques: []
id: 0833fcd4-eae6-4f8f-9513-b66f65a2150f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Confirm-SQLi-with-Error-Based-Payloads

## Summary

This procedure confirms SQL injection using error-based techniques by eliciting database errors or hangs when time-based methods cause instability.

## Description

When the database hangs during time-based tests, switch to payloads that force error messages, such as malformed OR conditions. Tested payloads '1 or1' (no space) trigger 500 errors with custom messages, while '1 or 1=2' causes hangs. Applicable to the PHP/MySQL setup where initial error-based worked without issues.

## Requirements

1. Endpoint access and prior vulnerability suspicion
2. Ability to handle potential hangs (increase timeouts)
3. Log analysis for error details

## Defense

Defensive measures and detection strategies:

- Customize error pages to avoid leaking info (e.g., no 'doc_id not found')
- Rate-limit requests to prevent abuse
- Monitor for 500 errors correlated with suspicious inputs
- Enable PHP error logging without exposure

## Objectives

1. Obtain error messages confirming injection
2. Differentiate true/false conditions via errors/hangs
3. Validate when primary method fails

## Instructions

### Step 1: Test 'or1' Payload

**Context**: Inject a simple OR without space to trigger a parsing error and custom 500 response.

**Command** ([[commands/sqli-error-based-or1-test]]):
```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 or1" -v
```

> Expected: HTTP 500 with body containing 'doc_id 1 or1 not found'.

### Step 2: Test 'or 1=2' Payload

**Context**: Use a false boolean to cause query hang or timeout.

**Command** ([[commands/sqli-error-based-or-1-equals-2-test]]):
```bash
curl -X GET "https://████/library.php?path=test&doc_id=1 or 1=2" --max-time 60 -v
```

> Expected: Request hangs or times out, confirming execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqli-error-based-or1-test]]
- [[commands/sqli-error-based-or-1-equals-2-test]]

## Tools Used


## Tags

- [[error-based]]
- [[sqli]]
