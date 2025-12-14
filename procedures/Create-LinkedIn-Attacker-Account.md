---
tags:
  - account-creation
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:25:18.081Z'
sub_techniques: []
id: ed23e106-7981-48a4-af7c-23e8fd2fa90b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-LinkedIn-Attacker-Account

## Summary

This procedure sets up a standard LinkedIn user account to serve as the attacker's profile for initiating messaging attacks, ensuring the messages appear legitimate.

## Description

In the context of exploiting LinkedIn's messaging API, creating a dedicated attacker account is essential to avoid linking the attack to the attacker's real profile. The account must pass LinkedIn's basic registration and verification to access the messaging features. This step occurs in a web browser and requires no special tools, but it establishes the foundation for sending manipulated messages.

## Requirements

1. Valid email address not previously associated with LinkedIn
2. Basic personal information for registration (name, location)
3. Internet access to LinkedIn's registration page

## Defense

Defensive measures and detection strategies:

- Monitor for bulk account creations from suspicious IPs
- Implement CAPTCHA or email verification delays for new signups
- Rate-limit messaging from newly created accounts

## Objectives

1. Gain access to LinkedIn's messaging interface
2. Establish a profile for social engineering victims to accept messages
3. Prepare for API interaction without account suspension

## Instructions

### Step 1: Register New Account

**Context**: Access LinkedIn's signup page and provide registration details to create the account.

No specific command; use the web interface:

1. Navigate to https://www.linkedin.com/signup
2. Enter name, email, password, and other required fields
3. Submit the form and confirm via email link

> Upon success, the account dashboard loads, confirming activation.

### Step 2: Verify Messaging Access

**Context**: Test the account by attempting to send a basic message to ensure full functionality.

No specific command; in the LinkedIn app:

1. Log in and navigate to Messages
2. Send a test message to a contact or connection

> Expected output: Message sent successfully without errors.

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
