---
tags:
  - clickjacking
  - ui-redressing
  - iframe
  - x-frame-options
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:05.143Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: d9b87dc7-b42d-41a9-b9a8-951fc9318f1d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate Clickjacking with Iframe Embedding

## Summary

This procedure demonstrates a clickjacking (UI redressing) vulnerability by embedding a target web page, such as the Zomato book login page, into an iframe on an external site. It exploits the lack of X-Frame-Options header, allowing attackers to overlay invisible iframes on malicious pages to trick users into performing actions like entering credentials.

## Description

Clickjacking occurs when a malicious site loads a vulnerable page in an iframe and overlays transparent elements to capture user interactions. In this case, the login page at http://book.zomato.com/account/login.aspx lacks the X-Frame-Options header, permitting embedding from any origin. The procedure involves creating a local HTML file with an iframe, loading it in a browser, and verifying unrestricted access. This can lead to account takeover if users are deceived on an attacker's site, though the vulnerability was rated informative with no direct exploitation beyond demonstration.

## Requirements

1. A modern web browser (e.g., Chrome, Firefox) for rendering HTML
2. A text editor to create the HTML file
3. Internet connectivity to access the target URL
4. No special permissions or credentials required

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on all pages
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for unusual iframe embeddings via web application firewall (WAF) logs
- Educate users on phishing risks and verify site authenticity

## Objectives

1. Prove the target page can be framed externally
2. Simulate a UI redressing attack scenario
3. Identify potential for user deception and unauthorized actions

## Instructions

### Step 1: Create the Embedding HTML File

**Context**: Build a basic HTML structure to host the iframe pointing to the vulnerable login page.

Open a text editor and input the following code:

```html
<html><body><iframe src="http://book.zomato.com/account/login.aspx" width="500" height="500"></body></html>
```

Save the file as demo.html.

> This creates a simple page that loads the target without restrictions. Expected output: A saved HTML file.

### Step 2: Render the HTML in a Browser

**Context**: Execute the HTML to embed and display the target page.

Open the demo.html file in a web browser.

> The browser should load the iframe seamlessly. Expected output: Visible login form inside the iframe.

### Step 3: Validate the Vulnerability

**Context**: Confirm the page loads without framing blocks and test interactivity.

Use browser developer tools (press F12) to inspect the iframe and check response headers for X-Frame-Options (should be absent). Attempt to interact with form elements.

> Verify no errors occur. Expected output: Fully functional login page in iframe, proving vulnerability.

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
- [[web]]
- [[vulnerability-demo]]
