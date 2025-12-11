---
tags:
  - json-manipulation
  - email-array
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 509035e5-6ab8-4fda-90ee-4117ec499bff
created_at: '2025-12-11T06:10:31.060Z'
updated_at: '2025-12-11T06:10:31.060Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Modify JSON Payload for Email Array

## Summary

This procedure edits the JSON payload to inject an array of emails, including the attacker's, into the GitLab password reset request.

## Description

In the JSON-formatted request, replace the single email value with an array containing both the victim's and attacker's emails. This exploits the lack of input validation, causing reset links to be sent to multiple recipients. Targets GitLab's password reset endpoint.

## Requirements

1. JSON-formatted request in Burp Suite
2. Attacker's email address
3. Editing capabilities in Burp

## Defense

Defensive measures and detection strategies:

- Strict input validation for arrays
- Sanitize parameters in reset functionality

## Objectives

1. Inject email array
2. Trigger multi-email reset
3. Enable link reception by attacker

## Instructions

### Step 1: Edit Payload

**Context**: In the request body, modify 'user[email]':'victim@gmail.com' to 'user': {'email': ['victim@gmail.com', 'attacker@gmail.com']}.

> Ensure JSON is valid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- json-manipulation
- email-array
