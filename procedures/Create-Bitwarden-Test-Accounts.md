---
id: proc-bitwarden-create-accounts
tags:
  - bitwarden
  - account-creation
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
updated_at: '2025-12-14T17:29:36.677Z'
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
# Create-Bitwarden-Test-Accounts

## Summary

This procedure creates two new Bitwarden user accounts to serve as the basis for testing organization role management. It establishes attacker-controlled identities for simulating owner and admin roles in the privilege escalation attack.

## Description

Bitwarden allows free registration of user accounts via its web interface. This step involves navigating to the signup page, providing email and password details, and completing any email verification. No special privileges are required, making it a low-barrier entry point. The accounts will later be used to create an organization and demonstrate the escalation flaw. Expected outcome: Two functional accounts ready for organization setup.

## Requirements

1. Web browser with JavaScript enabled
2. Valid email addresses for registration (e.g., temporary emails if testing)
3. Internet access to app.bitwarden.com

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from suspicious IPs
- Implement CAPTCHA on signup to deter automation
- Rate-limit registrations per IP/email domain

## Objectives

1. Obtain two independent Bitwarden accounts
2. Verify account functionality via login
3. Prepare for organization invitation workflow

## Instructions

### Step 1: Register AccountA

**Context**: Create the primary account that will own the organization initially.

Navigate to https://app.bitwarden.com/signup in your browser. Enter an email address and strong password for accountA. Complete the registration form and submit.

If email verification is prompted, check the inbox and click the verification link.

Log in to confirm: Go to https://app.bitwarden.com, enter credentials, and ensure dashboard loads.

### Step 2: Register AccountB

**Context**: Create the secondary account that will be invited as admin and escalated.

Repeat the registration process for accountB using a different email and password. Verify via email if required, then log in to confirm access.

**Expected Output**: Both accounts active with successful logins; no errors in credential storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[bitwarden]]
- [[account-creation]]
