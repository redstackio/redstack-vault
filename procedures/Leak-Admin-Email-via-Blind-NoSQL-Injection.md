---
tags:
  - blind-injection
  - data-leak
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
  - '[[Account Discovery]]'
updated_at: '2025-12-14T03:46:14.837Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b5034c7f-95af-46ca-ae89-84155927cb61
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Leak-Admin-Email-via-Blind-NoSQL-Injection

## Summary

This procedure uses blind NoSQL injection to extract an admin's email address character by character from the users collection, enabling targeted password reset attacks.

## Description

By crafting conditional $where queries like {"$where":"this.roles.includes('admin') && /^A/.test(this.services.email.address)"} and iterating over the alphabet, the procedure builds the email via response oracles (e.g., presence/absence in results). It targets the unsanitized query parameter in /api/v1/users.list. Prerequisites include admin identification from prior steps. Expected outcome: Full email for reset requests.

## Requirements

1. Authenticated session from previous procedure
2. Identified admin user ID or username
3. Python script capable of blind extraction logic
4. Vulnerable endpoint access

## Defense

Defensive measures and detection strategies:

- Remove or restrict $where operator usage in MongoDB queries
- Log and alert on repeated similar queries indicating blind extraction
- Encrypt or obfuscate sensitive fields like emails in the database
- Implement rate limiting on user list queries

## Objectives

1. Leak admin email for reset exploitation
2. Demonstrate blind injection feasibility
3. Enable account targeting

## Instructions

### Step 1: Execute Blind Email Leakage

**Context**: Run the script to perform iterative $where tests on email characters.

**Command** ([[commands/python3-post-auth-nosqli]]):
```bash
python3 post_auth_nosqli.py -u attacker -p attacker 'http://localhost:3000'
```

> The script sends payloads testing each position and character, using response length or status as oracle. Expected output: Reconstructed email, e.g., "admin@rocket.chat".

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/python3-post-auth-nosqli]]

## Tools Used

- [[tools/Python3]]
- [[tools/requests]]
- [[tools/post_auth_nosqli.py]]

## Tags

- blind-injection
- data-leak
