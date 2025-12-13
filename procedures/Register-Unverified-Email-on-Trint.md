---
tags:
  - email-registration
  - auth-bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: c0f2bf79-94dd-4b74-aee5-abf8dd57def9
created_at: '2025-12-13T09:01:26.372Z'
updated_at: '2025-12-13T09:01:26.372Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Register Unverified Email on Trint

## Summary

This procedure involves registering an account on app.trint.com using an organization domain email without any verification, enabling initial access for further exploitation.

## Description

The lack of email verification allows attackers to claim emails like support+1@trint.com, which match the organization's domain, setting the stage for SSO bypass. This targets web-based registration forms and requires no special tools.

## Requirements

1. Access to app.trint.com registration page
2. Ability to provide a custom email address
3. No prior credentials needed

## Defense

Defensive measures and detection strategies:

- Implement email verification during registration
- Monitor for suspicious registrations with plus-addressing

## Objectives

1. Gain initial account access
2. Claim organization domain email
3. Prepare for token retrieval

## Instructions

### Step 1: Navigate to Registration

**Context**: Access the Trint registration form.

Browse to https://app.trint.com/ and initiate the signup process.

> This sets up the unverified account.

### Step 2: Submit Registration

**Context**: Enter the target email and complete signup.

Provide email support+1@trint.com and any required details, then submit.

> No verification email is sent, granting immediate access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[email-registration]]
- [[auth-bypass]]
