---
id: proc-uuid-004
tags:
  - oauth
  - twitter
  - hijacking
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:35.371Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Complete OAuth Flow to Hijack Access

## Summary

This procedure finalizes the OAuth process in the attacker's session, claiming the access token now associated with the victim's account due to the shared token vulnerability.

## Description

With the victim having authorized the request token, the attacker returns to their original browser session on the third-party site (e.g., unfollowerstats.com, still as TwitterAccount01) and refreshes or continues the flow. The flaw allows the app to issue an access token bound to the victim's credentials, effectively hijacking the session.

## Requirements

1. Original browser session active
2. Victim has authorized the token
3. Third-party site callback handling

## Defense

Defensive measures and detection strategies:

- Enforce user-session binding in OAuth implementations
- Validate authorizing user against initiator
- Audit access token issuances for mismatches

## Objectives

1. Resume and complete the OAuth callback
2. Obtain victim's access token
3. Gain unauthorized app access

## Instructions

### Step 1: Return to Original Session

**Context**: Ensure the initial tab/session is still open.

Switch back to the browser tab with unfollowerstats.com open as the attacker.

### Step 2: Refresh and Authorize

**Context**: Trigger the callback using the pre-authorized token.

Refresh the page or click to proceed; the site detects the authorized token and logs in with the victim's account.

**Expected Output**: Attacker views victim's dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- oauth
- hijacking
