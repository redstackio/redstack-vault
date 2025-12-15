---
id: f6g7h8i9-j0k1-2345-fghi-678901234567
tags:
  - idor
  - broken-access-control
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.256Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# IDOR-for-Unauthorized-User-Update

## Summary

This procedure exploits insufficient authorization in the support review update endpoint to modify any user's details by supplying an arbitrary user_id, enabling IDOR attacks.

## Description

The POST to /support/review/{id} accepts a user_id parameter without validating the requester's ownership, allowing updates to name, email, and username for any account. Requires a second trial account for testing and access to the internal review page. This compromises account integrity and sets up for XSS injection.

## Requirements

1. Access to /support/review/{id} (via previous steps)
2. user_id of target account (e.g., from new trial)
3. CSRF token from page source

## Defense

Defensive measures and detection strategies:

- Enforce user_id ownership checks server-side
- Use session-based authorization for updates
- Audit logs for mismatched user_id and session user
- Implement rate-limiting on update endpoints

## Objectives

1. Modify unauthorized user profiles
2. Inject payloads into user data
3. Escalate to persistent attacks

## Instructions

### Step 1: Obtain Target user_id

**Context**: Create or identify a secondary account.

Register a trial account to get user_id=6.

### Step 2: Craft Update Request

**Context**: Send POST with arbitrary user_id.

From review page, POST name=<inject>&email=jobert%40mydocz.cosmic&username=jobert&user_id=6&_csrf_token=987d.

```http
POST /support/review/{id} HTTP/1.1
Host: h1-415.h1ctf.com

name=<inject-here>&email=jobert%40mydocz.cosmic&username=jobert&user_id=6&_csrf_token=987d
```

> Updates succeed without checks. Expected output: 200 OK, profile changed.

### Step 3: Verify Modification

**Context**: Confirm unauthorized change.

View updated profile or login to second account.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- broken-access-control
