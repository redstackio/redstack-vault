---
tags:
  - account-takeover
  - session-termination
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Manipulation]]'
updated_at: '2025-12-14T17:32:57.803Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: d17b6658-e7e2-4899-a4d7-55ee211df86b
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Account Manipulation]]'
---
# Sign-Out-After-Modification

## Summary

This procedure terminates the current session after account modifications to enforce the changes and prevent immediate victim detection.

## Description

Following an email change, logging out ensures the victim cannot easily revert or notice the alteration without attempting login. This step is crucial in web applications like Infogram to solidify the takeover by invalidating the old session pathway.

## Requirements

1. Active session post-email change
2. Access to the user menu

## Defense

Defensive measures and detection strategies:

- Auto-notify on logouts after profile changes
- Session logging for anomaly detection

## Objectives

1. Secure the modification
2. Force new login verification

## Instructions

### Step 1: Initiate Logout

**Context**: End the session cleanly.

From the profile or dashboard, click the user menu and select "Log Out".

> Expected: Redirect to login page; cookies/sessions cleared.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Account Manipulation]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-takeover]]
- [[session-termination]]
