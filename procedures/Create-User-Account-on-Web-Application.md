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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:41.708Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: ed7b2d29-671a-44d7-b5db-b35e9b038e0f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-User-Account-on-Web-Application

## Summary

This procedure outlines the process of registering a new user account on a target web application, providing the necessary access to authenticated features like the certificate upload section for subsequent exploitation.

## Description

In the context of exploiting web vulnerabilities, creating a legitimate user account is often a prerequisite to access protected areas. This procedure targets the basic info registration form, typically found at endpoints like /app/registration/basic-info. It assumes the application allows open registration without additional verification. Successful execution grants login credentials for further actions, such as uploading files in authenticated sessions.

## Requirements

1. Web browser with JavaScript enabled
2. Valid email address for registration (if verification is required, though not in this case)
3. Access to the public registration endpoint

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification on registration to prevent automated account creation
- Rate-limit registration attempts to detect abuse
- Monitor for unusual registration patterns from new IP addresses

## Objectives

1. Obtain valid user credentials for authenticated access
2. Enable navigation to vulnerable features like certificate uploads
3. Establish a foothold for exploitation without alerting defenses

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the registration page to begin the account creation process.

Open a web browser and go to the registration endpoint, such as https://target.com/app/registration/basic-info.

### Step 2: Fill and Submit Form

**Context**: Provide required information to complete registration.

Enter details like name, email, and password into the basic info form. Ensure the password meets any complexity requirements. Click submit to create the account.

**Expected Output**: Confirmation message or redirection to login/dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[initial-access]]
