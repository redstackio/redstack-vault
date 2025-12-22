---
tags:
  - xss
  - stored-xss
  - javascript-execution
  - session-hijacking
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
updated_at: '2025-12-14T03:16:37.384Z'
sub_techniques: []
id: 43a39982-ebd4-44e5-a42f-0a4f9f1e145a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Uploaded-File

## Summary

This procedure triggers the execution of a stored XSS payload by rendering the uploaded malicious SVG in a victim's browser, leading to arbitrary JavaScript execution.

## Description

Once the SVG is uploaded and stored, accessing or displaying it in the web interface causes the browser to parse the SVG and execute embedded scripts. This exploits the lack of sanitization, allowing attacks like cookie theft in the context of the viewing user. It targets authenticated sessions and relies on social engineering or legitimate viewing to trigger.

## Requirements

1. URL or interface access to the uploaded SVG file
2. Victim browser without strict XSS protections
3. Attacker monitoring exfiltration endpoint
4. Authenticated context for maximum impact

## Defense

Defensive measures and detection strategies:

- Render uploads in isolated iframes with sandboxing
- Strip or escape script content from SVGs before serving
- Implement strict CSP headers blocking inline scripts
- Log and alert on script execution attempts in file views

## Objectives

1. Execute JavaScript in the victim's browser context
2. Exfiltrate sensitive data like session cookies
3. Achieve session hijacking or further persistence

## Instructions

### Step 1: Access the Uploaded File

**Context**: Navigate to the location where the SVG is displayed or embedded in the web application.

Use the browser to visit the file view URL, e.g., click on the attachment link in the dashboard.

No command; browser navigation.

> The server serves the SVG, which the browser renders directly.

### Step 2: Observe Payload Execution

**Context**: The onload or script tag triggers JavaScript upon rendering.

Monitor the browser console or network tab for execution signs.

Example observed behavior: Alert popup or HTTP request to attacker server.

> Success is indicated by data exfiltration, confirming the XSS chain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- stored-xss
- javascript-execution
