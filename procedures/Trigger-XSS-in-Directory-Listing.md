---
tags:
  - xss
  - execution
  - browser
type: procedure
tools:
  - '[[tools/Firefox-ESR]]'
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
updated_at: '2025-12-14T00:11:09.688Z'
sub_techniques: []
id: 8032f8a9-4c60-4b7b-aaaf-e58d068f80c0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Directory-Listing

## Summary

This procedure accesses the seeftl server's directory listing in a browser and interacts with the malicious filename to execute the injected JavaScript, demonstrating the stored XSS impact.

## Description

When the browser loads the directory listing, the unsanitized filename injects an onmouseover event into the HTML. Hovering over the link triggers the alert, proving arbitrary JavaScript execution in the victim's context. This could extend to stealing cookies, session hijacking, or phishing.

## Requirements

1. seeftl server running on localhost:8000
2. Browser with JavaScript enabled
3. Access to http://localhost:8000/

## Defense

Defensive measures and detection strategies:

- Enable browser extensions for XSS detection (e.g., NoScript)
- Use web application firewalls (WAF) to scan for injected scripts
- Educate users on avoiding suspicious file servers

## Objectives

1. Load the vulnerable listing in a browser
2. Execute the payload via user interaction
3. Confirm impact like session theft potential

## Instructions

### Step 1: Access and Interact with Listing

**Context**: Open the server URL in a browser and hover over the filename to trigger the event.

**Command**:
```bash
# No command; use browser to navigate to http://localhost:8000/
```

> In Firefox ESR 60.7.2esr, the listing shows files; hovering the malicious name executes alert("xss"). Expected: Popup dialog confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-ESR]]

## Tags

- xss
- execution
