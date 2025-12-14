---
tags:
  - web-access
  - account-creation
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
updated_at: '2025-12-14T03:16:02.473Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 225c8f7b-35bc-4220-acce-43144d4d13c6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-DoD-Support-Form

## Summary

This procedure outlines creating an account and navigating to the vulnerable support request form in the U.S. Department of Defense web application, enabling access to the arbitrary file upload functionality.

## Description

The DoD web application allows user registration without restrictions, followed by navigation to IT support sections. This step is prerequisite for exploiting the file upload vulnerability, as it positions the attacker to reach the unprotected form. Expected outcomes include form access, setting the stage for malicious uploads that could lead to RCE or XSS.

## Requirements

1. Web browser with JavaScript enabled
2. Internet access to the redacted DoD application URL
3. Basic user details for registration (e.g., email, name)

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA or email verification for account creation
- Monitor for anomalous navigation patterns to support forms
- Rate-limit form accesses from new accounts

## Objectives

1. Successfully register and authenticate a user account
2. Reach the support request form with file upload capability
3. Confirm no access controls block progression

## Instructions

### Step 1: Register New Account

**Context**: Create a legitimate-looking account to blend in and gain authenticated access.

Navigate to the redacted URL in your browser. Click the registration link, fill in fields such as username, email, and password, then submit.

> Upon success, you will receive a confirmation or be redirected to the login page.

### Step 2: Log In and Navigate to Support

**Context**: Authenticate and proceed to the vulnerable section.

Enter your credentials on the login page and submit. Once logged in, locate and click the "Faculty/Staff IT Support" link. Then select the redacted support option to load the request form.

> The form should display fields including a file attachment option without type restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-access]]
- [[account-creation]]
