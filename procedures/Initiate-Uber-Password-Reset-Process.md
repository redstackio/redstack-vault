---
tags:
  - xss
  - self-xss
  - password-reset
  - uber
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
id: 0c4936f8-a4e5-4cd1-a835-144d4ac91134
created_at: '2025-12-14T03:15:26.598Z'
updated_at: '2025-12-14T03:15:26.598Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Initiate-Uber-Password-Reset-Process

## Summary

This procedure outlines the steps to start the Uber password reset process, which is the entry point for exploiting the reflected Self-XSS vulnerability in the new password field on partners.uber.com.

## Description

In the context of testing for Self-XSS in Uber's authentication flow, this procedure involves navigating to the forgot password page, submitting an email request, and following the emailed link to reach the vulnerable reset form. It requires a valid Uber account but no elevated privileges. The outcome is access to the unsanitized input field where the payload will be injected. This step is low-risk and mimics legitimate user behavior.

## Requirements

1. Web browser with JavaScript enabled
2. Valid email address associated with an Uber account
3. Access to the email inbox for receiving the reset link

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on password reset requests to prevent abuse
- Monitor for unusual patterns in reset link clicks from automated tools
- Use CAPTCHA on forgot password forms to deter scripted access

## Objectives

1. Gain access to the password reset form on partners.uber.com
2. Prepare for payload injection in the subsequent step
3. Validate the reset flow is active and reachable

## Instructions

### Step 1: Navigate to Forgot Password Page

**Context**: Begin the reset process by accessing Uber's login portal.

Navigate to https://login.uber.com/forgot-password in your web browser.

> This loads the form for entering an email to initiate the reset.

### Step 2: Submit Email Request

**Context**: Request the reset link by providing account credentials.

Enter your Uber account email address in the provided field and click the submit button.

> An email with a unique reset link will be sent to the provided address.

### Step 3: Follow Reset Link

**Context**: Access the vulnerable reset page via the email.

Check your email inbox, locate the password reset email from Uber, and click the embedded link.

> This redirects to https://partners.uber.com/reset-password, displaying the new password form.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- self-xss
- uber
