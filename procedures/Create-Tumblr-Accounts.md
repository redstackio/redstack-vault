---
tags:
  - account-creation
  - tumblr
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
updated_at: '2025-12-14T17:26:56.427Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b5973c37-3fea-4422-84b7-43c3a968f5b3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-Tumblr-Accounts

## Summary

This procedure outlines the creation of two Tumblr accounts (attacker and victim) using distinct email addresses, including email confirmation to enable messaging functionality, as a prerequisite for exploiting the messaging DoS vulnerability.

## Description

Tumblr requires email-verified accounts for full access to features like messaging. This step involves registering new accounts on the Tumblr platform via its web interface. The attacker uses one email for the sending account and another for the receiving account to simulate the attack scenario. Once created, accounts must be confirmed via email links to activate messaging. This sets up the environment for sending a message that will later cause DoS upon account deletion. No special privileges are needed, and the process is straightforward for any user with valid emails.

## Requirements

1. Access to two unique email addresses (e.g., cyanpiny+attacker@gmail.com and cyanpiny+victim@gmail.com)
2. Web browser with internet access to tumblr.com
3. Ability to receive and click email confirmation links

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from similar IP addresses or email patterns
- Implement CAPTCHA or rate limiting on registration to prevent abuse
- Log and review unusual account creation spikes

## Objectives

1. Establish two functional Tumblr accounts for attack simulation
2. Ensure messaging is enabled on both accounts
3. Prepare for message transmission without triggering early detection

## Instructions

### Step 1: Register Attacker Account

**Context**: Create the account that will send the triggering message.

Navigate to tumblr.com/signup in your web browser. Enter the attacker email (e.g., cyanpiny+attacker@gmail.com), choose a username and password, and complete the registration form. Submit and check the email for the confirmation link.

> Click the confirmation link in the email to activate the account. Upon success, you should be able to log in and access the dashboard.

### Step 2: Register Victim Account

**Context**: Create the receiving account that will suffer the DoS.

Repeat the registration process using the victim email (e.g., cyanpiny+victim@gmail.com). Submit the form and confirm via the email link.

> After confirmation, log in to verify full access, including the messaging section.

### Step 3: Verify Account Functionality

**Context**: Ensure both accounts can log in and access messaging.

Log in to each account separately via tumblr.com/login. Navigate to the messaging inbox to confirm it's accessible.

> Successful login and inbox visibility indicate readiness for the next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[tumblr]]
- [[web]]
