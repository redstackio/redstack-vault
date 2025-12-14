---
tags:
  - csrf
  - request-capture
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-capture-deletion-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:29.443Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: ff65dc5f-fed4-49cd-a946-9fe30764ae41
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture Account Deletion Request Using Burp Suite

## Summary

This procedure involves creating a GitLab account and intercepting the account deletion POST request to extract the CSRF authenticity_token for later reuse in bypassing protections.

## Description

In the context of exploiting a CSRF vulnerability in GitLab's account deletion, this step requires registering an account, navigating to the deletion form, and using a proxy like Burp Suite to capture the POST request to `/users`. The request includes `_method=delete` and `authenticity_token`, which is not properly invalidated across sessions due to issues with Warden authentication hooks during email confirmation.

## Requirements

1. Access to GitLab instance (public or local on port 3000)
2. Temporary email service for account creation
3. Burp Suite configured as browser proxy
4. Browser session for navigation

## Defense

Defensive measures and detection strategies:

- Implement proper CSRF token rotation on authentication events
- Monitor for anomalous deletion requests from unusual referers
- Use session invalidation on new account creation

## Objectives

1. Obtain a valid authenticity_token from deletion form
2. Capture full POST request details for modification
3. Prepare for token reuse in cross-session attack

## Instructions

### Step 1: Register and Log In

**Context**: Create an attacker account to access the deletion form.

Navigate to GitLab registration, use a temporary email, and log in. No command needed; perform via browser.

### Step 2: Intercept Deletion Request

**Context**: Submit the deletion form while proxying traffic to capture the token.

Configure Burp Suite proxy, go to `/profile/account`, fill and submit deletion. Intercept the POST.

**Command** ([[commands/curl-capture-deletion-request]]):
```bash
curl -X POST https://gitlab.com/users \
  -H "Cookie: _gitlab_session=1staccount_cookie;" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "_method=delete&authenticity_token=auth_1staccount"
```

> This simulates the captured request; in Burp, drop and inspect to note the token. Expected output: Intercepted request with token visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-capture-deletion-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- csrf
- request-interception
