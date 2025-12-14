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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.431Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c4a84abb-f906-4114-9a1f-2155919ccffd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Secret-Account

## Summary

This procedure outlines the standard process for registering a new account on the Secret web application, serving as the initial step in testing authentication vulnerabilities.

## Description

In the context of exploiting broken authentication, creating an account allows an attacker to set up a controlled environment for testing password reset behaviors. The target is the Secret app's registration endpoint, typically over HTTPS. Expected outcome is a fully functional account tied to an attacker-controlled email, enabling subsequent manipulation without alerting the real user.

## Requirements

1. Web browser with access to the Secret app URL
2. Valid email address for registration (e.g., a@email.com)
3. No prior account on the target application

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account creation to prevent abuse
- Require CAPTCHA on registration to deter automated signups
- Monitor for unusual registration patterns from single IPs

## Objectives

1. Gain initial access to the application via a new account
2. Establish email control for reset link receipt
3. Prepare for email change testing

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the signup page to begin account creation.

Open a web browser and go to the Secret application's registration page (e.g., https://secret.app/register).

> Fill in the required fields: username, email (a@email.com), and initial password. Submit the form.

### Step 2: Verify Email

**Context**: Complete any email verification to activate the account.

Check the email inbox for a verification link from Secret and click it to confirm.

> Upon success, log in to the account dashboard to confirm activation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[initial-access]]
