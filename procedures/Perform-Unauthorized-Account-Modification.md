---
id: proc-uuid-4
tags:
  - csrf
  - web
  - account-takeover
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
updated_at: '2025-12-14T17:27:15.691Z'
skill_level: basic
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform Unauthorized Account Modification

## Summary

This procedure submits a modified form in Slack account settings using the reused CSRF token to change sensitive information like the username, confirming the bypass success.

## Description

With the token replaced, the server treats the request as authenticated and valid, allowing unauthorized changes. This impacts account integrity on the web platform; in a real attack, could be tricked via malicious site, but here manual for PoC.

## Requirements

1. Settings page with replaced token
2. Active new session
3. Intended modification (e.g., new username)

## Defense

Defensive measures and detection strategies:

- Implement double-submit cookie pattern for CSRF
- Audit account changes for anomalies
- Require re-auth for sensitive actions

## Objectives

1. Submit altered form
2. Achieve modification
3. Validate bypass

## Instructions

### Step 1: Prepare Form Data

**Context**: Enter change details.

In username field, input new value.

> Field accepts input.

### Step 2: Submit Form

**Context**: Trigger action with reused token.

Click Save or Submit button.

> Request sent with old token.

### Step 3: Confirm Change

**Context**: Verify success.

Check profile; change applied without CSRF error.

> Update reflected.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[account-takeover]]
