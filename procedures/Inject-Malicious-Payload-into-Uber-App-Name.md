---
id: proc-uber-xss-inject-001
name: Inject-Malicious-Payload-into-Uber-App-Name
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Chrome]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.811Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Uber-App-Name

## Summary

This procedure involves creating a new application in Uber's developer portal with a malicious JavaScript payload embedded in the name field, exploiting insufficient input sanitization to store the payload for later execution.

## Description

In the context of Uber's developer portal at https://login.uber.com/applications, the application name field allows arbitrary input without proper escaping. By injecting a payload like "><img src=x onerror=prompt(1)>, an attacker can store HTML/JavaScript that executes when the name is rendered in the browser, such as during app listing or deletion. This targets administrators or other developers viewing the app list, enabling client-side attacks like session theft. Prerequisites include a valid Uber developer account and browser access.

## Requirements

1. Authenticated access to https://login.uber.com/applications
2. Modern web browser (e.g., Firefox or Chrome) for testing
3. No additional tools beyond standard browser functionality

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user-controlled fields like app names
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous app names containing script tags or event handlers in audit logs

## Objectives

1. Persist a malicious JavaScript payload in application metadata
2. Set up conditions for execution in victim browsers
3. Enable potential data exfiltration or session hijacking

## Instructions

### Step 1: Authenticate and Navigate

**Context**: Log in to the Uber developer portal to gain access to the applications management interface.

Open your browser and navigate to https://login.uber.com/applications. Enter your developer credentials to authenticate.

> Expected output: Successful login redirecting to the applications dashboard.

### Step 2: Create New Application with Payload

**Context**: Initiate app creation and inject the XSS payload into the name field to store it server-side.

Click 'Create New Application' or equivalent. In the 'Name' field, enter the payload: "><img src=x onerror=prompt(1)>. Fill other required fields minimally and submit.

> Expected output: Application saved, appearing in the list with the payload as the name. No immediate execution occurs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Chrome]]

## Tags

- xss
- stored-xss
- uber
