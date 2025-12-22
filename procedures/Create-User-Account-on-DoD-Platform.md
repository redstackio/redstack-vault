---
tags:
  - account-creation
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
techniques:
  - '[[External Remote Services]]'
sub_techniques: []
id: 78214ea0-68f1-4db6-b311-f3b55d634ecb
created_at: '2025-12-14T17:25:34.291Z'
updated_at: '2025-12-14T17:25:34.291Z'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create-User-Account-on-DoD-Platform

## Summary

This procedure outlines the creation of a new user account on the U.S. Department of Defense's JOINOnline platform, serving as the initial access point for exploiting subsequent vulnerabilities like IDOR in profile management.

## Description

The DoD's online registration system allows public signup for users interested in military joining processes. By creating an account, an attacker gains authenticated access to user-specific endpoints. This step is prerequisite for accessing profile update features where the IDOR vulnerability resides. The target environment is a web application over HTTPS, with no advanced authentication beyond email verification. Expected outcomes include a valid session and an assigned numeric user ID.

## Requirements

1. Internet access and a web browser
2. A valid email address for verification
3. Basic personal details (name, etc.) to complete registration

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or rate limiting on registration endpoints to prevent bulk account creation
- Monitor for anomalous signup patterns from suspicious IPs
- Require additional verification (e.g., phone) for sensitive platforms

## Objectives

1. Gain initial authenticated access to the platform
2. Obtain a numeric user ID for use in subsequent exploitation
3. Establish a baseline for testing access controls

## Instructions

### Step 1: Navigate to Registration Page

**Context**: Access the public registration endpoint to begin the signup process.

Open a web browser and visit the registration URL: https://www.█████████/ (censored DoD domain). Fill in the required fields including name, email, and other details.

> Submit the form to trigger email verification. Check your inbox for the confirmation link.

### Step 2: Verify and Log In

**Context**: Complete verification to activate the account and log in.

Click the verification link in the email, then log in with the new credentials. Upon successful login, note the dashboard URL which may reveal initial user ID patterns.

> Expected output: Redirect to user dashboard with session established.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[External Remote Services]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[initial-access]]
