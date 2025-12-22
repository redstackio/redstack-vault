---
id: proc-register-invalid-email
tags:
  - account-creation
  - web-access
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:55:20.752Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Register-Account-with-Invalid-Email

## Summary

This procedure creates a new user account on the target website using an invalid email address controlled by the attacker's SMTP server, setting the stage for email validation exploitation.

## Description

Targeted at web applications with email validation features, such as www.xvideos.com, this involves navigating to the registration page and submitting form data with 'invalid@example.org' as the email. The site accepts the registration without immediate validation, allowing later triggering of SMTP interactions that deliver the XSS payload via error messages.

## Requirements

1. Access to the target website (www.xvideos.com) via a modern browser
2. No special credentials; public registration endpoint
3. Configured SMTP server from prior procedure

## Defense

Defensive measures and detection strategies:

- Validate email formats and domains during registration
- Rate-limit account creations to prevent abuse
- Log and monitor registrations with suspicious emails

## Objectives

1. Primary objective: Gain initial foothold via account creation
2. Secondary objective: Use invalid email to route validation through controlled SMTP
3. Expected outcome: Account created with pending email validation

## Instructions

### Step 1: Access Registration Page

**Context**: Navigate to the site's homepage and initiate registration.

**Instructions**: Open www.xvideos.com in a browser and click the 'Join for FREE' button.

**Expected Output**: Registration form loads.

### Step 2: Submit Registration Form

**Context**: Fill in required fields using the invalid email.

**Instructions**: Enter username, password, and set email to 'invalid@example.org'; submit the form.

**Expected Output**: Account confirmation; redirect to dashboard with unvalidated email notice.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-creation
- web-access
