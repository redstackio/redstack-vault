---
tags:
  - nextcloud
  - session-bypass
  - persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:28.237Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Local Accounts]]'
id: 52f70f26-e1bc-46d0-80a3-0a3007185ccd
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Files-Using-Saved-Cookies

## Summary

This procedure reuses saved session cookies to access Nextcloud files, bypassing the app token revocation and demonstrating persistent unauthorized access.

## Description

After revocation, direct token use fails, but session cookies from prior authentication remain valid due to improper validation in Nextcloud. This step submits HTTP requests with the cookies to filesystem endpoints, exploiting the flaw for continued data exposure. Target: Same DAV API paths as Step 2. Expected outcome: Successful file access, confirming the vulnerability.

## Requirements

1. Saved cookies from Step 2
2. HTTP client supporting cookie injection (e.g., curl with --cookie-jar)
3. Same network access as initial steps

## Defense

Defensive measures and detection strategies:

- Invalidate sessions on permission revocation
- Monitor for cookie-based access post-revocation in logs
- Implement token-binding to sessions for stricter controls

## Objectives

1. Exploit access control failure
2. Achieve persistent filesystem access
3. Validate data exposure risk

## Instructions

### Step 1: Prepare Cookie Request

**Context**: Load saved cookies into the client.

In curl, use `--cookie "nc_session_id=value; oc_session_id=value"` or import to browser extensions like Cookie Editor.

### Step 2: Submit Filesystem Request

**Context**: Access files without the revoked token.

Send GET to `/remote.php/dav/files/username/filename.txt` including the cookies in headers. No token needed.

**Expected Output**: File content returned successfully.

### Step 3: Validate Bypass

**Context**: Confirm persistence by repeating access.

Perform multiple requests; access should continue without re-authentication.

**Expected Output**: Consistent success, no permission errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- [[Local Accounts]] Local Accounts

## Commands Used


## Tools Used


## Tags

- nextcloud
- session-bypass
- persistence
