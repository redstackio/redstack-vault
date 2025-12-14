---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - initial-access
  - web-auth
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
updated_at: '2025-12-14T05:32:10.300Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register-and-Login-to-MTN-Careers

## Summary

This procedure establishes initial authenticated access to the MTN Group careers website by registering a new user account and logging in, enabling access to the profile update section where the vulnerable file upload feature is located.

## Description

The MTN Careers website at https://careers.mtn.cm/ allows open registration without restrictions. Attackers can create an account using basic personal details, then log in to reach the user profile area. This step is prerequisite for exploiting the unvalidated file upload, as the upload feature requires authentication. Expected outcomes include a valid session token and navigation to the profile editing page, setting the stage for malicious file upload.

## Requirements

1. Internet access to https://careers.mtn.cm/
2. Web browser with form submission capabilities
3. Valid email address for registration verification (if required)

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration endpoints to prevent automated account creation
- Monitor for unusual registration patterns, such as multiple accounts from the same IP
- Require email/SMS verification for new accounts to reduce abuse

## Objectives

1. Create a new user account to gain legitimate access
2. Authenticate and access profile management features
3. Establish a session for subsequent upload actions

## Instructions

### Step 1: Navigate to Registration Page

**Context**: Access the main careers site and initiate account creation to obtain user credentials.

Visit https://careers.mtn.cm/ in your web browser and locate the registration link (typically under 'Join Us' or similar). Fill out the form with fabricated details such as name, email, and password.

### Step 2: Complete Registration and Verify

**Context**: Submit the registration form and handle any verification steps to activate the account.

Submit the form and check your email for a verification link if prompted. Click the link to confirm the account.

### Step 3: Log In to the Account

**Context**: Use the newly created credentials to authenticate and reach the profile section.

Return to the login page, enter your email and password, and submit. Upon success, navigate to the user profile or 'My Account' section to access update features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[initial-access]]
- [[web-auth]]
