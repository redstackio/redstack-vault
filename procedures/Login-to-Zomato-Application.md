---
id: proc-zomato-login
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
  - Android
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-13T23:55:38.142Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Login-to-Zomato-Application

## Summary

This procedure establishes an authenticated session in the Zomato application via the Android app, providing access to vulnerable endpoints for further exploitation.

## Description

In the context of exploiting a blind XSS in Zomato's admin dashboard, logging in as a regular user allows interaction with the application functions that feed data into the admin view. This step uses standard authentication without any modifications, setting the stage for request interception. Expected outcome is a valid session token for subsequent API calls to api.zomato.com.

## Requirements

1. Valid Zomato user credentials (username/email and password)
2. Zomato Android app installed on a device or emulator
3. Network connectivity to Zomato services

## Defense

Defensive measures and detection strategies:

- Implement multi-factor authentication (MFA) for all logins
- Monitor for unusual login patterns from new devices or locations

## Objectives

1. Obtain authenticated access to application functions
2. Establish session for API interactions
3. Prepare for payload injection without alerting defenses

## Instructions

### Step 1: Launch and Authenticate

**Context**: Open the app and enter credentials to initiate login.

No specific command; use the app UI:

- Launch Zomato Android app
- Enter username/email and password
- Tap login button

> Successful login redirects to the main dashboard, with session cookies or tokens set.

### Step 2: Verify Session

**Context**: Confirm access to protected sections.

Navigate to a user function that triggers API calls, ensuring requests to api.zomato.com are authenticated.

> Expected output: API responses with 200 status and user data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- authentication
- mobile-app
