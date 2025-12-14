---
tags:
  - google
  - setsid
  - logout
type: procedure
tools:
  - '[[tools/Clean-Browser-Instance]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Google
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.910Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 80bdeb2f-8172-46d2-8708-a5aca189f220
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-Google-SetSID-Logout-and-Relogin

## Summary

This procedure exploits the Google SetSID endpoint to log out the victim from their Google session and force a relogin, setting the stage for credential interception via a malicious app.

## Description

When the victim clicks the truncated link, it resolves to accounts.youtube.com/accounts/SetSID with parameters that initiate a session invalidation (logout) and redirect to a controlled site. This targets logged-in users, prompting credential re-entry. Use a clean browser to test without interference from existing sessions.

## Requirements

1. Victim logged into Google in browser
2. Malicious URL with SetSID and continue parameters
3. Clean browser instance for testing

## Defense

Defensive measures and detection strategies:

- Verify unexpected logouts and avoid re-entering creds on suspicious redirects
- Implement app verification in Google OAuth flows
- Monitor for anomalous SetSID usage

## Objectives

1. Invalidate current Google session
2. Prompt victim for credentials on redirect
3. Transition to credential capture phase

## Instructions

### Step 1: Resolve Full URL on Click

**Context**: The truncated link expands to the SetSID endpoint upon click.

Navigate to the URL in a browser.

> Expected: Google logout page loads.

### Step 2: Handle Redirect After Logout

**Context**: Post-logout, redirect via 'continue' parameter to malicious site.

Allow browser to follow redirect.

> Expected: Relogin prompt appears, credentials entered.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Clean-Browser-Instance]]

## Tags

- [[google]]
- [[setsid]]
- [[logout]]
