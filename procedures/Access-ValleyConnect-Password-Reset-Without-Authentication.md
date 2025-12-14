---
id: proc-tva-password-reset-bypass
name: Access-ValleyConnect-Password-Reset-Without-Authentication
type: procedure
verified: false
submitted: true
created_at: '2023-10-17T00:00:00Z'
updated_at: '2025-12-14T17:31:52.479Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - auth-bypass
  - web
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Access-ValleyConnect-Password-Reset-Without-Authentication

## Summary

This procedure demonstrates accessing the password reset page in TVA ValleyConnect without authentication, exposing password rules and self-service functionality to unauthorized users.

## Description

From the main portal (after Step 1), clicking the password reset menu leads to https://valleyconnect.tva.gov/password-rules without checks, revealing application logic like password policies. This is part of the broader auth bypass in the web app, targeting public HTTPS access. Outcomes include potential enumeration of reset flows, though no actual resets occur without creds.

## Requirements

1. Successful completion of main portal access.
2. Web browser with JavaScript enabled.
3. Direct URL access if menu is unavailable.

## Defense

Defensive measures and detection strategies:

- Enforce authentication middleware on all self-service endpoints.
- Log and block direct access to /password-rules from unauthenticated IPs.

## Objectives

1. Load password reset interface.
2. View sensitive configuration like rules.
3. Confirm bypass extends to user actions.

## Instructions

### Step 1: Navigate to Password Reset

**Context**: Use the portal's menu or direct URL to access the reset page.

In the browser, click the 'Reset Password' menu item from the main page, or directly visit https://valleyconnect.tva.gov/password-rules.

> Page loads showing password requirements (e.g., length, complexity). Success if no login redirect occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- auth-bypass
- web
