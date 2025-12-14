---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - auth-bypass
  - initial-access
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:24:48.215Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Enter Credentials to Reach 2FA Prompt

## Summary

This procedure initiates the login process on the SingleStore portal by submitting the victim's email and password, advancing to the 2FA challenge without alerting defenses.

## Description

In the context of a 2FA bypass attack, this step establishes a valid session up to the OTP verification. It targets https://portal.singlestore.com/ and assumes the attacker possesses the victim's credentials. The outcome is an active session ready for 2FA interception, exploiting the system's reliance on client-side progression.

## Requirements

1. Victim's email and password
2. Browser with Burp Suite proxy configured (Intercept off initially)
3. Network access to the SingleStore portal

## Defense

Defensive measures and detection strategies:

- Implement client-side fingerprinting to detect proxy usage
- Log all login attempts and monitor for unusual IP patterns

## Objectives

1. Trigger the 2FA prompt using valid primary credentials
2. Maintain an active session for subsequent manipulation
3. Position for OTP brute-force without initial failure flags

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the authentication endpoint to begin the process.

No command required; use browser to visit https://portal.singlestore.com/ and input the victim's email in the email field, password in the password field, then click the login button.

> This submits a POST request to the auth endpoint, returning a 2FA challenge if credentials are valid.

### Step 2: Submit Credentials

**Context**: Confirm credentials to reach 2FA.

Ensure Burp Proxy is capturing traffic but not intercepting yet. Submit the form.

> Expected: Redirect to 2FA input page with session cookie set.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[initial-access]]
