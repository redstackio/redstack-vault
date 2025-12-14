---
id: 2da99995-33d7-4fd2-9e50-071644f9a730
name: Reproduce-Simplenote-Logout-Session-Flaw
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.106Z'
tactics:
  - '[[Collection]]'
  - '[[Persistence]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
sub_techniques: []
tags:
  - information-disclosure
  - session-management
  - web-vulnerability
commands: []
platforms:
  - Web
tools:
  - '[[tools/Google-Chrome]]'
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Collection]]'
  - '[[Persistence]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---

# Reproduce-Simplenote-Logout-Session-Flaw

## Summary

This procedure reproduces an information disclosure vulnerability in the Simplenote web application by demonstrating how logout does not properly invalidate the browser session, enabling access to authenticated content via the back button and exposing sensitive user notes.

## Description

The Simplenote web app at https://app.simplenote.com/ suffers from a session management flaw where the logout action fails to fully terminate the authenticated session on the client side. After logout, the browser's history and caching mechanisms allow navigation back to protected pages, restoring access without re-authentication. This can lead to unauthorized exposure of user data if the device is accessed by others post-logout. The procedure requires a valid account and uses standard browser navigation; no advanced tools are needed. Expected outcome is viewing protected notes after apparent logout, confirming the vulnerability.

## Requirements

1. Valid Simplenote account credentials (email and password)
2. Web browser such as [[tools/Google-Chrome]] (version 35.0.1916.114m or compatible)
3. Internet access to reach https://app.simplenote.com/
4. No proxy or VPN required, but ensure no browser extensions interfere with sessions

## Defense

Defensive measures and detection strategies:

- Implement proper session invalidation on logout by clearing cookies, tokens, and cache
- Use HTTP-only and secure flags on session cookies to prevent client-side persistence
- Redirect to a non-cacheable page post-logout and include client-side JavaScript to clear history
- Monitor for anomalous access patterns post-logout via server-side logging

## Objectives

1. Gain initial authenticated access to Simplenote
2. Trigger logout to simulate session termination
3. Exploit back navigation to disclose protected information
4. Validate unauthorized data exposure without re-authentication

## Instructions

### Step 1: Navigate and Authenticate

**Context**: Establish an active session by accessing the application and logging in to view protected content.

No specific command; use the browser interface:

Open [[tools/Google-Chrome]] and go to https://app.simplenote.com/. Enter credentials and submit the login form.

> This creates an authenticated session, loading the notes dashboard. Verify by checking that personal notes are visible.

### Step 2: Initiate Logout

**Context**: Perform logout to test session termination, which should prevent further access.

No specific command; use the application UI:

Click the logout button in the user menu or settings area.

> The page redirects to the login screen, but the session remains partially active in the browser.

### Step 3: Exploit with Back Navigation

**Context**: Use browser history to bypass the logout and restore access to sensitive data.

No specific command; use browser controls:

Press the back button (or Alt+Left Arrow) to navigate to the previous authenticated page.

> The dashboard reloads with full access to notes, confirming the disclosure without prompting for login.

### Step 4: Validate Disclosure

**Context**: Confirm the vulnerability by interacting with protected content.

No specific command; inspect the page:

Attempt to view or edit a note on the restored page.

> Successful interaction indicates the session is still valid, exposing user data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]
- [[Persistence]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome]]

## Tags

- [[information-disclosure]]
- [[session-management]]
- [[web-vulnerability]]
