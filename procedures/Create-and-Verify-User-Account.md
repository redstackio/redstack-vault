---
tags:
  - authentication
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:39:10.051Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bf1c3c1d-4cf1-414a-95d5-2e2f345f0f04
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-and-Verify-User-Account

## Summary

This procedure establishes authenticated access to the target web application by creating a new user account and completing email verification, a prerequisite for accessing protected features like product creation and LRS configurations.

## Description

In the context of exploiting SSRF in an AWS-hosted web app, user registration is open and requires only basic details and email verification. This allows attackers to gain legitimate access without prior credentials. The process targets applications using self-service signup, common in SaaS products. Expected outcomes include dashboard access, enabling subsequent steps in the attack chain.

## Requirements

1. Valid email address (Gmail recommended for reliable verification)
2. Web browser with access to https://█████
3. No existing account on the target

## Defense

Defensive measures and detection strategies:

- Implement CAPTCHA on registration to prevent automated signups
- Rate-limit registration attempts and monitor for bulk account creation
- Log and alert on verification email patterns from disposable providers

## Objectives

1. Obtain authenticated session for feature access
2. Verify account to unlock full application functionality
3. Establish foothold for vulnerability exploitation

## Instructions

### Step 1: Register New User

**Context**: Fill out the account creation form to initiate registration.

Navigate to https://█████/users/create and provide required details such as username, email, and password.

**Expected Output**: Form submission success; verification email sent.

### Step 2: Verify Email and Login

**Context**: Complete verification to activate the account and log in.

Check your email for the verification code or link. If not received, try a Gmail address. Click the link or enter the code, then log in with the new credentials.

**Expected Output**: Redirect to dashboard upon successful login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- initial-access
