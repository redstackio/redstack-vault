---
tags:
  - xss-trigger
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 72520f53-e72a-4651-ac4a-a1bddc1aeaf6
created_at: '2025-12-14T00:11:25.254Z'
updated_at: '2025-12-14T00:11:25.254Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger XSS in Support Chat

## Summary

This procedure triggers the execution of a stored XSS payload by viewing the affected support chat, leading to cookie exfiltration.

## Description

Upon opening the chat, the malicious filename is rendered in an img tag, causing the onerror event to execute JavaScript that sends document cookies to an external server.

## Requirements

1. Previously uploaded malicious file
2. Access to the support chat interface
3. Attacker-controlled server to receive exfiltrated data

## Defense

Defensive measures and detection strategies:

- Use secure flags on cookies to prevent client-side access
- Monitor network traffic for unexpected outbound requests
- Implement XSS auditing tools

## Objectives

1. Execute injected JavaScript
2. Steal session cookies
3. Achieve potential account compromise

## Instructions

### Step 1: Open Support Chat

**Context**: Load the chat to render the image.

Navigate to the CS Money support chat where the upload occurred.

> Triggers rendering of the img tag with malicious filename.

### Step 2: Verify Exfiltration

**Context**: Check attacker server for data.

Monitor the server at https://gatolouco.000webhostapp.com/cs money/index.php for incoming cookies.

> Confirms successful execution and theft.

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

- xss-trigger
- data-exfiltration
