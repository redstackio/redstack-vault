---
tags:
  - account-creation
  - weblate
  - django
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
updated_at: '2025-12-14T17:31:19.719Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
id: f15501cf-2774-4c6d-88c5-7c5cc26ecf07
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-and-Verify-Weblate-Account

## Summary

This procedure outlines the creation of a new user account on a Weblate instance and verification via email, serving as the initial setup for testing authentication vulnerabilities.

## Description

In the context of demonstrating the password reset token reuse vulnerability, this procedure establishes a legitimate account on the target Weblate application (built on Python/Django). It involves navigating to the registration page, providing user details, and confirming ownership through an emailed link. This step ensures the account is active before proceeding to exploit the flawed token handling. Expected outcomes include a fully verified account ready for login and further manipulation.

## Requirements

1. Web browser with access to the Weblate instance (e.g., https://demo.weblate.org)
2. Valid email address for confirmation
3. No prior authentication needed

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on registration to prevent automated account creation
- Monitor for unusual registration spikes from single IPs
- Log and alert on email confirmation patterns

## Objectives

1. Establish a test account for vulnerability reproduction
2. Verify email integration for reset token delivery
3. Prepare for authentication testing

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the account creation page to input new user details.

Navigate to `https://demo.weblate.org/accounts/profile/` and select the registration option. Fill in the username, email, and initial password.

> Submit the form to trigger email confirmation.

### Step 2: Confirm Email

**Context**: Validate the account by following the confirmation link.

Check the registered email for the confirmation message from Weblate. Click the provided link to activate the account.

> Upon success, the account is verified, and login is possible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- weblate
- registration
