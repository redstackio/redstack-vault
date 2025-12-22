---
id: proc-create-attacker-account
tags:
  - account-creation
  - rocket-chat
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
updated_at: '2025-12-14T17:31:18.949Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
---

# Create-Attacker-Account-in-Rocket-Chat

## Summary

This procedure registers a standard non-admin user account in the Rocket.Chat instance, providing initial access for the attacker to create malicious channels.

## Description

Using the web UI's registration feature, create a user with limited privileges. This simulates a legitimate user who later exploits the vulnerability. No special tools are needed beyond a web browser; the process leverages default open registration settings in the setup.

## Requirements

1. Running Rocket.Chat instance with registration enabled
2. Web browser access to http://localhost:3000
3. No existing attacker account

## Defense

Defensive measures and detection strategies:

- Disable open registration and require admin approval for new users
- Monitor user creation logs for suspicious patterns
- Implement CAPTCHA on registration forms

## Objectives

1. Gain authenticated access as a non-privileged user
2. Prepare for channel creation exploitation
3. Verify login functionality

## Instructions

### Step 1: Access Registration

**Context**: Navigate to the login/registration page.

**Instructions**: Open http://localhost:3000 in a browser and click the registration option.

### Step 2: Fill Registration Form

**Context**: Provide credentials for the attacker account.

**Instructions**: Enter username 'attacker', password 'attacker', and any required email. Submit the form.

**Expected Output**: Confirmation message and redirect to dashboard.

### Step 3: Verify Login

**Context**: Test the new account.

**Instructions**: Log out if needed, then log in with 'attacker'/'attacker'.

**Expected Output**: Successful access to user interface without admin features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- rocket-chat

