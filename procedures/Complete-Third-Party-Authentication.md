---
id: proc-weblate-complete-auth
tags:
  - authentication
  - oauth
  - third-party
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
updated_at: '2025-12-14T17:31:10.964Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Complete Third-Party Authentication

## Summary

This procedure simulates or guides the victim through the third-party OAuth authentication process in Weblate, triggering the evaluation of the malicious 'next' parameter upon successful login.

## Description

After accessing the endpoint, the user is redirected to the third-party provider (e.g., GitHub) for credentials. Upon approval, Weblate receives the callback and processes the 'next' parameter, applying the flawed sanitization that allows the open redirect. This step is crucial as the vulnerability only activates post-authentication.

## Requirements

1. Valid account on the third-party provider (e.g., GitHub)
2. Access to the malicious URL from Step 1
3. No additional tools; uses standard browser OAuth flow

## Defense

Defensive measures and detection strategies:

- Log all OAuth callbacks and inspect 'next' parameters for anomalies
- Implement rate limiting on authentication attempts
- Use multi-factor authentication (MFA) to add friction to phishing
- Alert on redirects to external domains post-auth

## Objectives

1. Authenticate the user via third-party provider
2. Return control to Weblate for 'next' processing
3. Enable the redirect without interruption

## Instructions

### Step 1: Initiate OAuth Flow

**Context**: From the loaded auth page, click the provider login button to start OAuth.

No command; browser action: Select GitHub login and enter credentials.

> The provider redirects back to Weblate with auth code.

### Step 2: Approve and Complete Login

**Context**: Authorize the application on the provider side.

Browser action: Approve scopes and complete login.

> Expected output: Weblate dashboard loads momentarily before redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- authentication
- weblate
