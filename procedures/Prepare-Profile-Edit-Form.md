---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - profile-edit
  - email-manipulation
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
updated_at: '2025-12-14T17:33:06.613Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Prepare-Profile-Edit-Form

## Summary

This procedure prepares the profile edit form on the EditUserProfile endpoint by entering the attacker's password and modifying the email to the victim's, setting up for intercepted submission.

## Description

The vulnerability stems from no checks on email uniqueness or ownership during updates. By authenticating with the attacker's password but targeting the victim's email, the form submission can be intercepted to complete the overwrite. This step occurs after logging in as the attacker and assumes proxy interception is configured.

## Requirements

1. Active attacker session on EditUserProfile page
2. Knowledge of attacker's current password
3. Victim's email address

## Defense

Defensive measures and detection strategies:

- Validate email changes against ownership (e.g., session user ID match)
- Require secondary authentication for sensitive changes like email
- Log and alert on email update attempts

## Objectives

1. Authenticate the edit action with attacker's credentials
2. Stage email overwrite to victim's details
3. Position for request modification without submission

## Instructions

### Step 1: Access EditUserProfile

**Context**: Load the form using attacker's session to ensure authenticated access.

Navigate to https://target.com/user/EditUserProfile after logging in as attacker.

**Expected Output**: Form fields loaded with current attacker details.

### Step 2: Enter Password

**Context**: Provide authentication for the edit to bypass basic checks.

Fill the current password field with the attacker's password.

**Expected Output**: Password accepted for form validation.

### Step 3: Modify Email Field

**Context**: Change the email to victim's to initiate overwrite targeting.

Update the email input from attacker@gmail.com to victim@gmail.com.

**Expected Output**: Form reflects victim's email, ready for submission interception.

### Step 4: Intercept Submission

**Context**: Prevent initial submission to allow modification.

Click submit and forward the request to a proxy repeater without sending.

**Expected Output**: Intercepted HTTP POST request with form data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- profile-edit
- email-manipulation
