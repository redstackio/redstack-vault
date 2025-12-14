---
tags:
  - blind-injection
  - token-leak
type: procedure
tools:
  - '[[tools/Python3]]'
  - '[[tools/requests]]'
  - '[[tools/post_auth_nosqli.py]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/python3-post-auth-nosqli]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.825Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ac01b912-8e1b-4030-9a62-cc8fdb68461a
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Leak-Password-Reset-Token-via-Blind-Injection

## Summary

This procedure extracts the admin's password reset token character by character using blind NoSQL injection on the token field.

## Description

Targeted $where queries like {"$where":"this._id == 'adminId' && /^A/.test(this.services.password.reset.token)"} are sent to users.list, using response oracles to build the token. Requires prior reset request and admin ID. This enables direct password change without further auth.

## Requirements

1. Generated reset token from previous step
2. Admin user ID
3. Blind injection script

## Defense

Defensive measures and detection strategies:

- Sanitize queries to prevent field access via $where
- Store tokens encrypted or in separate collections
- Detect iterative queries on specific fields
- Use query parsing to block conditional JavaScript

## Objectives

1. Obtain usable reset token
2. Enable password reset
3. Advance to account takeover

## Instructions

### Step 1: Perform Token Leakage

**Context**: Iterate over token characters with tailored queries.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> Script builds token via oracle responses. Expected output: Full token string, e.g., a 40-char hash.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/python3-post-auth-nosqli]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]
- [[tools/post_auth_nosqli.py]]

## Tags

- blind-injection
- token-leak
