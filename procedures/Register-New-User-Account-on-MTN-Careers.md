---
tags:
  - registration
  - initial-access
  - web
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
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:23:27.944Z'
sub_techniques: []
id: f8540507-77c1-49de-b816-015e34ca66b6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Register-New-User-Account-on-MTN-Careers

## Summary

This procedure outlines the steps to create a new user account on the MTN Group careers website, providing initial access to authenticated features like profile updates.

## Description

In the context of exploiting web vulnerabilities, registering a new account is the entry point to access user-specific functionalities such as file uploads. The target is https://careers.mtn.cm/, a PHP-based web application without restrictions on account creation. Successful registration grants a session for further actions, leading to potential exploitation of upload features.

## Requirements

1. Web browser with internet access
2. Valid email address for verification (if required)
3. Basic user details (name, password)

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on registration to prevent automated sign-ups
- Rate-limit registration attempts to detect abuse
- Monitor for unusual registration patterns from single IPs

## Objectives

1. Gain authenticated access to the application
2. Enable navigation to profile management areas
3. Set up for subsequent exploitation steps

## Instructions

### Step 1: Navigate to Registration Page

**Context**: Access the site's registration form to begin account creation.

Visit https://careers.mtn.cm/ and locate the 'Register' or 'Sign Up' link, typically in the top navigation or footer.

### Step 2: Fill Registration Form

**Context**: Provide necessary details to complete account setup.

Enter required fields: full name, email address, password, and any other prompted information. Submit the form.

### Step 3: Verify Account if Needed

**Context**: Confirm the account via email or on-site validation.

Check email for verification link and click it, or follow any on-screen prompts to activate the account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- registration
- initial-access
