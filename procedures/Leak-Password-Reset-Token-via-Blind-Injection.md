---
tags:
  - token-leak
  - blind-injection
type: procedure
tools:
  - '[[tools/post-auth-nosqli-py]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.447Z'
sub_techniques: []
id: 7f862de9-e0c5-4e46-8e03-4f4deef091bd
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Leak-Password-Reset-Token-via-Blind-Injection

## Summary

This procedure blindly extracts the admin's password reset token using character-by-character $where oracles targeting the services.password.reset.token field.

## Description

Post-reset, the token is stored in MongoDB. Payloads like {"$where":"this.roles.includes('admin') && /^A/.test(this.services.password.reset.token)"} allow inference of each character via response oracles, enabling full reconstruction for takeover.

## Requirements

1. Fresh reset token in DB
2. Admin role filter
3. Automation script for efficiency

## Defense

- Sanitize all query inputs
- Use secure random tokens with short TTL
- Audit DB for injection attempts

## Objectives

1. Reconstruct full reset token
2. Enable password change
3. Achieve account control

## Instructions

### Step 1: Detect Token Length

**Context**: Optional: Guess length first.

**Instructions**: Use string.length tests in $where.

> Expected: Length inferred (e.g., 32 chars).

### Step 2: Enumerate Characters

**Context**: Guess each position.

**Instructions**: For each pos, test a-zA-Z0-9 with regex ^[pos]/.test(token.substr(0,pos+1)).

> Expected: Full token like 'abc123...'. 

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/post-auth-nosqli-py]]

## Tags

- reset-token-leak
