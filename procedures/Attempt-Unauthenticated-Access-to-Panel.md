---
id: proc-attempt-unauth-acronis
tags:
  - auth-bypass
  - web-testing
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:28.537Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Attempt Unauthenticated Access to Panel

## Summary

This procedure tests direct access to a protected web panel without authentication to verify the existence of access controls, setting the stage for bypass attempts.

## Description

In the context of the Acronis notary panel, unauthenticated users are typically blocked from accessing dynamic panel functions. This manual test confirms the block, highlighting that the vulnerability lies in static file handling rather than dynamic execution. No tools or commands are needed; it's performed via a standard web browser. Expected outcome: Access denial, confirming protection for authenticated routes.

## Requirements

1. Web browser with internet access
2. Target URL: notary.acronis.com panel endpoint
3. No credentials or prior setup

## Defense

Defensive measures and detection strategies:

- Implement strict authentication checks on all endpoints, including static file serves
- Use web application firewalls (WAF) to log and block unauthorized access attempts
- Monitor server logs for 401/403 errors on protected paths

## Objectives

1. Confirm authentication enforcement on panel access
2. Identify protected endpoints for targeted bypass testing
3. Establish baseline for vulnerability validation

## Instructions

### Step 1: Navigate to Panel Endpoint

**Context**: Directly attempt to load the panel without logging in to trigger the access control.

Open a web browser and enter the target URL, such as https://notary.acronis.com/panel (replace with actual panel path if known).

> No command needed; use browser address bar. Expected output: Redirect to login, error page (e.g., 401 Unauthorized), or blank/blocked response indicating protection.

### Step 2: Inspect Response

**Context**: Verify the block to ensure it's not an open endpoint.

Use browser developer tools (F12) to check network tab for response codes and headers.

> Look for authentication-related headers or messages. Expected output: Confirmation of denial without file access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[auth-bypass]]
- [[web-testing]]
