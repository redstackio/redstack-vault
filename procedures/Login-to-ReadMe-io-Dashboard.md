---
id: proc-uuid-003
tags:
  - authentication
  - session
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
updated_at: '2025-12-13T23:52:33.885Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-ReadMe-io-Dashboard

## Summary

This procedure authenticates the registered user to the ReadMe.io dashboard, establishing a session with necessary cookies and tokens for API requests.

## Description

Using the verified credentials, log in to https://dash.readme.io to access the management interface. This step sets session cookies and CSRF tokens (X-XSRF-TOKEN) required for subsequent POST requests. The dashboard provides visibility into projects and users, but in this exploit, it's used as a stepping stone for unauthorized access.

## Requirements

1. Verified ReadMe.io account credentials
2. Web browser or HTTP client
3. Cookies enabled

## Defense

Defensive measures and detection strategies:

- Enforce multi-factor authentication (MFA) for logins.
- Log and alert on login attempts from new locations.
- Use short session timeouts.

## Objectives

1. Establish authenticated session.
2. Obtain CSRF token for API calls.
3. Access dashboard for verification.

## Instructions

### Step 1: Submit Login Credentials

**Context**: Authenticate to gain session access.

No command; browser-based:

1. Go to https://dash.readme.io/login.
2. Enter email and password, submit.

> Successful login redirects to dashboard; inspect cookies in DevTools (Application tab).

### Step 2: Capture Session Token

**Context**: Extract X-XSRF-TOKEN for protected requests.

1. In DevTools Network tab, reload dashboard.
2. Find a request (e.g., to /api/projects) and copy X-XSRF-TOKEN from headers.

> Token is now available for use in POST requests.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[authentication]]
- [[web]]
