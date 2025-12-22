---
tags:
  - session-reset
  - cookie-clear
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T05:32:10.087Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d5d171b1-603b-4111-b93a-6c034b72ee55
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Logout-Account-and-Clear-Browser-Cookies

## Summary

This procedure terminates the active session on CS.Money and removes browser cookies to reset authentication state, enabling a fresh login attempt for bypass exploitation.

## Description

As part of the 2FA bypass chain, this step ensures no residual session data interferes with partial authentication. It targets the web platform and requires only a browser. Outcomes include a clean slate for re-login without cached tokens.

## Requirements

1. Active session on cs.money
2. Web browser (e.g., Chrome Developer Tools for cookie management)
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Implement session timeout and monitor for frequent logouts followed by incomplete logins
- Use secure cookie flags (HttpOnly, Secure) to prevent easy clearing

## Objectives

1. Invalidate current session
2. Remove authentication artifacts
3. Prepare for partial re-authentication

## Instructions

### Step 1: Initiate Logout

**Context**: End the current user session to prevent carryover of full authentication.

From the CS.Money dashboard, click the logout button in the user menu.

> Browser redirects to login page with session terminated.

### Step 2: Clear Cookies

**Context**: Manually delete domain-specific cookies to erase any persistent auth data.

Open browser developer tools (F12), go to Application/Storage tab, select Cookies for cs.money, and delete all entries.

> Alternatively, use browser settings to clear site data for cs.money.

### Step 3: Verify Reset

**Context**: Confirm no session remnants by reloading the site.

Refresh https://cs.money and ensure it prompts for login without auto-auth.

> No dashboard access indicates successful reset.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-reset]]
- [[cookie-clear]]
