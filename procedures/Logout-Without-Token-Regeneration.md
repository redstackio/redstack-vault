---
tags:
  - csrf
  - session-management
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:06.092Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 14b93de3-ac46-4389-a5ed-b5e6dd2bce96
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Logout-Without-Token-Regeneration

## Summary

This procedure logs out the attacker session on Khan Academy while ensuring the fixed fkey CSRF token remains unchanged in the browser.

## Description

Due to poor session handling, Khan Academy's logout does not regenerate the fkey, leaving it vulnerable to inheritance by subsequent users on the same browser. This step transitions from attacker control to setup for victim session overlap, exploiting the token's persistence in browser storage.

## Requirements

1. Active attacker session with known fkey
2. Access to the logout functionality
3. Browser DevTools for verification

## Defense

Defensive measures and detection strategies:

- Regenerate CSRF tokens on all authentication state changes, including logout
- Clear browser storage on logout
- Detect multi-user logins on shared sessions via logging

## Objectives

1. End attacker session cleanly
2. Preserve fkey for victim inheritance
3. Validate token fixation post-logout

## Instructions

### Step 1: Initiate Logout

**Context**: Trigger the logout action to terminate the session.

Click the logout button or navigate to the logout endpoint (e.g., via user menu on https://www.khanacademy.org).

> The site redirects to the login page, confirming session end, but fkey persists.

### Step 2: Confirm Token Persistence

**Context**: Re-inspect the browser to ensure fkey is unchanged.

Reload a page or check DevTools storage/network tabs post-logout.

> The fkey value remains identical, indicating the fixation vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]] Defense Evasion

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[logout-flaw]]
