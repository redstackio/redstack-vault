---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567892
tags:
  - email
  - confirmation
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:42.889Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Attacker-Email-Confirmation-Link-Generation

## Summary

This procedure generates a confirmation email from Liberapay containing authentication parameters needed for the CSRF POC.

## Description

The attacker initiates the login process by submitting their email on the Liberapay login page, receiving a link with id, key, and token parameters. These are critical for crafting the cross-site request. The target environment is the web login flow at https://liberapay.com/. Prerequisites include an attacker-controlled Liberapay account and email access.

## Requirements

1. Attacker's Liberapay account
2. Access to email inbox
3. Web browser for navigation

## Defense

Defensive measures and detection strategies:

- Rate-limit email confirmation requests
- Log and alert on repeated confirmation attempts

## Objectives

1. Obtain confirmation link with parameters
2. Prepare for parameter extraction
3. Validate link functionality

## Instructions

### Step 1: Submit Attacker Email

**Context**: Trigger the email by requesting login confirmation.

No command; navigate to https://liberapay.com/ and enter attacker email in the login form, then submit.

> Email arrives with URL containing log-in.id, log-in.key, log-in.token.

### Step 2: Retrieve and Inspect Email

**Context**: Check inbox for the link.

Manually open email and copy the full URL.

> Expected: Valid parameters in query string.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email]]
- [[login-flow]]
