---
id: proc-reddit-create-test-001
tags:
  - account-creation
  - test-setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.356Z'
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
# Create-Test-Reddit-Account

## Summary

This procedure sets up a test Reddit account to simulate a target for verifying the password change rate limiting vulnerability, using a known initial password for controlled brute-forcing.

## Description

In the context of testing Reddit's old interface, create a new account to establish a baseline for the attack. This allows safe experimentation without affecting real users. The procedure assumes browser access and focuses on the web platform. Expected outcome is a functional account ready for password change testing, highlighting the need for initial session control in real attacks.

## Requirements

1. Web browser access to https://old.reddit.com
2. No prior credentials needed, but stable internet connection required
3. Optional: Burp Suite for traffic monitoring during setup

## Defense

Defensive measures and detection strategies:

- Monitor for unusual account creation patterns from single IPs
- Implement CAPTCHA on registration to deter automated testing
- Log all new account activities for anomaly detection

## Objectives

1. Establish a test account with a predictable password for brute-force simulation
2. Verify access to password change functionality
3. Prepare environment for request interception

## Instructions

### Step 1: Register New Account

**Context**: Navigate to the old Reddit interface and complete the registration form to create a test user.

No specific command; use browser to visit https://old.reddit.com/register, enter username, email, and set initial password to !23Qweasdzxc.

> After submission, confirm email if prompted and log in to verify.

### Step 2: Confirm Account Access

**Context**: Log in with the new credentials to ensure the account is active and accessible.

Use browser login form at https://old.reddit.com/login with the set password.

> Successful login redirects to the user dashboard, indicating setup complete.

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

- [[account-creation]]
- [[test-setup]]
