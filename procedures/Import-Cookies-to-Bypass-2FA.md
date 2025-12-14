---
tags:
  - cookie-import
  - auth-bypass
type: procedure
tools:
  - '[[tools/Browser-Cookie-Editor]]'
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
updated_at: '2025-12-14T17:24:47.928Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 53f2ee52-5d4d-4282-a742-f59ff6fee632
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Import-Cookies-to-Bypass-2FA

## Summary

This procedure imports stolen session cookies into a new browser to gain authenticated access to a HackerOne account without re-entering 2FA credentials.

## Description

By pasting exported cookies into another browser, the session is restored, exploiting the lack of 2FA re-verification on cookie reuse. Scenario: Attacker uses MitM-stolen cookies to impersonate the user. Target: HackerOne web sessions; outcomes: Immediate access to account features without second factor.

## Requirements

1. Exported cookie data from a valid 2FA session
2. Clean browser instance (incognito or new profile)
3. Cookie editor tool installed

## Defense

Defensive measures and detection strategies:

- Bind sessions to user-agent, IP, or device fingerprints
- Rotate session cookies frequently and invalidate on new devices
- Detect multi-browser logins and trigger alerts or re-auth

## Objectives

1. Restore session via cookie import
2. Verify 2FA bypass by accessing protected areas
3. Maintain persistence without additional factors

## Instructions

### Step 1: Prepare New Browser Session

**Context**: Start a fresh instance to avoid conflicts.

- Open incognito window or new browser profile.
- Navigate to https://hackerone.com.

> Ensures no existing cookies interfere.

### Step 2: Import Cookies

**Context**: Load the stolen cookies to authenticate.

- Activate [[tools/Browser-Cookie-Editor]] extension.
- Paste or import the JSON/text export.
- Set domain to hackerone.com and apply.

> Cookies are injected; refresh the page to activate session.

### Step 3: Validate Access

**Context**: Confirm bypass by navigating to secure sections.

- Go to account dashboard or reports.
- Attempt sensitive actions like viewing private data.

> Grants access without 2FA prompt if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Cookie-Editor]]

## Tags

- cookie-import
- auth-bypass
