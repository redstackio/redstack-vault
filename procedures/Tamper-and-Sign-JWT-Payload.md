---
tags:
  - jwt-tampering
  - impersonation
type: procedure
tools:
  - '[[tools/jwt-io]]'
tactics:
  - '[[Persistence]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 3ed2d0d4-8096-4e78-967f-360e651ff8a7
created_at: '2025-12-13T09:01:26.686Z'
updated_at: '2025-12-13T09:01:26.686Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Tamper and Sign JWT Payload

## Summary

This procedure modifies the JWT payload and signs it using the extracted secret to create a forged token.

## Description

The attacker alters key claims like email, iat, and jti, then uses the hardcoded HMAC secret to sign the token. This enables impersonation in Zendesk. The approach exploits unsecured credentials in client-side code.

## Requirements

1. Decoded JWT and extracted secret
2. Victim's email address
3. Tool for signing JWTs

## Defense

Defensive measures and detection strategies:

- Store secrets server-side and rotate regularly
- Validate JWTs on the server with additional checks

## Objectives

1. Forge a valid JWT for target user
2. Enable unauthorized access
3. Demonstrate impersonation

## Instructions

### Step 1: Modify and Sign

**Context**: Tamper with payload fields.

In jwt.io, modify iat to current Unix timestamp, jti to random UUID v4, email to victim's email, and sign using the extracted HMAC secret oq1HJ4jXo99Wt41bwvLh9BXBVdgpi52CjkXbThow7UhWQGtJ.

> Generate the new signed JWT string.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/jwt-io]]

## Tags

- [[jwt-tampering]]
- [[impersonation]]
