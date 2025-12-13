---
tags:
  - nextcloud
  - id4me
  - account-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 1110cc6d-43ca-4c45-9403-77f09064f2b9
created_at: '2025-12-13T09:01:26.581Z'
updated_at: '2025-12-13T09:01:26.581Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Complete Unauthorized Registration

## Summary

This procedure completes the registration process using the dummy server, creating and logging into a new user account.

## Description

The dummy server handles requests and redirects back to Nextcloud, resulting in account creation without proper authorization.

## Requirements

1. Redirect from custom domain
2. Functional dummy server
3. Nextcloud vulnerability present

## Defense

Defensive measures and detection strategies:

- Patch the user_oidc app to fully disable features
- Monitor for new account creations from unknown sources

## Objectives

1. Create new user account
2. Gain access to Nextcloud features
3. Achieve unauthorized login

## Instructions

### Step 1: Follow Redirects

**Context**: Complete the fake authentication on the dummy server.

Follow the prompts and redirect back to Nextcloud.

> New account is created upon redirect.

### Step 2: Log In

**Context**: Verify access as the new user.

Log in and access features like chat rooms.

> Confirms successful exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[id4me]]
- [[account-creation]]
