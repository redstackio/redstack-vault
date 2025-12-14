---
id: proc-load-xss-poc-edge
tags:
  - xss
  - microsoft-edge
  - postmessage
type: procedure
tools:
  - '[[tools/Microsoft-Edge]]'
  - '[[tools/universal_xss.html]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Web
  - Microsoft Edge
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.183Z'
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
# Load-Universal-XSS-POC-in-Microsoft-Edge

## Summary

This procedure involves navigating to the hosted PoC page in Microsoft Edge using the spoofed domain, initiating the postMessage to the URL Advisor frame without origin validation.

## Description

The universal_xss.html file is loaded via the spoofed google.com subdomain on the local server. In Edge, the URL Advisor injects its UI as first-party content on every domain, making the frame vulnerable. The PoC sends data via postMessage, which is assigned unsanitized to a link target. Prerequisites: server running and hosts configured; outcome: frame interaction ready for injection.

## Requirements

1. Microsoft Edge installed and Kaspersky KIS active
2. Local server on port 5000 and hosts file modified
3. No proxy interfering with localhost

## Defense

Defensive measures and detection strategies:

- Disable or sandbox browser extensions like URL Advisor
- Validate postMessage origins in security software updates
- Monitor for anomalous frame injections in browser dev tools

## Objectives

1. Load PoC to send malicious postMessage
2. Confirm URL Advisor frame activation
3. Prepare for clickjacking without errors

## Instructions

### Step 1: Navigate to PoC

**Context**: Open Edge and access the full spoofed URL to trigger the frame.

**Command** (Browser navigation):
```bash
# No CLI; in Edge, go to: http://www.google.example.com:5000/universal_xss.html
```

> Manually enter the URL in Edge. Expected output: Page loads, URL Advisor balloon appears, postMessage sent to frame.

### Step 2: Inspect Interaction

**Context**: Use dev tools to verify postMessage handling.

**Command** (Dev tools):
```bash
# Open F12 in Edge, check console for postMessage events
```

> No errors in console indicate successful unvalidated message receipt in the frame.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Microsoft-Edge]]
- [[tools/universal_xss.html]]

## Tags

- xss
- microsoft-edge
- postmessage
