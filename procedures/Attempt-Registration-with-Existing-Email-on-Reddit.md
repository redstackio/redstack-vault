---
tags:
  - registration
  - email-duplicate
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
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:58.378Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: d474addb-54f5-4db2-a605-6974514871ff
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Attempt Registration with Existing Email on Reddit

## Summary

This procedure tests Reddit's registration endpoint by submitting an email already associated via OAuth, revealing the absence of conflict detection and allowing progression to duplicate account creation.

## Description

Navigating to the registration page at https://accounts.reddit.com/account/register/, this step enters the previously used email along with a new username and password. The system's failure to check for existing OAuth-linked emails permits the form to proceed, exposing the misconfiguration. Manual web interaction required.

## Requirements

1. Email from prior OAuth step
2. New username and password for the duplicate account
3. Web browser

## Defense

Defensive measures and detection strategies:

- Enforce cross-flow email validation (OAuth vs. direct registration)
- Flag and block registrations with emails linked to existing OAuth accounts
- Log registration attempts with known emails for anomaly detection

## Objectives

1. Submit registration with duplicate email
2. Bypass uniqueness checks
3. Advance to account creation

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the signup form.

Go to https://accounts.reddit.com/account/register/ in your browser.

> This displays the registration form fields.

### Step 2: Enter Duplicate Email

**Context**: Input the email to test conflict detection.

Fill in the email field with the exact email used in the OAuth login.

> Expected output: No immediate error; field accepts the input.

### Step 3: Provide Additional Details

**Context**: Complete form to trigger submission.

Enter a new username, password, and any other required fields, then proceed.

> Expected output: Form advances without duplicate email rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- registration
- duplicate-email
- auth-bypass
