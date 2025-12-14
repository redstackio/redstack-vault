---
tags:
  - account-creation
  - initial-access
  - web
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:28:59.328Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4b89be34-80f2-43d0-a81a-36cb06a25688
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Multiple-Cloudup-Accounts

## Summary

This procedure involves registering multiple user accounts on the Cloudup platform to facilitate testing of cross-account access controls in a vulnerability assessment scenario.

## Description

In the context of exploiting authentication bypass vulnerabilities, creating separate accounts allows simulation of unauthorized access attempts from different users. This step establishes the foundation for uploading protected content from one account and attempting access from another, revealing flaws in inter-account isolation. The target environment is the web-based Cloudup service, where registration is open and requires only an email address. Expected outcomes include verified account access, enabling subsequent steps in the attack chain.

## Requirements

1. Web browser with internet access
2. Valid email addresses for account verification (two or more)
3. No prior Cloudup account or credentials needed

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account registrations to prevent abuse
- Monitor for suspicious patterns like multiple accounts from similar IPs
- Require CAPTCHA or additional verification for bulk registrations

## Objectives

1. Establish isolated user contexts for cross-account testing
2. Verify platform's account creation process
3. Prepare for privilege escalation simulation

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the Cloudup signup page to begin account creation.

Open a web browser and go to https://cloudup.com. Click on the sign-up or register button.

### Step 2: Register First Account

**Context**: Create the primary account (Account X) for uploading protected files.

Enter a unique email address, choose a password, and complete any required fields. Submit the form and verify the account via the confirmation email if prompted.

### Step 3: Register Second Account

**Context**: Create a secondary account (Account Y) for unauthorized access attempts.

Repeat the registration process with a different email address to create Account Y. Log in to confirm functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[initial-access]]
- [[web]]
