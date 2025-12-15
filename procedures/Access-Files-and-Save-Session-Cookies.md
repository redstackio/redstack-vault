---
tags:
  - nextcloud
  - session-cookies
  - filesystem-access
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:28.247Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 20d3df06-baae-485e-bccd-2225b1db8352
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Files-and-Save-Session-Cookies

## Summary

This procedure uses the app token to authenticate and access Nextcloud files, capturing session cookies generated during the session for persistent reuse.

## Description

Once authenticated with the app token, Nextcloud establishes a session that generates cookies (e.g., session ID, CSRF tokens) for subsequent requests. This step involves making filesystem API calls to read or list files, inspecting the response headers to extract and save these cookies. The saved cookies represent persistent authentication material. Target environment: Nextcloud web API endpoints like `/remote.php/dav/files/`. Expected outcomes: Confirmed file access and stored cookies enabling cookie-based auth.

## Requirements

1. Valid app token from previous step
2. Tools for HTTP requests (browser dev tools or curl)
3. Knowledge of Nextcloud DAV API paths

## Defense

Defensive measures and detection strategies:

- Invalidate all sessions upon permission changes
- Log and alert on unusual session durations or cookie reuse
- Use secure, HttpOnly, SameSite cookies to limit exposure

## Objectives

1. Verify app token functionality on filesystem
2. Extract session artifacts for bypass testing
3. Simulate legitimate access to capture auth state

## Instructions

### Step 1: Authenticate with App Token

**Context**: Initiate a session using the token to access files.

Send a request to a filesystem endpoint, e.g., using browser: navigate to `/apps/files/?dir=/&token=your_app_token` or API call to `/remote.php/dav/files/username/`. Ensure the request succeeds.

### Step 2: Access Target Files

**Context**: Perform read operations to generate full session cookies.

List or download a file, such as via GET `/remote.php/dav/files/username/filename.txt` with the token in query or Basic Auth header. Observe the response.

**Expected Output**: File content or listing returned.

### Step 3: Capture and Save Cookies

**Context**: Extract cookies from the authenticated response.

In browser dev tools (Network tab), copy cookies like `nc_session_id`, `oc_session_id` from Set-Cookie headers. Save them to a file or cookie jar for reuse (e.g., in curl: `--cookie 'nc_session_id=value'`).

**Expected Output**: Cookies stored for Step 4.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- nextcloud
- session-cookies
- filesystem-access
