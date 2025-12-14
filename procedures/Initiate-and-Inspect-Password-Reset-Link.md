---
id: proc-001
tags:
  - password-reset
  - link-inspection
  - broken-auth
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.447Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-and-Inspect-Password-Reset-Link

## Summary

This procedure initiates a password reset for an Instagram Brand account and inspects the received email link to confirm the use of HTTP scheme, exposing the security token for potential interception.

## Description

In the Instagram Brand platform, password reset links are sent via email using Mandrillapp, but they employ HTTP instead of HTTPS. By requesting a reset and examining the link, attackers can identify the vulnerable transmission of the token parameter. This step sets up the attack by revealing the insecure link structure without requiring network interception yet. Prerequisites include access to a target email and basic web navigation.

## Requirements

1. Valid email address linked to an Instagram Brand account
2. Web browser for accessing the sign-in page
3. Email client to receive and inspect the reset email

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS-only links in all email communications
- Monitor for anomalous password reset requests from unusual IPs
- Implement token expiration and one-time-use validation

## Objectives

1. Trigger and receive the password reset email
2. Extract and analyze the link to observe HTTP scheme and token
3. Prepare for subsequent interception

## Instructions

### Step 1: Request Password Reset

**Context**: Access the Instagram Brand registration/sign-in page to initiate the reset process for the target email.

No command required; use browser to navigate to `https://en.instagram-brand.com/register/signin`, click 'Forgot Password', and enter the target email.

> Expected: Confirmation email sent.

### Step 2: Inspect Email Link

**Context**: Open the received email, copy the hyperlink, and paste it into a text editor like Notepad to view the raw URL.

No command required; right-click the link in the email client, copy, and paste.

> Expected Output: URL like `http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<security token>`, confirming HTTP and token visibility.

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
- [[link-inspection]]
- [[broken-auth]]
