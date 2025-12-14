---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - cloudflare
  - account-creation
  - unverified-account
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
updated_at: '2025-12-14T17:24:48.127Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Create-Unverified-Cloudflare-Account-with-Target-Email

## Summary

This procedure allows an attacker to create a Cloudflare account using a target user's email address without completing email verification, establishing initial control over the account tied to the target's identity.

## Description

In the context of Cloudflare's authentication system, the signup process does not enforce immediate email verification, allowing arbitrary email addresses to be used for account creation. This leads to the attacker gaining access to an unverified account dashboard. The procedure targets web-based signup interfaces and requires only basic form submission. Expected outcomes include dashboard access and the ability to perform further actions like enabling 2FA.

## Requirements

1. Web browser with internet access
2. Knowledge of the target's email address
3. No prior Cloudflare credentials

## Defense

Defensive measures and detection strategies:

- Implement mandatory email verification during signup with time-bound links
- Monitor for multiple account creations using the same email and flag suspicious activity
- Use rate limiting on signup attempts per email

## Objectives

1. Gain initial access to a Cloudflare account using the target's email
2. Bypass verification to reach the dashboard
3. Set up for subsequent account manipulation

## Instructions

### Step 1: Navigate to Signup Page

**Context**: Access the Cloudflare registration form to begin account creation.

Navigate to https://dash.cloudflare.com/sign-up in a web browser.

> This loads the signup interface where email and other details can be entered.

### Step 2: Submit Signup Form

**Context**: Enter the target's email and complete the form without verification.

Fill in the form with the target's email address, a chosen username, and temporary password. Submit the form and ignore or skip any verification prompts if not enforced.

> Upon submission, the system creates the account and grants dashboard access without requiring email confirmation, allowing immediate login.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[cloudflare]]
- [[account-creation]]
- [[unverified-account]]
