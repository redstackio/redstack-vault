---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - registration
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:33:12.275Z'
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
# Register-Account-on-Target-Web-Application

## Summary

This procedure creates a new user account on the target web application, providing initial authenticated access necessary for subsequent exploitation steps.

## Description

In the context of exploiting an IDOR vulnerability in a DoD web application, registration establishes a legitimate user session. The target is a public-facing registration endpoint at https://█████████/signIn/CreateAccount.html. No special privileges are required, but the application must allow open registration. Expected outcome is a functional account that can be used to access profile features.

## Requirements

1. Internet access to the target URL
2. Valid email address for registration
3. Basic browser or HTTP client

## Defense

Defensive measures and detection strategies:

- Rate limiting on registration attempts
- CAPTCHA on signup forms
- Email verification for new accounts

## Objectives

1. Gain authenticated access to the application
2. Establish a baseline user session
3. Prepare for profile manipulation

## Instructions

### Step 1: Access Registration Page

**Context**: Navigate to the signup endpoint to begin account creation.

No specific command; use a browser to visit https://█████████/signIn/CreateAccount.html and fill in the form with desired username, email, and password.

> Submit the form to receive a success response or confirmation.

### Step 2: Verify Registration

**Context**: Confirm the account is active by attempting login.

Use the login page at https://██████████/signIn/signIn.html with the new credentials.

> Expected output: Redirect to dashboard or success message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- registration
- web-app
