---
tags:
  - login-trigger
  - mfa-challenge
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
updated_at: '2025-12-14T17:24:48.301Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: a87be276-fee4-4332-8201-fea729d65d6c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Login-with-Victim-Credentials-to-Trigger-MFA

## Summary

This procedure authenticates to the Grammarly login endpoint using victim credentials to initiate the MFA challenge, setting up the interception point for the bypass.

## Description

Using the victim's email and password, submit credentials to the login form on auth.grammarly.com. This triggers the MFA prompt if enabled, leading to the vulnerable POST request. Prerequisites include valid credentials and an enabled MFA. The attack scenario involves an attacker who has phished or obtained these creds, aiming to escalate to full access via bypass.

## Requirements

1. Victim's email and password
2. Web browser or API client
3. Enabled MFA on target account

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on login attempts
- Alert on failed logins from new devices/locations

## Objectives

1. Reach MFA stage without alerting
2. Prepare for request interception
3. Confirm credentials validity

## Instructions

### Step 1: Submit Credentials

**Context**: Enter details into the login form to authenticate.

Fill email and password fields; click 'Sign In'.

> Expected: Redirect to MFA code entry page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[login-trigger]]
- [[mfa-challenge]]
