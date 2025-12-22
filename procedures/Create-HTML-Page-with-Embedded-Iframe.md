---
tags:
  - clickjacking
  - ui-redressing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:05.242Z'
sub_techniques: []
id: 5d0edef2-d414-4471-bb8a-4f2519b94ee4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create HTML Page with Embedded Iframe

## Summary

This procedure creates a simple HTML page that embeds the target website in an iframe, exploiting the absence of X-Frame-Options to demonstrate clickjacking potential.

## Description

Clickjacking relies on framing the target site invisibly or overlaid on a malicious page to capture user clicks. This procedure uses basic HTML to construct such a page for the target https://sifchain.finance/. In an attack scenario, this file would be hosted on an attacker-controlled domain. Prerequisites include a text editor. Outcomes: A functional HTML file that loads the target without restrictions, allowing simulation of tricking users into credential entry or transaction approvals.

## Requirements

1. Text editor to write HTML
2. Target URL from prior reconnaissance
3. Local file system access

## Defense

Defensive measures and detection strategies:

- Set X-Frame-Options: DENY or SAMEORIGIN in server responses
- Monitor for anomalous iframe embeddings via web application firewall (WAF)

## Objectives

1. Build iframe-containing HTML for exploitation
2. Ensure compatibility with target site
3. Prepare for vulnerability verification

## Instructions

### Step 1: Open Text Editor

**Context**: Start creating the HTML structure.

Launch a text editor like Notepad or VS Code.

> This sets up the environment for coding the iframe.

### Step 2: Write HTML with Iframe

**Context**: Embed the target URL in an iframe to test framing.

Paste the following code into the editor:

```html
<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>Website is vulnerable to clickjacking!</p>
<iframe src="https://sifchain.finance/" width="1000" height="600"></iframe>
</body>
</html>
```

> Save as clickjack_test.html. Expected output: Valid HTML file with iframe sourcing the target.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[ui-redressing]]
