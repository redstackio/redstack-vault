---
tags:
  - web-inspector
  - network-analysis
type: procedure
tools:
  - '[[tools/Web-Inspector]]'
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
updated_at: '2025-12-14T17:31:30.846Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a37079f9-b976-4914-a81a-1ae6d4f254cc
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inspect-Network-Requests-with-Web-Inspector

## Summary

This procedure uses browser developer tools to inspect network traffic on the Rocket.Chat login page, enabling preparation for custom payload injection in authentication requests.

## Description

To exploit the MongoDB injection vulnerability, attackers need to monitor and modify requests to the /api/v1/login endpoint. This involves opening the Web Inspector (e.g., in Chrome or Firefox) to view network activity, focusing on POST requests. It reveals how the loginToken parameter is handled and allows execution of JavaScript like fetch for PoC testing. This is crucial for understanding the unsanitized input flow in login_token_server.js.

## Requirements

1. Modern web browser (Chrome, Firefox)
2. Access to the Rocket.Chat login page
3. Basic knowledge of developer tools

## Defense

Defensive measures and detection strategies:

- Enable Content Security Policy (CSP) to restrict dev tools usage in production
- Log unusual browser behaviors or extended session times on login pages

## Objectives

1. Capture baseline network requests to /api/v1/login
2. Prepare for payload modification and execution
3. Identify session storage mechanisms for tokens

## Instructions

### Step 1: Open Developer Tools

**Context**: Launch the Web Inspector to monitor network activity.

**Instructions**: Right-click on the login page and select "Inspect" or press F12. Switch to the Network tab and filter for XHR/Fetch requests.

**Expected Output**: Network panel opens, showing any initial loads.

### Step 2: Simulate Login Attempt

**Context**: Trigger a request to observe the loginToken parameter.

**Instructions**: Attempt a normal login (with invalid creds) and inspect the POST body in the Network tab.

**Expected Output**: Request details reveal JSON body with loginToken field, unsanitized for MongoDB.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Inspector]]

## Tags

- [[tools/Web-Inspector]]
- [[network-analysis]]
