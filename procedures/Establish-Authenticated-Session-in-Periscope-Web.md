---
tags:
  - authentication
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:30:35.145Z'
skill_level: basic
impact_level: low
detection_risk: low
sub_techniques: []
id: 03254830-856e-44f5-bf75-4536040cb4dc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Establish Authenticated Session in Periscope Web

## Summary

This procedure establishes an authenticated session in Periscope Web, a prerequisite for exploiting CSRF in the OAuth flow by ensuring the victim's browser has valid session cookies.

## Description

Periscope Web uses session-based authentication. Logging in sets cookies that authenticate subsequent requests. This step is social-engineered to get the victim to authenticate before visiting the malicious site. Without this, CSRF cannot leverage the session.

## Requirements

1. Victim's Periscope credentials
2. Web browser access
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for logins
- Educate users on phishing and suspicious links
- Monitor for unusual login locations

## Objectives

1. Create active session for CSRF exploitation
2. Verify authentication state
3. Prepare for forged requests

## Instructions

### Step 1: Navigate to Login Page

**Context**: Direct the victim to the Periscope login to initiate authentication.

No command; use browser to access https://periscope.tv and enter credentials.

> Expected: Redirect to dashboard upon success.

### Step 2: Verify Session

**Context**: Confirm session cookies are set using browser dev tools.

Inspect network requests or cookies for auth tokens.

> Expected: Presence of session cookies like 'auth_token'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[authentication]]
- [[web-session]]
