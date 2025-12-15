---
tags:
  - account-creation
  - setup
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:12.358Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: cac6b0cf-5d90-4709-b1eb-60a0b64b5742
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Create-and-Verify-Test-Accounts

## Summary

This procedure establishes attacker and victim test accounts on the target web application to facilitate subsequent IDOR exploitation by providing necessary user identifiers and verifying the registration flow.

## Description

In the context of testing for IDOR vulnerabilities in user profile management, creating verified accounts simulates real users and allows observation of user ID assignment patterns, which are often sequential numerics. This step ensures the environment is set up correctly before proceeding to request interception and modification. Expected outcomes include active accounts with access to profile update endpoints.

## Requirements

1. Access to two unique email addresses for registration
2. Internet connectivity to the target site (mtnmobad.mtnbusiness.com.ng)
3. Web browser for account creation

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on account registrations to prevent abuse
- Monitor for multiple registrations from similar IP addresses
- Require CAPTCHA on registration forms

## Objectives

1. Create functional attacker and victim accounts
2. Verify email addresses to activate accounts
3. Confirm access to profile management features

## Instructions

### Step 1: Register Attacker Account

**Context**: Begin by creating the primary account for the attacker to use in request capture.

Navigate to the registration page on mtnmobad.mtnbusiness.com.ng, provide details including a unique email, and submit the form. Check the email inbox for the verification link and click it to activate the account.

### Step 2: Register Victim Account

**Context**: Create a secondary account to simulate the target for exploitation.

Repeat the registration process with a different email address. Verify the email as before to ensure the account is active and can access profile updates.

### Step 3: Test Login

**Context**: Validate that both accounts can log in successfully.

Log in to each account separately to confirm access to the dashboard and profile update section.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-creation]]
- [[setup]]
