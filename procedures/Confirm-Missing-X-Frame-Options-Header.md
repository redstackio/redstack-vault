---
id: proc-confirm-missing-xframe
name: Confirm Missing X-Frame-Options Header
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.701Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - clickjacking
  - iframe
  - header-confirmation
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Confirm Missing X-Frame-Options Header

## Summary

This procedure confirms a clickjacking vulnerability by attempting to embed the target API endpoint in an iframe, verifying that no X-Frame-Options header blocks the framing, which could allow UI redressing attacks on sites like GoodHire's API.

## Description

After initial header checks, this step practically tests the vulnerability by creating a test HTML page with an iframe pointing to the endpoint. If the content loads without browser enforcement of framing restrictions, the absence is confirmed. This is particularly relevant for APIs that render UI elements, enabling attackers to overlay malicious content and capture unintended user actions, though impact is low without user interaction.

## Requirements

1. A local web server or ability to open HTML files in a browser (e.g., file:// protocol).
2. Internet access to the target endpoint.
3. Text editor to create the test HTML file.

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options: SAMEORIGIN on all responses.
- Log and alert on cross-origin iframe attempts using server-side monitoring.
- Employ browser security features like sandboxing for embedded content.

## Objectives

1. Attempt to frame the API endpoint in an iframe.
2. Observe if loading succeeds without restrictions.
3. Document the vulnerability for reporting.

## Instructions

### Step 1: Create Test HTML File

**Context**: Build a simple HTML page to embed the target URL in an iframe.

**Command** (Manual file creation):
Create a file named test-iframe.html with the following content:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Clickjacking Test</title>
</head>
<body>
    <h1>Test Page</h1>
    <iframe src="https://www.goodhire.com/api" width="600" height="400" style="border: 1px solid black;"></iframe>
    <p>If the iframe loads, X-Frame-Options is missing.</p>
</body>
</html>
```

> Save the file and open it in a modern browser like Chrome or Firefox.

### Step 2: Load and Verify in Browser

**Context**: Open the HTML file and check if the iframe renders the API content.

**Command** (Browser action):
Open test-iframe.html in your browser.

> Expected: The iframe displays the API response (e.g., JSON or UI) without errors like "Refused to display in a frame". Console (F12) should show no framing-related warnings.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[ui-redressing]]
