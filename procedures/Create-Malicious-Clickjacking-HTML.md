---
tags:
  - clickjacking
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
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:44.946Z'
sub_techniques: []
id: 2186613c-ac30-4919-9920-4bc55d1da1d7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-Malicious-Clickjacking-HTML

## Summary

This procedure involves crafting a malicious HTML file that embeds the UPchieve profile page in an iframe, exploiting the absence of X-Frame-Options to set up the clickjacking overlay.

## Description

The attacker creates a simple HTML page with an iframe targeting https://app.upchieve.org/profile. The iframe is initially small and positioned to overlay decoy elements, tricking the victim into interacting with hidden controls. When the victim opens this file while logged in, the embedded page allows unauthorized actions without their knowledge, leading to account modifications or data exposure.

## Requirements

1. Text editor for HTML creation
2. Knowledge of basic HTML/CSS for iframe positioning
3. Delivery method to victim (e.g., email attachment or hosted link)

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options: DENY or SAMEORIGIN headers on all pages
- Use Content-Security-Policy (CSP) frame-ancestors directive
- Scan for and block suspicious HTML attachments in email gateways

## Objectives

1. Embed the target page in an iframe without restrictions
2. Position the iframe for invisible overlay
3. Enable tricked user interactions for exploitation

## Instructions

### Step 1: Write Basic HTML Structure

**Context**: Start with a container page that includes the iframe.

Create a file named iframe.html with content:

```html
<!DOCTYPE html>
<html>
<head><title>Decoy Page</title></head>
<body>
  <h1>Click here for a prize!</h1>
  <iframe src="https://app.upchieve.org/profile" width="300" height="200" style="position:absolute; top:50px; left:50px; opacity:0.5;"></iframe>
</body>
</html>
```

> This sets up an initial semi-transparent iframe overlay.

### Step 2: Test Local Loading

**Context**: Verify the iframe embeds the profile.

Open iframe.html in a browser while logged into UPchieve. Check if the profile loads inside the iframe.

> Success if the profile content appears without framing errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- clickjacking
- html
- iframe
