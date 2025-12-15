---
tags:
  - password-reset
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ea4c62f0-57c7-4f45-b91e-a9d82de87e3f
created_at: '2025-12-14T17:33:06.125Z'
updated_at: '2025-12-14T17:33:06.125Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request-Password-Reset-Link-Without-Using-It

## Summary

This procedure initiates a password reset on a Twitter account to generate a reset link sent to the initial email, which is preserved for later use in the exploit chain.

## Description

Targeting the password reset functionality, this step logs out and requests a reset for the account tied to abcd@x.com, receiving a time-limited link via email. The link is not actioned immediately, allowing it to persist during subsequent email changes. This exploits the lack of token invalidation.

## Requirements

1. Active Twitter account with email abcd@x.com
2. Access to abcd@x.com inbox
3. Web browser

## Defense

Defensive measures and detection strategies:

- Rate-limit reset requests per account
- Log and alert on repeated resets from same IP

## Objectives

1. Obtain a valid reset token
2. Ensure link delivery to old email
3. Set up for post-update exploitation

## Instructions

### Step 1: Log Out and Initiate Reset

**Context**: Start the reset flow to trigger email delivery.

Log out of the account, go to https://twitter.com/login, and click 'Forgot password?'. Enter the username or email abcd@x.com.

> Twitter sends a reset email with a unique link.

### Step 2: Receive and Store Link

**Context**: Capture the link without activation.

Open abcd@x.com and note the reset link from the email, but do not click it.

> The link remains valid for approximately 1 hour.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[twitter]]
