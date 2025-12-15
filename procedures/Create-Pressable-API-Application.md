---
id: proc-pressable-create-app
tags:
  - api
  - pressable
  - setup
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:33:24.403Z'
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
# Create Pressable API Application

## Summary

This procedure creates a new API application in the Pressable dashboard, providing a legitimate entry point for subsequent request interception and IDOR exploitation.

## Description

In the context of exploiting an IDOR in the Pressable API, creating your own API application generates an application ID that can be used to craft update requests. This step requires a valid Pressable account and occurs on the web platform at https://my.pressable.com/api/applications. The outcome is a new app with an ID, enabling proxy-based interception.

## Requirements

1. Valid Pressable account credentials
2. Web browser access to https://my.pressable.com
3. Optional: Proxy tool like Burp Suite for later steps

## Defense

Defensive measures and detection strategies:

- Monitor API application creation logs for anomalous patterns
- Implement rate limiting on application creation endpoints

## Objectives

1. Obtain a base application ID for request manipulation
2. Establish session with authenticity_token
3. Prepare for IDOR testing

## Instructions

### Step 1: Navigate and Create Application

**Context**: Access the API applications management page and submit a new application form.

No specific command; perform via web interface:

- Log in to https://my.pressable.com
- Navigate to /api/applications
- Fill in application details (e.g., name, description) and submit

> This creates the app and displays its ID. Note the ID for later use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[api]]
- [[pressable]]
- [[setup]]
