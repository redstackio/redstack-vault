---
tags:
  - authentication
  - oauth
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:33:12.462Z'
sub_techniques: []
id: 88c66bb4-b174-4408-9860-4cd0db00b32f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Visit-and-Authenticate-to-Target-Site

## Summary

This procedure establishes a legitimate session on the target web platform using GitHub OAuth authentication, generating session cookies that can later be exploited due to improper expiration handling.

## Description

In the context of testing session management vulnerabilities on https://micropurchase.18f.gov/, this step involves navigating to the site and authenticating via GitHub to create an active user session. The platform integrates GitHub for login, setting browser cookies that represent the authenticated state. Due to the root cause of insufficient session expiration, these cookies remain valid even after logout, enabling hijacking. Prerequisites include a GitHub account with access to the platform and a modern browser.

## Requirements

1. Valid GitHub account capable of OAuth login to the target site
2. Browser access to https://micropurchase.18f.gov/ (no VPN or proxy restrictions)
3. Optional: Proxy tool like [[tools/Burp-Suite]] for traffic monitoring

## Defense

Defensive measures and detection strategies:

- Implement server-side session invalidation on logout with short cookie expiration times
- Use HttpOnly and Secure flags on cookies to prevent client-side access and transmission over insecure channels
- Monitor for anomalous login patterns or cookie reuse from unusual IPs

## Objectives

1. Create an active, cookie-based session tied to the victim's account
2. Prepare for cookie extraction in subsequent steps
3. Validate OAuth flow integrity (though flawed in this case)

## Instructions

### Step 1: Navigate to Target Site

**Context**: Access the login page to initiate the authentication process.

No specific command; use browser to visit https://micropurchase.18f.gov/.

> Expected: Landing page with sign-in options loads.

### Step 2: Authenticate via GitHub

**Context**: Use GitHub OAuth to log in and establish the session.

Click the "Sign in through GitHub" button, authorize the app, and complete the flow.

> Expected: Redirect to dashboard with account options; session cookies set in browser dev tools.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[authentication]]
- [[oauth]]
- [[web]]
