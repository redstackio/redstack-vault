---
id: proc-uuid-003
tags:
  - authorization-bypass
  - user-enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-bypass-with-token]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:44.930Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# Bypass-Authorization-with-Token-for-User-Enumeration

## Summary

This procedure uses an extracted security token to bypass authentication in ImpressCMS's /include/findusers.php, enabling unauthenticated enumeration of usernames and real names.

## Description

The script in /include/findusers.php checks for a valid token via $_REQUEST['token'] and sets $denied to false without verifying user login status. Tokens from public sources like misc.php are accepted, allowing attackers to query the user database. This leads to full disclosure of registered user details, useful for further attacks like phishing or credential stuffing.

## Requirements

1. Valid token from previous extraction step
2. Access to /include/findusers.php
3. Basic URL parameter handling knowledge

## Defense

Defensive measures and detection strategies:

- Enforce authentication alongside token validation
- Rate-limit requests to findusers.php
- Audit logs for token usage without sessions

## Objectives

1. Gain unauthorized access to user search functionality
2. Extract usernames and real names
3. Demonstrate impact of authorization flaw

## Instructions

### Step 1: Prepare Token Parameter

**Context**: Replace [TOKEN_VALUE] with the extracted token.

No command; manually construct URL: http://target.com/include/findusers.php?token=abc123def456.

> Ensure token is URL-encoded if needed.

### Step 2: Execute Bypass Request

**Context**: Send the request to trigger the flawed check and retrieve data.

**Command** ([[commands/curl-bypass-with-token]]):
```bash
curl "http://target.com/include/findusers.php?token=abc123def456"
```

> Response includes user list; parse for usernames/real names.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-bypass-with-token]]

## Tools Used


## Tags

- [[authorization-bypass]]
- [[user-enumeration]]
