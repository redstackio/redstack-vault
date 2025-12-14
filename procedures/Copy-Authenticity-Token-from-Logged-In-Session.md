---
id: proc-uuid-1
tags:
  - csrf
  - token-theft
  - session
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
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:03.185Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Copy-Authenticity-Token-from-Logged-In-Session

## Summary

This procedure extracts the CSRF authenticity token from a logged-in browser session on a shared workstation, exploiting the fact that the token does not regenerate after login, allowing it to be reused across user sessions.

## Description

In vulnerable web applications like the reported Liberapay instance, the CSRF token remains static post-login, violating secure design by permitting persistence. An attacker with brief access to a shared device can inspect the session, copy the token, and prepare for subsequent exploitation. This targets environments with multi-user workstations, such as public libraries or offices, where users log in sequentially without clearing browser data.

## Requirements

1. Access to a shared workstation with browser logged into the target application
2. Basic knowledge of browser developer tools
3. No special privileges beyond standard user login

## Defense

Defensive measures and detection strategies:

- Regenerate CSRF tokens on every login or session change
- Implement per-session token binding to user accounts
- Monitor for anomalous requests from shared IPs or devices

## Objectives

1. Obtain a valid, static CSRF token for reuse
2. Enable crafting of authenticated requests without victim's direct input
3. Set up for unaware execution by next user

## Instructions

### Step 1: Log In and Inspect Session

**Context**: Gain temporary access to the shared workstation and authenticate to the target web application to expose the token.

Log in using a legitimate account. Open browser developer tools (F12 in most browsers) and navigate to the Network or Elements tab.

**Expected Output**: Visible form elements or headers containing the token.

### Step 2: Extract Token Value

**Context**: Locate and copy the authenticity token from the session data.

Search for 'authenticity_token' or 'csrf_token' in the page source or request headers. Copy the value (e.g., a 32-character string).

**Expected Output**: Token string ready for use, e.g., "X-CSRF-Token: abc123def456ghi789".

### Step 3: Verify Token Persistence

**Context**: Confirm the token does not change to ensure exploit viability.

Simulate a logout and relogin or refresh the session; re-inspect to verify the token remains identical.

**Expected Output**: Unchanged token value across actions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[token-theft]]
