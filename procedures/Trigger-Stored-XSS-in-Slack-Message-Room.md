---
id: proc-slack-trigger-xss-001
tags:
  - xss
  - execution
  - slack
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
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.370Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger Stored XSS in Slack Message Room

## Summary

This procedure triggers the stored XSS payload by logging in as a victim and viewing a message room, causing the unsanitized company name to render and execute JavaScript in the browser context.

## Description

Once the payload is stored in the company name field, it is reflected without escaping when displayed in Slack message rooms or headers. Logging into the affected workspace and navigating to any channel or direct message will cause the browser to parse the malicious IMG tag, firing the onerror event and running the JavaScript. This can demonstrate execution via an alert and be escalated to steal session tokens or sensitive data.

## Requirements

1. Access to victim credentials for the affected Slack workspace
2. Web browser to simulate victim interaction
3. Pre-injected XSS payload in the company name

## Defense

Defensive measures and detection strategies:

- Apply output encoding (e.g., HTML entity encoding) when rendering user input in UI
- Deploy browser-based XSS auditors or extensions for detection
- Log and alert on unexpected JavaScript execution in web apps

## Objectives

1. Cause payload execution in victim's browser
2. Verify arbitrary code execution capability
3. Highlight potential for data exfiltration or account compromise

## Instructions

### Step 1: Log In as Victim

**Context**: Use victim credentials to authenticate into the Slack web application.

Open the Slack web app (slack.com) and log in with the victim's account details for the compromised workspace.

### Step 2: Navigate to Message Room

**Context**: View a section of the UI where the company name is displayed, such as a channel or DM.

Select or join a message room (e.g., a randomly generated test channel). The company name will appear in the header or sidebar, triggering the stored payload.

**Expected Output**: Browser executes the JavaScript, showing an alert box with "XSS-by-Imran".

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
