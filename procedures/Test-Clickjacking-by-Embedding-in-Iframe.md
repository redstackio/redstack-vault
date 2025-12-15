---
tags:
  - clickjacking
  - iframe
  - x-frame-options
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/create-iframe-test-html]]'
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e33486e4-d756-46de-a090-66fa194fa326
created_at: '2025-12-14T17:28:04.689Z'
updated_at: '2025-12-14T17:28:04.689Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test-Clickjacking-by-Embedding-in-Iframe

## Summary

This procedure tests for clickjacking vulnerabilities by attempting to embed a target web page in an iframe, exploiting the absence of frame-busting headers like X-Frame-Options. It is used to identify sites susceptible to UI manipulation attacks where attackers can trick users into unintended interactions.

## Description

Clickjacking occurs when a malicious site loads a victim site in an invisible iframe and overlays elements to capture clicks. This procedure creates a basic HTML file to embed the target (e.g., love.uber.com) and verifies if it loads without restrictions. Prerequisites include a local web server or direct file opening in a browser; no special access is needed. Expected outcomes: successful embedding confirms the vulnerability, allowing further POC development.

## Requirements

1. Internet access to reach the target domain
2. Web browser for testing
3. Text editor or terminal for creating HTML files

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on all responses
- Use Content-Security-Policy (CSP) frame-ancestors directive to restrict framing
- Monitor for anomalous iframe embeddings via web application firewall (WAF) logs

## Objectives

1. Confirm if target site can be iframed
2. Identify missing security headers
3. Validate potential for clickjacking attacks

## Instructions

### Step 1: Create Test HTML File

**Context**: Generate a simple HTML page with an iframe pointing to the target URL to test embedding.

**Command** ([[commands/create-iframe-test-html]]):
```bash
cat > test-iframe.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking Test</title>
</head>
<body>
    <h1>Testing iframe embedding</h1>
    <iframe src="https://love.uber.com" width="800" height="600"></iframe>
</body>
</html>
EOF
```

> This command creates test-iframe.html with an iframe sourcing love.uber.com. Expected output: File created successfully; no errors in terminal.

### Step 2: Load and Verify in Browser

**Context**: Open the HTML file in a browser to check if the iframe loads the target site.

**Instructions**: Run `open test-iframe.html` (macOS) or equivalent, or drag the file to a browser. Inspect the page source or console for any X-Frame-Options errors.

> If the site loads fully, the vulnerability is confirmed. Browser console should show no blocking messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used

- [[commands/create-iframe-test-html]]

## Tools Used


## Tags

- [[clickjacking]]
- [[web]]
- [[vulnerability-testing]]
