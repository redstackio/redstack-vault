---
tags:
  - account-creation
  - takeover
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
updated_at: '2025-12-14T17:32:58.377Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: ea42276b-0cfd-4d8d-b610-24f439a22269
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Complete Duplicate Account Creation on Reddit

## Summary

This procedure finalizes the creation of a duplicate Reddit account using an email already linked via OAuth, confirming the vulnerability and enabling scenarios where an attacker can takeover a victim's intended account.

## Description

Building on the registration attempt, submitting the form creates a new account without detecting the existing OAuth association. This results in two accounts sharing the same email, allowing the attacker to claim control before the legitimate user. The impact includes unauthorized access if the victim tries to register or log in later. Performed via standard web form submission.

## Requirements

1. Partially filled registration form from prior step
2. Valid new credentials
3. No active conflicting session

## Defense

Defensive measures and detection strategies:

- Implement backend checks for email conflicts across all account creation paths
- Automatically merge or block duplicates upon detection
- Alert on multiple accounts per email and require verification

## Objectives

1. Successfully create the duplicate account
2. Demonstrate account takeover potential
3. Gain control over email-linked identity

## Instructions

### Step 1: Review Form Details

**Context**: Ensure all fields are correctly filled for submission.

Double-check username, password, and email in the registration form.

> This prevents unrelated errors during submission.

### Step 2: Submit Registration

**Context**: Trigger account creation.

Click the "Sign Up" or equivalent submit button.

> Expected output: Success message and redirect to account setup or dashboard.

### Step 3: Verify Duplicate Creation

**Context**: Confirm the new account exists independently.

Log in with the new credentials to access the duplicate account.

> Expected output: Access granted without issues, proving duplicate functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- account-duplication
- takeover
- oauth-exploit
