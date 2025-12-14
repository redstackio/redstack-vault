---
tags:
  - authentication
  - session
  - web-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-sync-request-craft]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:47.977Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Default Accounts]]'
id: 249f14c1-1151-4f45-8be0-9fc052369554
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Authenticate-and-Craft-Sync-Request

## Summary

Authenticate to CS.Money using a Steam account to obtain a session cookie, then craft a legitimate POST request to the /sync endpoint for replication in the IDOR exploit.

## Description

CS.Money uses Steam OAuth for login, setting a 'steamid' cookie upon success. This procedure logs in the attacker, navigates to the 3D viewer, triggers a sync action, and captures the request format via browser tools. The request includes JSON payload for builds and backgrounds, which will be modified later. Expected outcome: A templated HTTP request ready for tampering.

## Requirements

1. Valid Steam account for attacker
2. Browser with developer tools (e.g., Chrome DevTools)
3. Access to https://new.cs.money/

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and secure cookie flags (HttpOnly, Secure)
- Log authentication events and monitor for anomalous sessions
- Validate session tokens server-side beyond cookies

## Objectives

1. Establish authenticated session
2. Capture baseline sync request structure
3. Prepare payload for exploitation

## Instructions

### Step 1: Login via Steam

**Context**: Access the site and authenticate to set the steamid cookie.

No command; use browser.

> Navigate to https://new.cs.money/, click login, and complete Steam OAuth. Inspect cookies to confirm 'steamid=7656119XXXXXXXXXX'.

### Step 2: Trigger and Capture Sync

**Context**: Perform an action that sends a /sync POST, then copy as curl.

**Command** ([[commands/curl-sync-request-craft]]):
```bash
curl -X POST https://3d.cs.money/sync \
  -H "Cookie: steamid=7656119XXXXXXXXXX" \
  -H "Content-Type: application/json" \
  -d '{"backgrounds":["/assets/images/back3.jpeg"],"builds":[],"edition":1}'
```

> This replicates the sync with empty builds. Expected output: JSON response indicating successful sync (e.g., {"status":"ok"}).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques

- [[Default Accounts]]

## Commands Used

- [[commands/curl-sync-request-craft]]

## Tools Used


## Tags

- authentication
- web-request
