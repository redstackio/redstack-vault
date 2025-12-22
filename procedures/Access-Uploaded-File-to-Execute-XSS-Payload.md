---
tags:
  - stored-xss
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.702Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: dfaa040b-661a-400f-b4a7-0aaa5f120da8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Uploaded-File-to-Execute-XSS-Payload

## Summary

This procedure triggers a stored XSS vulnerability by accessing the previously uploaded malicious HTML file, causing the embedded JavaScript to execute in the browser context and potentially steal sensitive data like cookies.

## Description

After uploading a malicious HTML file via the unrestricted upload, the file is served from an endpoint like /registration-service/files/ without sanitization. Opening the file in a browser tab renders the HTML and executes any scripts, leading to stored XSS. In a real attack, the payload could exfiltrate data to an attacker-controlled server. This affects users viewing the certification tab, as the attachment is accessible in their session.

## Requirements

1. Successful upload of malicious file from prior procedure
2. Active session in the certification tab
3. Web browser to open the file URL

## Defense

Defensive measures and detection strategies:

- Sanitize or escape uploaded content to prevent script execution
- Use Content-Security-Policy (CSP) headers to block inline scripts
- Monitor for anomalous JavaScript execution or data exfiltration attempts in browser logs

## Objectives

1. Execute arbitrary JavaScript in the victim's browser
2. Capture session cookies or other sensitive information
3. Demonstrate impact of stored XSS for account takeover

## Instructions

### Step 1: Locate Uploaded File

**Context**: Identify the stored file in the application interface.

Return to the certification tab and find the uploaded 'xss.html' attachment in the list.

### Step 2: Open File in Browser

**Context**: Serve and render the file to trigger the payload.

Click to open the attachment in a new tab. The browser will load it from https://target.com/registration-service/files/xss.html, executing the script.

**Expected Output**: Alert dialog showing document.cookie contents, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[javascript-execution]]
