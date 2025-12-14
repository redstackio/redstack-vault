---
tags:
  - account-creation
  - initial-access
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:13.005Z'
sub_techniques: []
id: 15cce259-0ede-46bb-a2a1-b57ec25cafec
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Test-Victim-and-Attacker-Accounts

## Summary

This procedure sets up two test accounts on the target platform to simulate a victim and attacker, enabling isolated sessions for vulnerability testing in the cashier system.

## Description

In the context of exploiting IDOR in the cashier iframe, creating separate victim and attacker accounts is essential. The victim account represents the target, while the attacker account provides the session from which to inspect and modify the iframe. Accounts must be real and verified to access the cashier functions. Use incognito or separate browsers to prevent cross-session interference.

## Requirements

1. Access to the registration page at https://www.binary.com/signup
2. Valid email addresses for verification
3. Separate browser instances or incognito modes

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation to prevent abuse
- Monitor for multiple accounts from similar IPs or devices
- Require CAPTCHA or additional verification for new registrations

## Objectives

1. Establish authenticated sessions for both personas
2. Obtain account IDs (PINs) for parameter manipulation
3. Ensure isolation to mimic real-world multi-account attacks

## Instructions

### Step 1: Register Victim Account

**Context**: Create the target account to obtain its ID for later exploitation.

Navigate to the signup page and complete registration with victim details. Verify via email and log in to retrieve the account ID from the profile or cashier URL.

### Step 2: Register Attacker Account

**Context**: Create the attacker's account to load the vulnerable iframe.

Repeat registration for the attacker, using different credentials. Log in in a separate browser session and confirm access to the cashier.

### Step 3: Verify Account IDs

**Context**: Extract PINs needed for IDOR.

From each logged-in session, navigate to the cashier or profile to note the account ID (PIN).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[account-creation]]
- [[initial-access]]
