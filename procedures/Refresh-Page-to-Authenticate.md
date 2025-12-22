---
tags:
  - session-hijacking
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.126Z'
sub_techniques: []
id: ba133c2b-d002-40e9-acc9-2ad69e73ce25
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Refresh Page to Authenticate

## Summary

This procedure reloads the application page to apply the forged PROD_CAS_SESSION cookie, triggering server-side acceptance of the impersonated session.

## Description

After cookie modification, refreshing forces the application to re-evaluate the session based on the unvalidated cookie value. In the vulnerable DoD app, this results in seamless authentication as the victim without further checks.

## Requirements

1. Forged cookie already set
2. Current page on target domain
3. Browser session active

## Defense

Defensive measures and detection strategies:

- Use secure, HttpOnly, and SameSite cookies to prevent client-side tampering
- Server-side token validation with expiration and binding to IP/user-agent
- Detect rapid session changes in logs

## Objectives

1. Apply cookie changes
2. Establish active victim session
3. Confirm impersonation

## Instructions

### Step 1: Reload the Page

**Context**: Trigger session revalidation.

Press F5 or Ctrl+R (Cmd+R on Mac) to refresh the current page, or click the browser refresh button.

**Expected Output**: Page reloads, and the UI updates to reflect the victim's authenticated state (e.g., welcome message with victim's name).

### Step 2: Verify Authentication

**Context**: Check for session indicators.

Look for top-right dropdown showing 'Welcome [Victim's Name]' instead of login prompts.

**Expected Output**: Authenticated interface loads without redirects to login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-hijacking]]
- [[auth-bypass]]
