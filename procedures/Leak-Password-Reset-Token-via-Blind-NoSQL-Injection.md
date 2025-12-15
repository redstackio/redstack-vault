---
tags:
  - nosql-injection
  - blind-injection
  - token-leak
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
  - '[[tools/pre_auth_nosqli.py]]'
tactics:
  - '[[Credential Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:30.571Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7f5aff2b-23ee-4782-8e74-322764bb0e97
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Leak-Password-Reset-Token-via-Blind-NoSQL-Injection

## Summary

This procedure exploits a pre-auth blind NoSQL injection in Rocket.Chat's getPasswordPolicy method to extract password reset tokens character by character using MongoDB $regex operator.

## Description

The 'token' parameter in /api/v1/method.callAnon lacks sanitization, allowing injection of operators like {"$regex":"^A"} to match token prefixes. By observing response differences (policy on match, error on mismatch), the full token is guessed positionally. Targets MongoDB queries for reset tokens. Prerequisites include a generated token from prior reset.

## Requirements

1. Vulnerable Rocket.Chat instance (e.g., 3.12.1)
2. Access to anonymous method call endpoint
3. Python script for automation
4. Knowledge of possible charset (alphanumeric)

## Defense

Defensive measures and detection strategies:

- Sanitize inputs to prevent operator injection
- Use parameterized queries in Node.js/MongoDB
- Log and alert on anomalous API calls with regex patterns

## Objectives

1. Extract full reset token
2. Enable unauthorized access
3. Bypass auth without credentials

## Instructions

### Step 1: Craft and Send Injection Payloads

**Context**: Iterate over token length (assume 32 chars) and charset to build the token.

**Command** ([[commands/run-exploit-script]]):
```bash
python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@rocketchat.local' --leak-token
```

> Script sends payloads like {"token":{"$regex":"^A"}} to getPasswordPolicy. Matches return policy JSON; mismatches error. Builds token progressively. Expected output: Full token printed.

### Step 2: Verify Leak

**Context**: Test partial token in a reset attempt.

**Command** ([[commands/run-exploit-script]]):
```bash
python3 pre_auth_nosqli.py 'http://localhost:3000' 'admin@rocketchat.local' --test-token 'partial_leak'
```

> Confirms partial matches. Expected: Success if accurate.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Python3]]
- [[tools/requests]]
- [[tools/pre_auth_nosqli.py]]

## Tags

- nosql-injection
- blind-injection
- token-leak
