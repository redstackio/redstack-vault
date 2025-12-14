---
id: proc-clickjacking-iframe-demo
name: Demonstrate Clickjacking via Iframe Embedding
tags:
  - clickjacking
  - web
  - iframe
  - nextcloud
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.482Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Clickjacking via Iframe Embedding

## Summary

This procedure demonstrates a clickjacking (UI Redressing) vulnerability by creating a simple HTML page that embeds the target website in an iframe. It confirms the absence of protections like X-Frame-Options headers, allowing attackers to overlay invisible elements and trick users into performing unintended actions, such as clicking download buttons disguised under malicious overlays.

## Description

Clickjacking exploits the lack of frame-busting mechanisms on web applications, enabling malicious sites to embed the target in an iframe and manipulate user interactions. In this case, the Nextcloud download site at https://download.nextcloud.com is vulnerable because it loads unrestricted in external iframes. The procedure involves crafting an HTML file and testing it in a browser, revealing how attackers could create phishing-like pages to induce actions like unintended file downloads. Prerequisites include basic web knowledge and access to a text editor and browser; no special permissions are needed as it targets a public-facing site.

## Requirements

1. Text editor (e.g., Notepad, VS Code) for creating HTML files
2. Modern web browser (e.g., Chrome, Firefox) for testing
3. Internet access to https://download.nextcloud.com

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on all pages
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for unusual iframe embeddings via web application firewalls (WAF)
- Educate users on phishing risks and verify site authenticity before interactions

## Objectives

1. Verify if the target site can be embedded in an external iframe
2. Demonstrate potential for UI manipulation to trick user actions
3. Highlight the vulnerability for remediation, such as adding frame protections

## Instructions

### Step 1: Create the Test HTML File

**Context**: Build a basic HTML page that attempts to iframe the target site to check for embedding restrictions.

Create a file named `clickjacking.html` using a text editor and insert the following code:

```html
<html>
<head>
<title>Clickjack test page</title>
</head>
<body>
<p>Website is vulnerable to clickjacking!</p>
<iframe src="https://download.nextcloud.com" width="500" height="500"></iframe>
</body>
</html>
```

Save the file to your local directory.

> This code defines a simple page with an iframe pointing to the Nextcloud download site. If vulnerable, the site will load fully.

### Step 2: Load and Verify in Browser

**Context**: Open the HTML file in a browser to observe if the target site embeds without blocks, confirming the clickjacking risk.

Navigate to the `clickjacking.html` file by double-clicking it or using the browser's File > Open menu. Inspect the loaded iframe.

> Successful loading indicates no X-Frame-Options or similar protections are in place. The site renders normally, allowing overlays for attacks like tricking users into downloads.

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
- [[web]]
- [[iframe]]
- [[nextcloud]]
