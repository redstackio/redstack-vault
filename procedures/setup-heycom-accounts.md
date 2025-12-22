---
id: proc-uuid-001
tags:
  - account-setup
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:55:20.604Z'
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
# Setup Hey.com Accounts

## Summary

This procedure establishes the necessary user accounts on hey.com to enable testing of email forwarding for stored XSS injection, simulating attacker-controlled sender and receiver environments.

## Description

In the context of exploiting stored XSS in hey.com's forwarding feature, two accounts are required: one to send and inject payloads via forwarding, and another to receive and trigger the payload. This setup assumes no prior access and focuses on legitimate account creation to avoid detection. Expected outcome is authenticated sessions for both accounts, allowing seamless progression to payload injection.

## Requirements

1. Web browser access to hey.com
2. Valid email addresses for registration (use disposable if testing)
3. No VPN or proxies initially to mimic normal user behavior

## Defense

Defensive measures and detection strategies:

- Rate limiting on account creation to prevent bulk registrations
- Email verification delays to slow automated setups
- Monitor for unusual account pairing in forwarding patterns

## Objectives

1. Gain initial access to hey.com platform
2. Prepare controlled environment for payload delivery
3. Ensure accounts are functional for email operations

## Instructions

### Step 1: Register Sender Account

**Context**: Create the primary account for composing and forwarding malicious emails.

Navigate to hey.com and complete the registration form with a new email address. Verify the account via the confirmation email and log in.

**Expected Output**: Successful login dashboard.

### Step 2: Register Receiver Account

**Context**: Create a secondary account to receive forwarded emails and test payload execution.

Repeat registration process with a different email. Log in to confirm access to Imbox.

**Expected Output**: Access to empty Imbox.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-setup
- initial-access
