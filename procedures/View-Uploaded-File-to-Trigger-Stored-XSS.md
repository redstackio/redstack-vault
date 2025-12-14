---
id: proc-uber-trigger-xss-001
tags:
  - stored-xss
  - javascript-execution
  - uber-eats
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
updated_at: '2025-12-13T23:52:49.536Z'
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
# View-Uploaded-File-to-Trigger-Stored-XSS

## Summary

This procedure triggers the stored XSS by accessing the uploaded malicious file, which is served inline and executes JavaScript in the victim's browser.

## Description

Once uploaded, the file is served from the Uber Eats server with Content-Disposition: inline, causing browsers to render HTML/SVG content directly. This executes any embedded JavaScript, leading to stored XSS. Impacts include session hijacking if viewed by admins or other users, or phishing via dynamic content manipulation.

## Requirements

1. URL or access path to the uploaded file
2. Browser session (potentially shared or targeted)
3. Knowledge of the serving behavior

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user-uploaded content before rendering
- Use Content Security Policy (CSP) to block inline scripts
- Monitor for XSS payload executions via browser console logs or WAF alerts

## Objectives

1. Execute the injected JavaScript payload
2. Demonstrate client-side compromise
3. Highlight potential for data theft or account takeover

## Instructions

### Step 1: Locate File Access Point

**Context**: Find where the server serves the uploaded content.

In the menu interface or dashboard, click on the uploaded item or construct the direct URL to the file.

### Step 2: Access and Render File

**Context**: Trigger inline rendering to execute the payload.

Visit the file URL; the server responds with inline disposition, loading the HTML/SVG in the browser.

> The script executes immediately, e.g., showing an alert('XSS') box.

### Step 3: Validate Exploitation

**Context**: Confirm XSS and assess impact.

Inspect browser console for errors or use a more advanced payload to exfiltrate cookies, verifying session access.

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

- [[stored-xss]]
- [[javascript-execution]]
- [[uber-eats]]
