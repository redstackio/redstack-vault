---
tags:
  - email-change
  - rocket-chat
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8900934c-8770-4bd9-806f-63cfcc3cfbc4
created_at: '2025-12-14T17:24:47.906Z'
updated_at: '2025-12-14T17:24:47.906Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Email-Change-in-Rocket.Chat

## Summary

This procedure triggers the email address change feature in Rocket.Chat, sending a verification link to the current email, which is key to the 2FA bypass attack.

## Description

Logged in as the account owner (or simulating via controlled account), navigate to settings to request an email update. Entering a new email address initiates a verification email to the old address. This flaw allows the link to serve as a backdoor. Prerequisites include an active session with 2FA enabled.

## Requirements

1. Logged-in Rocket.Chat session with 2FA active
2. Control over the current email for link receipt
3. New email address (attacker-controlled for full takeover)

## Defense

Defensive measures and detection strategies:

- Require 2FA confirmation for email changes
- Rate-limit email change requests
- Notify users via alternate channels for changes

## Objectives

1. Generate verification email with bypass link
2. Simulate victim interaction for attack chaining
3. Validate email delivery mechanism

## Instructions

### Step 1: Navigate to Email Settings

**Context**: Access the profile edit section.

Go to My Account > Profile > Email Address.

> Enter a new email and submit the change request.

### Step 2: Receive Verification Email

**Context**: Check the original email for the link.

Open the inbox associated with the current account email.

> Expected output: Email with subject like "Verify your new email" containing a unique verification URL.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-change]]
- [[rocket-chat]]
