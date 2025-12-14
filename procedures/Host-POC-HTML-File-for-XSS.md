---
id: proc-uuid-001
name: Host-POC-HTML-File-for-XSS
tags:
  - xss
  - poc-hosting
type: procedure
tools:
  - '[[tools/Local-Web-Server]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.472Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Host-POC-HTML-File-for-XSS

## Summary

This procedure sets up a local web server to host a proof-of-concept HTML file designed to exploit a reflected XSS vulnerability on www.shopify.com through a one-click interaction.

## Description

In this attack scenario, the attacker creates a simple HTML file (poc.html) with a clickable element that, when interacted with, sends a request to the vulnerable Shopify endpoint. The file is hosted on a local HTTP server to simulate delivery via phishing or malicious links. This step is crucial for controlling the environment and injecting payloads without relying on external hosting. Prerequisites include a basic understanding of HTML and web serving. Expected outcomes: A accessible POC page ready for parameter injection and execution.

## Requirements

1. Local machine with Python or similar for simple HTTP server
2. Text editor to create poc.html
3. Network access to serve the file locally

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict script sources
- Monitor for unusual HTTP traffic from local IPs to external domains
- Use web application firewalls (WAF) to block suspicious parameter patterns

## Objectives

1. Deliver the XSS vector via a controlled POC page
2. Prepare for payload injection targeting Shopify
3. Enable one-click exploitation without direct access to the target

## Instructions

### Step 1: Create POC HTML File

**Context**: Build the basic HTML structure with a clickable element that will load Shopify content.

Create poc.html with content like:

```html
<!DOCTYPE html>
<html>
<body>
<button onclick="fetch('https://www.shopify.com/?x=' + encodeURIComponent(document.location.search.slice(1)))">Click to Exploit</button>
</body>
</html>
```

> This script captures the URL parameter and injects it into a request to Shopify. Save the file in a directory.

### Step 2: Start Local Web Server

**Context**: Serve the POC file over HTTP to make it accessible via browser.

Use Python's built-in server (assuming Python 3 installed):

```bash
cd /path/to/poc/directory
python -m http.server 8000
```

> The server runs on port 8000. Access at http://localhost:8000/poc.html. Verify by loading the page in a browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Local-Web-Server]]

## Tags

- [[xss]]
- [[poc-hosting]]
