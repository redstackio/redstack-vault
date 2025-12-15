---
tags:
  - auth-bypass
  - verification
  - account-takeover
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: c4161013-73a7-44c0-8e96-6497f554e1dd
created_at: '2025-12-14T17:33:24.367Z'
updated_at: '2025-12-14T17:33:24.367Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify Bypass on Self-Created Account

## Summary

This procedure creates a test account to obtain a fresh confirmation link, then manipulates its token to confirm the exploit's reproducibility without credentials.

## Description

By self-registering, attackers generate a controlled token to test manipulation reliably. Changing digits (e.g., '2' to '5') bypasses checks, proving the vulnerability's consistency. This validates impact like PII exposure and impersonation potential in a safe manner.

## Requirements

1. Ability to register a new Sorare account
2. Email access for confirmation link receipt
3. [[tools/Web-Browser]] for manipulation

## Defense

Defensive measures and detection strategies:

- Randomize token generation without predictable increments
- Log token access attempts and flag anomalies
- Require CAPTCHA or additional verification on registration

## Objectives

1. Test exploit in controlled environment
2. Confirm unauthorized access mechanics
3. Demonstrate full takeover impact

## Instructions

### Step 1: Create Test Account and Obtain Link

**Context**: Generate a fresh token for manipulation.

Register a new account on sorare.com to receive the email confirmation link, e.g., https://sorare.com/confirm_email?redirectUrl=https%3A%2F%2Fsorare.com%2F&token=qvQfgPqvWV-2FiM5k2f7.

> Expected output: Email with clickable link containing token.

### Step 2: Manipulate and Access

**Context**: Apply the same edit technique to bypass.

Edit token to 'qvQfgPqvWV-5FiM5k2f7' (change '2' to '5') in the address bar and load.

> Expected output: Access to account settings without password entry, verifying takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[verification]]
- [[account-takeover]]
