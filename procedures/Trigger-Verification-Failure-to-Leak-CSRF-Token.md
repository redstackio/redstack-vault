---
tags:
  - csrf
  - token-leakage
  - web
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
updated_at: '2025-12-14T17:27:29.223Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a2658931-fe23-4a4a-b382-51e3d8bfdf5b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger Verification Failure to Leak CSRF Token

## Summary

This procedure exploits an error handling flaw in the Robocoin wallet verification process to cause a redirect that exposes the CSRF token in the URL query parameter, making it visible in browser history.

## Description

The Robocoin wallet at https://wallet.robocoin.com/verify/ fails to properly handle verification errors, appending the CSRF token to a GET redirect URL. This leakage occurs when an invalid verification request is made, storing the token in the browser's history where it can be accessed. The attack targets authenticated users during account setup or recovery, enabling subsequent CSRF bypasses. Prerequisites include luring the victim to interact with a crafted verification link.

## Requirements

1. Access to a web browser on the victim's machine or ability to induce victim navigation
2. Knowledge of the verification endpoint URL
3. Victim must be in an authenticated session or attempting verification

## Defense

Defensive measures and detection strategies:

- Implement proper error handling to avoid token exposure in URLs
- Use HTTP-only cookies for CSRF tokens instead of query parameters
- Monitor for anomalous verification failures and redirects

## Objectives

1. Induce a verification error to trigger token leakage
2. Ensure the token is captured in browser history
3. Prepare for token reuse in follow-on attacks

## Instructions

### Step 1: Craft Malicious Verification Request

**Context**: Create a link or form that submits invalid data to the verification endpoint, triggering the error redirect.

Navigate to or direct the victim to https://wallet.robocoin.com/verify/ with tampered parameters, such as an invalid ID (e.g., append ?id=invalid to the URL). This simulates a failed verification attempt.

> The browser will process the request, encounter the failure, and redirect to https://wallet.robocoin.com/verify/id?_csrf=token, exposing the token.

### Step 2: Observe the Redirect

**Context**: Confirm the error handling behavior that leaks the token.

After submission, check the browser's address bar or network tab in developer tools (F12) for the redirected URL containing the _csrf parameter.

> Expected: URL updates to include the token, e.g., https://wallet.robocoin.com/verify/id?_csrf=abc123def456. The token is now logged in history.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-leakage]]
