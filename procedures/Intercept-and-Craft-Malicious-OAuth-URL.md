---
tags:
  - csrf
  - oauth
  - url-crafting
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.857Z'
sub_techniques: []
id: 87a3bd00-b253-4c8b-9be8-991d2124024d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Intercept-and-Craft-Malicious-OAuth-URL

## Summary

This procedure involves intercepting the OAuth GET request during HackerOne integration setup and crafting a malicious URL that bypasses CSRF protection, allowing it to be sent to victims for forged authorization.

## Description

Following integration initiation, the frontend makes a GET request to the vulnerable /oauth2/auth endpoint without proper CSRF validation. The attacker intercepts this using browser tools, copies the URL with csrf, scope, and session parameters, but drops the request to avoid legitimate completion. The crafted URL ties the authorization to the attacker's account, exploiting the backend's reliance on the state parameter in callbacks without origin or token checks.

## Requirements

1. Browser with developer tools (e.g., Chrome DevTools)
2. Active HackerOne session from previous setup
3. Knowledge of OAuth parameters

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all GET requests that initiate state changes
- Validate request origins and referrers
- Log and alert on unusual OAuth initiations

## Objectives

1. Capture vulnerable URL components
2. Construct clickable link for victim
3. Preserve exploitability without triggering defenses

## Instructions

### Step 1: Open Developer Tools

**Context**: Prepare to monitor network requests during the flow.

Open browser dev tools (F12), go to Network tab, and clear logs.

### Step 2: Trigger and Intercept GET Request

**Context**: Let the frontend generate the vulnerable GET, then abort it.

Proceed with the integration flow until the GET to https://hackerone.integration-authentication.com/oauth2/auth/:authentication_id appears. Right-click and copy the URL, but cancel the request.

Example URL:

```bash
https://hackerone.integration-authentication.com/oauth2/auth/<Auth ID>?csrf=F_Sr5vd7hWMLSkZoubYOTMbwROI922ZU6q1S4fEF43E=&scope=read:org%20repo&session=1iydW3sIKpyTGxhG8lxeWY9ddzaUknoUJT9Rr51ptMc=
```

> Ensure parameters like csrf and session are intact for forgery.

### Step 3: Verify URL Integrity

**Context**: Test the URL in a sandbox to confirm it initiates flow without errors.

Paste the URL into a new tab or tool to verify it loads the OAuth page.

**Expected Output**: OAuth authorization page loads, ready for victim click.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[oauth]]
- [[url-crafting]]
