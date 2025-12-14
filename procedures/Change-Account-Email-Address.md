---
tags:
  - account-manipulation
  - persistence
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:33:24.566Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 2c1cd3b7-ec2a-4abc-84b2-45ae188b465c
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Change-Account-Email-Address

## Summary

This procedure details logging into an Imgur account and updating the email address, which in the vulnerable state does not invalidate prior password reset links, facilitating takeover.

## Description

With temporary access to the Imgur account, the attacker navigates to settings to change the primary email to one under their control. This step simulates a victim attempting to secure their account by updating contact info, but due to the flaw, it leaves old reset tokens active. The process involves verification via the new email. Target is Imgur's account settings page. Prerequisites: Valid login credentials. Outcome: Email changed, but vulnerability exposed for next steps.

## Requirements

1. Active login session to the target Imgur account
2. Control over a new email address for verification
3. Web browser access to https://imgur.com

## Defense

Defensive measures and detection strategies:

- Automatically invalidate all pending reset tokens on email updates
- Require re-authentication for sensitive changes like email
- Log and alert on email changes post-reset requests

## Objectives

1. Update account contact info to attacker-controlled email
2. Trigger verification without disrupting old tokens
3. Prepare for exploitation of stale reset links

## Instructions

### Step 1: Access Account Settings

**Context**: Log in and reach the settings area to locate email options.

Go to https://imgur.com/signin, log in with current credentials. Click the profile icon and select 'Account settings'.

> Expected output: Settings dashboard loaded, showing sections like Account Overview.

### Step 2: Update and Verify Email

**Context**: Change the email and complete verification to make it active.

In the 'Email and Password' section, enter a new email address. Submit and check the new inbox for Imgur's verification email. Click the confirmation link in that email.

> Expected output: Success message confirming email update. Old reset links remain valid due to the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-manipulation]]
- [[Persistence]]
