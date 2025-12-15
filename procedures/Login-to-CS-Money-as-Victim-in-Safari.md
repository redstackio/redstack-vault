---
id: proc-uuid-1
tags:
  - authentication
  - safari
type: procedure
tools:
  - '[[tools/Safari-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:49.694Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-to-CS-Money-as-Victim-in-Safari

## Summary

This procedure authenticates a victim session on CS Money using Safari, establishing the necessary cookies for subsequent CSRF exploitation.

## Description

In the context of the CSRF attack, the victim must have an active session. This step simulates logging in via Steam to ensure authenticated requests can be forged later. It targets the web platform and relies on Safari for consistency with the exploit's browser specificity.

## Requirements

1. Safari browser on macOS
2. Valid Steam credentials for the victim account
3. Internet access to new.cs.money

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) to prevent unauthorized changes
- Monitor for anomalous login patterns from unusual user agents

## Objectives

1. Create an authenticated session
2. Set session cookies for CSRF targeting
3. Prepare for cross-site requests

## Instructions

### Step 1: Launch Safari and Navigate

**Context**: Open the browser and access the login page to initiate authentication.

No command required; manually navigate to https://new.cs.money and click login with Steam.

> Expected: Steam OAuth flow starts.

### Step 2: Complete Steam Login

**Context**: Authorize the application to grant session access.

No command; follow Steam prompts to approve.

> Expected: Redirect back to CS Money dashboard with active session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari-Browser]]

## Tags

- authentication
- safari
