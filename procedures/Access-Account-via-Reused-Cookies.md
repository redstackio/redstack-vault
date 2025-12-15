---
tags:
  - unauthorized-access
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:19.355Z'
sub_techniques: []
id: 13986951-6498-48c0-ab8e-5dd4ebb1781c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Access-Account-via-Reused-Cookies

## Summary

This procedure reuses imported session cookies to regain unauthorized access to a Coursera account, including profile viewing and editing, post-logout.

## Description

With reimported cookies, navigate to protected endpoints like /account/profile. Due to delayed invalidation, the session persists, allowing full account control despite UI logout state. This exploits web session management flaws in Coursera. Outcomes include data exfiltration or modification, with access lasting hours.

## Requirements

1. Reimported valid session cookies.
2. Network access to coursera.org.
3. Knowledge of protected endpoints.

## Defense

Defensive measures and detection strategies:

- Use one-time-use tokens refreshed on each request.
- Enforce logout across all tabs/devices.
- Audit logs for session ID reuse after logout events.

## Objectives

1. Restore session without credentials.
2. Access and manipulate account data.
3. Validate vulnerability impact.

## Instructions

### Step 1: Navigate to Protected Endpoint

**Context**: Test cookie validity by accessing account areas.

In the browser, go to https://www.coursera.org/account/profile.

> Page loads with authenticated user data if cookies are valid.

### Step 2: Verify and Exploit Access

**Context**: Confirm full functionality like editing profile.

Attempt to view or edit profile information.

> Successful modifications indicate complete session hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

