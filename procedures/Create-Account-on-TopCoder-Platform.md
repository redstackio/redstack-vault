---
tags:
  - account-creation
  - initial-access
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
id: 9e65c552-9e9d-4017-bad1-63e311e7753c
created_at: '2025-12-13T23:52:39.173Z'
updated_at: '2025-12-13T23:52:39.173Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Account-on-TopCoder-Platform

## Summary

This procedure outlines the creation of a new user account on the TopCoder platform to gain access to its Atlassian Confluence wiki, serving as the initial access vector for testing vulnerabilities like reflected XSS in the labels feature.

## Description

The TopCoder platform allows free registration, providing immediate access to wiki functionalities upon verification. This step is essential for authenticated testing of endpoints like /wiki/labels/, where unauthenticated access may be restricted. The process involves standard web form submission and email verification, with no advanced technical skills required. Expected outcomes include a functional session token for further interactions.

## Requirements

1. Valid email address for registration and verification
2. Web browser with JavaScript enabled
3. Internet access to https://apps.topcoder.com

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration endpoints to prevent automated account creation
- Monitor for unusual registration spikes from single IP addresses
- Require email domain whitelisting for high-risk environments

## Objectives

1. Establish authenticated access to the Confluence wiki
2. Obtain a session for testing protected endpoints
3. Validate user privileges for wiki interactions

## Instructions

### Step 1: Navigate to Registration Page

**Context**: Access the platform's signup form to begin account creation.

Visit https://apps.topcoder.com in your web browser and click on the 'Sign Up' or 'Register' link, typically found in the top navigation bar.

> This loads the registration form; ensure no ad blockers interfere with form submission.

### Step 2: Submit Registration Details

**Context**: Provide necessary user information to create the account.

Fill in the form with a username, email address, password, and any required fields like full name. Submit the form and check your email for a verification link.

> Upon submission, expect a success message or redirect; click the verification link in the email to activate the account.

### Step 3: Login and Verify Wiki Access

**Context**: Confirm the account grants access to the target wiki endpoint.

Log in using the new credentials and navigate to https://apps.topcoder.com/wiki to ensure the Confluence interface is accessible.

> Successful login shows the dashboard; attempt to access /wiki/labels/ to confirm permissions.

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
