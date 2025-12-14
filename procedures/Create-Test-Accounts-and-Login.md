---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - account-creation
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:33:06.616Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Test-Accounts-and-Login

## Summary

This procedure sets up attacker and victim test accounts on a web platform to enable subsequent manipulation of profile data for account takeover exploitation.

## Description

In a web application vulnerable to improper authentication on profile edits, creating separate attacker and victim accounts allows testing of email and user ID overwrites. The attacker logs in to access the EditUserProfile endpoint, while the victim's details are targeted. This step requires no special tools beyond browser access but sets the foundation for interception.

## Requirements

1. Access to the target web application's registration page
2. Valid email addresses for registration (e.g., attacker@gmail.com, victim@gmail.com)
3. Basic knowledge of the platform's login flow

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account registrations
- Monitor for multiple registrations from similar IPs
- Require email verification during signup

## Objectives

1. Establish controlled attacker and victim environments
2. Obtain session access for profile editing
3. Prepare for request interception without alerting defenses

## Instructions

### Step 1: Register Attacker Account

**Context**: Create the attacker's account to gain legitimate access for later manipulation.

Navigate to the registration page and provide details such as username, email (attacker@gmail.com), and password. Submit the form to complete registration.

**Expected Output**: Confirmation email or success message with account creation.

### Step 2: Register Victim Account

**Context**: Simulate the victim's account to obtain its email and later discover its user ID.

Repeat the registration process with victim details (victim@gmail.com, choose a password). Note the victim's user ID if exposed in responses or via enumeration.

**Expected Output**: Victim account created successfully.

### Step 3: Login to Both Accounts

**Context**: Authenticate sessions to access protected endpoints.

Log in to the attacker account first, then the victim account in a separate session or incognito window. Navigate to https://target.com/user/EditUserProfile using the attacker's session.

**Expected Output**: Successful login and access to the profile edit page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- account-creation
- web
