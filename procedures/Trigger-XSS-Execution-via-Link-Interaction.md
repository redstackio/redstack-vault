---
id: proc-slack-xss-trigger-4561
tags:
  - xss
  - javascript-execution
  - link-interaction
  - slack
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:31.223Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-via-Link-Interaction

## Summary

This procedure exploits the stored XSS by interacting with the malicious link in Slackbot DMs, executing JavaScript in the browser context for potential data theft.

## Description

Once the payload is stored and rendered as an anchor tag in the Slack web application, clicking the link triggers the javascript: URI, running arbitrary code like alerting cookies. This occurs in the victim's session if they view the DM thread during onboarding. The attack targets the web platform's rendering of stored messages. Prerequisites: Payload already injected and visible. Outcomes include JS execution for session hijacking or exfiltration.

## Requirements

1. Access to the Slack DM thread with the rendered payload
2. Victim or tester viewing in a web browser
3. No additional tools; relies on UI interaction

## Defense

Defensive measures and detection strategies:

- Block javascript: URIs in all hyperlink rendering
- Implement Content Security Policy (CSP) to restrict inline JS execution
- Monitor for unexpected alerts or JS errors in client logs

## Objectives

1. Execute stored JavaScript payload
2. Access client-side data like cookies
3. Demonstrate potential for broader attacks like session theft

## Instructions

### Step 1: Locate the Malicious Link

**Context**: Identify the stored payload in the DM history.

No command; scroll to the echoed response in Slackbot's thread.

> The payload appears as clickable text wrapped in an anchor.

### Step 2: Interact to Execute

**Context**: Click the link to trigger the XSS.

No command; simply click the hyperlink in the web interface.

> Expected: Alert box with document.cookie contents; console logs JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[cookie-theft]]
