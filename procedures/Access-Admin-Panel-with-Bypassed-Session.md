---
tags:
  - session-exploitation
  - admin-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 91f038e8-3e65-438c-837b-d2a164f9fec7
created_at: '2025-12-14T17:30:47.331Z'
updated_at: '2025-12-14T17:30:47.331Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Admin-Panel-with-Bypassed-Session

## Summary

This procedure leverages a bypassed OAuth session to access restricted areas of the Mapbox internal portal, including the admin panel, allowing viewing of sensitive data without proper authentication.

## Description

Once a valid session is obtained via the OAuth bypass, attackers can directly navigate to authenticated endpoints. In the Mapbox case, this grants entry to the admin panel, exposing user data, configurations, and other internal information. The procedure assumes the session cookie is already captured and focuses on injection and navigation to exploit the lack of auth checks.

## Requirements

1. Valid session cookie from the bypass procedure
2. Knowledge of protected URLs (e.g., /admin)
3. Browser or scripting tool for cookie injection

## Defense

Defensive measures and detection strategies:

- Enforce token validation on every protected endpoint
- Implement rate limiting and anomaly detection on session usage
- Audit session logs for accesses without preceding successful auth

## Objectives

1. Gain entry to admin panel and authenticated resources
2. Extract sensitive information
3. Maintain access for further reconnaissance

## Instructions

### Step 1: Inject Session Cookie

**Context**: Set the captured cookie in the browser or request to impersonate an authenticated user.

Open the portal in a browser, use an extension like Cookie Editor to add the session cookie, or craft requests with the Cookie header.

> Example request: GET /admin HTTP/1.1 Host: internal.mapbox.com Cookie: session_id=abc123

Expected: Server accepts the request as authenticated.

### Step 2: Navigate to Admin Panel

**Context**: Access restricted paths using the session.

Directly visit /admin or other protected URLs. Interact with the interface to view data.

> No command; manual navigation or scripted GET requests to /admin/dashboard.

Expected: Admin interface loads with full access to features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-exploitation]]
- [[admin-access]]
