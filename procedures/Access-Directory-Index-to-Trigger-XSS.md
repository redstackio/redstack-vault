---
tags:
  - xss
  - browser
  - execution
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
updated_at: '2025-12-14T03:16:37.209Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 39d0685e-9202-4465-bb54-74d3d6a375ef
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Directory-Index-to-Trigger-XSS

## Summary

This procedure accesses the server's directory index in a browser, triggering the injected iframe to load the malicious HTML and execute JavaScript.

## Description

Viewing http://localhost:8080 renders the unescaped HTML listing, where the malicious filename injects the iframe, sourcing the payload file and running the script in the user's browser context, demonstrating arbitrary code execution.

## Requirements

1. Running statics-server on localhost:8080
2. Web browser (e.g., Chrome, Firefox)
3. Malicious files in the served directory

## Defense

Defensive measures and detection strategies:

- Enable browser extensions for XSS detection (e.g., NoScript)
- Log and alert on unexpected JavaScript execution or iframe loads
- Use secure headers like X-Content-Type-Options: nosniff

## Objectives

1. Load the vulnerable directory listing
2. Activate the XSS payload via iframe
3. Achieve JavaScript execution for impact demonstration

## Instructions

### Step 1: Open Browser URL

**Context**: Navigate to the server endpoint to view the index and trigger the exploit.

**Command**:
```bash
# No command; use browser to open http://localhost:8080
```

> Manually enter the URL in the browser address bar. Expected output: Page loads with directory links, injected iframe executes, and alert dialog appears.

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
- execution
