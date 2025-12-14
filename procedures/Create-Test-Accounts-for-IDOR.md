---
id: proc-create-accounts-idor
tags:
  - idor
  - account-setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.121Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Test-Accounts-for-IDOR

## Summary

This procedure sets up victim and attacker accounts on the IntenseDebate platform to facilitate IDOR exploitation testing, ensuring authenticated access for profile manipulation.

## Description

In an IDOR attack scenario targeting web applications like IntenseDebate, creating separate accounts simulates real-world unauthorized access attempts. The victim account holds the target data, while the attacker account performs the exploit. No special privileges are needed beyond standard registration, but proxy tools like Burp Suite should be configured for traffic interception in later steps. Expected outcome: Two functional accounts ready for profile editing.

## Requirements

1. Internet access to https://intensedebate.com
2. Web browser (e.g., Chrome or Firefox) with proxy support for Burp Suite
3. Valid email addresses for account registration

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account registrations to prevent abuse
- Monitor for multiple account creations from the same IP
- Use CAPTCHA on signup forms to deter automated testing

## Objectives

1. Establish authenticated sessions for victim and attacker
2. Prepare environment for IDOR testing
3. Verify account functionality for profile access

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Access the registration endpoint to create accounts.

**Instructions**: Open a web browser and go to https://intensedebate.com/signup. Fill in the required fields (username, email, password) for the victim account and submit the form.

> Upon success, you will receive a confirmation email and be able to log in.

### Step 2: Create Attacker Account

**Context**: Repeat for the attacker to have a separate session.

**Instructions**: Refresh the signup page or use an incognito window, then register the attacker account with different credentials.

> Log in to both accounts separately to confirm access to https://www.intensedebate.com/edit-user-profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[account-setup]]
