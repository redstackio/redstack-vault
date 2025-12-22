---
tags:
  - web
  - authentication
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/postmessage-send-fake-signin]]'
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: b5c4fd8a-38d1-47ba-bdab-5a12be74d25a
created_at: '2025-12-11T06:10:28.584Z'
updated_at: '2025-12-11T06:10:28.584Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1078]]'
---
# Log In to Target Site with Digits

## Summary

This procedure involves authenticating a user on a site integrated with Digits SDK, setting up the necessary session for subsequent exploitation.

## Description

The target site, such as Fabric.io, uses Digits for sign-in. Logging in loads the SDK and establishes the victim's session, which can then be targeted via postMessage flaws.

## Requirements

1. Access to the target site (e.g., Fabric.io)
2. Valid user credentials for the victim account
3. Web browser

## Defense

Defensive measures and detection strategies:

- Monitor for unusual login patterns
- Implement strict session management

## Objectives

1. Establish authenticated session
2. Load Digits SDK in browser
3. Prepare for postMessage injection

## Instructions

### Step 1: Access Login Page

**Context**: Navigate to the login page of the Digits-integrated site.

Visit https://fabric.io/login and initiate Digits sign-in.

> This loads the SDK script from https://cdn.digits.com/1/sdk.js.

### Step 2: Complete Authentication

**Context**: Enter credentials or phone verification to log in.

Follow the on-screen prompts to authenticate.

> Expected: Successful login and dashboard access.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- web
- authentication
