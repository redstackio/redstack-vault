---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - web-vuln
  - registration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.085Z'
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
# Register-User-Account-to-Trigger-Verification-Email

## Summary

This procedure initiates the user registration on a vulnerable web application like Zomato to generate a verification email containing an exploitable non-expiring link with sensitive data in the URL.

## Description

In the context of Zomato's registration flow, entering basic details triggers an email with a 'Verify Email Address' link. The link's 'fbcid' parameter is Base64-encoded and includes sensitive info. This step sets up the attack by obtaining the link, which does not expire post-activation, enabling auth bypass.

## Requirements

1. Access to the target web app (e.g., zomato.com)
2. A valid email address (attacker-controlled or victim's)
3. Standard web browser

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration
- Monitor for unusual registration patterns from single IPs
- Expire verification links immediately after use

## Objectives

1. Generate the verification email and link
2. Obtain the URL with 'fbcid' parameter
3. Prepare for subsequent exploitation steps

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the registration endpoint to begin the process.

Navigate to https://www.zomato.com/register or equivalent in a web browser.

> This loads the form for user input.

### Step 2: Submit Registration Details

**Context**: Provide required fields to trigger email sending.

Enter full name, email address, and password. Click 'Register' or submit.

> Email is sent with the verification link; check inbox for delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-vuln]]
- [[registration]]
