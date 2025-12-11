---
tags:
  - password-reset
  - mattermost
type: procedure
tools:
  - '[[tools/Chrome]]'
  - '[[tools/Sublime-Text]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: f9bcc195-617a-4c7a-a3f6-6a6eb4531898
created_at: '2025-12-11T06:10:15.822Z'
updated_at: '2025-12-11T06:10:15.822Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Initiate Password Reset Request

## Summary

This procedure triggers the password reset process in Mattermost by navigating to the reset page and submitting the registered email, leading to the generation of a reset link.

## Description

Accessing the password reset functionality tests for insecure handling of sensitive links. The target is a Mattermost cloud instance, and success is indicated by the system sending a reset email. No commands are executed; it's browser-based.

## Requirements

1. Existing Mattermost account
2. Access to the reset URL: https://h1-*your-own-instance*.cloud.mattermost.com/reset_password
3. Web browser like [[tools/Chrome]]

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS for all sensitive links
- Monitor reset request rates to detect abuse

## Objectives

1. Trigger email with reset link
2. Test for transport security issues
3. Simulate user forgetfulness scenario

## Instructions

### Step 1: Navigate to Reset Page

**Context**: Open the password reset URL in the browser.

Use [[tools/Chrome]] to access https://h1-*your-own-instance*.cloud.mattermost.com/reset_password.

> Expected: Reset form loads.

### Step 2: Submit Email

**Context**: Enter the registered email and submit.

Fill in the email field and click submit to initiate the reset.

> Expected: Confirmation message and email dispatch.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Chrome]]

## Tags

- password-reset
- mattermost
