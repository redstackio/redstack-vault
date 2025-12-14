---
tags:
  - 2fa-bypass
  - secret-leak
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
updated_at: '2025-12-14T03:46:14.824Z'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 36bde74b-b4b0-4358-a033-a802bddfbe8e
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Leak-2FA-Secrets-if-Enabled

## Summary

This procedure checks for and leaks 2FA secrets (TOTP or email tokens) from the admin user document if multi-factor authentication is enabled.

## Description

If 2FA is active, blind injection targets fields like this.services.totp.secret or email 2FA hashes using similar $where conditionals. It first probes for 2FA presence, then extracts if found. Requires admin targeting from prior steps. Outcome: Bypasses for 2FA during reset.

## Requirements

1. Admin user document access via injection
2. Knowledge of 2FA field structures
3. Script supporting conditional checks

## Defense

Defensive measures and detection strategies:

- Never store 2FA secrets in plaintext; use secure vaults
- Detect queries accessing auth-related fields
- Enforce 2FA on all sensitive actions
- Rotate secrets periodically

## Objectives

1. Identify and leak 2FA data
2. Remove 2FA barrier for takeover
3. Ensure complete credential compromise

## Instructions

### Step 1: Probe and Leak 2FA Data

**Context**: Use $where to test and extract 2FA fields if present.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> Script checks for 2FA and leaks secrets. Expected output: TOTP secret or hash if enabled, or confirmation of absence.

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

- 2fa-bypass
- secret-leak
