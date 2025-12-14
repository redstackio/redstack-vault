---
tags:
  - account-creation
  - setup
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
updated_at: '2025-12-14T17:31:19.257Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e24b60a7-5b4d-4c41-8084-b99ac5e5df9f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-HackerOne-Account

## Summary

This procedure sets up a new HackerOne account using a controlled email address, serving as the initial step to prepare for exploiting the password reset vulnerability.

## Description

In the context of testing HackerOne's authentication flaws, creating an account with a specific email (e.g., a@x.com) allows subsequent steps like requesting reset tokens. This manual web-based action requires no tools and assumes access to the target platform. Expected outcome is a fully registered account ready for further manipulation.

## Requirements

1. Web browser with internet access
2. Control over an email address (e.g., a@x.com) for registration
3. Basic knowledge of web form submission

## Defense

Defensive measures and detection strategies:

- Monitor for rapid account creations from suspicious IPs
- Implement CAPTCHA on registration to deter automation
- Log all registration attempts for anomaly detection

## Objectives

1. Establish a baseline account for vulnerability testing
2. Ensure email verification is completed
3. Prepare for password reset exploitation

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the HackerOne signup page to begin account creation.

**Instructions**: Open a web browser and go to https://hackerone.com/signup. Fill in the required fields including username, password, and email a@x.com.

> Submit the form to trigger email confirmation.

### Step 2: Verify Email

**Context**: Complete the registration by confirming the email.

**Instructions**: Check the inbox of a@x.com for the verification email and click the confirmation link.

> Upon success, the account is active and accessible via login.

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
- [[setup]]
