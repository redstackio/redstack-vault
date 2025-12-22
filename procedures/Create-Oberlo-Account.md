---
id: proc-create-oberlo-account
tags:
  - account-creation
  - initial-access
  - oberlo
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:47:18.240Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Oberlo-Account

## Summary

This procedure outlines the creation of a new user account on the Oberlo platform, which is a prerequisite for accessing and exploiting features like profile editing in a stored XSS attack.

## Description

In the context of exploiting a stored XSS vulnerability, creating an account allows the attacker to authenticate and reach the vulnerable profile name field. Oberlo, integrated with Shopify, permits free registration without strict verification, making this step straightforward. The procedure assumes no prior access and uses standard web registration flows. Expected outcomes include a functional account that can be used to inject payloads.

## Requirements

1. Valid email address for registration
2. Web browser with JavaScript enabled
3. Internet access to https://app.oberlo.com

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification to limit automated account creation
- Monitor for rapid account registrations from suspicious IPs
- Rate-limit registration attempts

## Objectives

1. Gain authenticated access to the Oberlo dashboard
2. Enable profile modification capabilities
3. Set up for subsequent XSS injection

## Instructions

### Step 1: Navigate to Registration Page

**Context**: Access the Oberlo signup form to begin account creation.

Visit https://app.oberlo.com/auth/signup in your web browser.

> This loads the registration interface where email and password can be entered.

### Step 2: Enter Registration Details

**Context**: Provide necessary information to create the account.

Fill in the email field with a valid address, choose a password, and submit the form.

> Upon submission, Oberlo sends a confirmation email; check and verify if required.

### Step 3: Complete Login

**Context**: Authenticate the new account to access the dashboard.

After verification, log in at https://app.oberlo.com/auth/login.

> Successful login redirects to the main dashboard, confirming account creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[initial-access]]
- [[oberlo]]
