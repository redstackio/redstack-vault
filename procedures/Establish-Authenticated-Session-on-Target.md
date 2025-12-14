---
tags:
  - csrf
  - session
  - web
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
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
updated_at: '2025-12-14T17:27:36.193Z'
sub_techniques: []
id: 38ab5ba2-75c5-4a2e-861f-71589009e955
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Establish Authenticated Session on Target

## Summary

This procedure involves tricking a victim into logging into the target site to establish an active session that can be abused for CSRF attacks.

## Description

In the context of the Stripo CSRF exploit, an authenticated session is required to send requests to the plugins endpoint on behalf of the user. This step relies on social engineering, such as phishing, to get the victim to log in at https://my.stripo.email/ without suspicion. Once logged in, session cookies are set, enabling subsequent cross-site requests.

## Requirements

1. Victim's credentials or phishing site mimicking login
2. Access to victim's browser (via lure)
3. No tools beyond a standard browser

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for logins
- Educate users on phishing risks
- Monitor for unusual login patterns from new IPs

## Objectives

1. Establish valid session cookies
2. Prepare for session abuse
3. Ensure victim remains logged in during attack

## Instructions

### Step 1: Lure Victim to Login

**Context**: Direct the victim to the legitimate login page via email or link.

No command; use social engineering to prompt login at https://my.stripo.email/.

> Victim enters credentials, establishing session.

### Step 2: Verify Session

**Context**: Confirm active session using browser tools.

Use [[tools/Browser-Developer-Tools]] to inspect cookies:

Open DevTools > Application > Cookies > Check for session tokens.

> Expected: Active cookies for .stripo.email domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[csrf]]
- [[session]]
