---
id: proc-imgur-clickjacking-setup
tags:
  - clickjacking
  - iframe
  - x-frame-options
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/iframe-clickjacking-setup]]'
  - '[[commands/iframe-sandbox-removal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:33:06.888Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Setup-ClickJacking-Iframe-for-Imgur-Embed

## Summary

This procedure sets up an iframe to frame Imgur's embed endpoint, bypassing inconsistent X-Frame-Options enforcement on certain paths like /a/IMAGE_ID/embed/embed, allowing attackers to overlay malicious UI on legitimate Imgur pages for social engineering.

## Description

The attack targets Imgur's web platform where main domain pages can be framed via specific embed URLs with parameters like pub=true and ref=attacker-site. This enables ClickJacking by positioning invisible or overlaid elements to trick users into unintended actions. Prerequisites include hosting a malicious HTML page and using Firefox for testing, as the chain relies on browser-specific behaviors. Expected outcome is a framed Imgur page ready for UI manipulation without triggering frame-busting.

## Requirements

1. Malicious webpage hosted (e.g., localhost:embed.html)
2. Firefox browser for PoC execution
3. Target Imgur album ID (e.g., lz8DAkB) for embed URL
4. No authentication needed for framing

## Defense

Defensive measures and detection strategies:

- Enforce strict X-Frame-Options: DENY or SAMEORIGIN consistently across all endpoints
- Implement Content-Security-Policy (CSP) frame-ancestors directive to restrict framing
- Monitor for anomalous iframe embeddings in access logs
- User education on avoiding suspicious interactions on image sites

## Objectives

1. Bypass frame restrictions to load Imgur content in attacker-controlled context
2. Prepare for UI overlay to guide victim interactions
3. Enable chaining to self-XSS without direct access

## Instructions

### Step 1: Embed the Iframe

**Context**: Create the initial iframe targeting the embed endpoint to load Imgur content.

**Command** ([[commands/iframe-clickjacking-setup]]):
```html
<iframe src="http://imgur.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540"></iframe>
```

> This HTML snippet loads the public embed view of an Imgur album, using ref parameter to spoof referrer and w=540 for sizing. Expected output: Imgur page renders inside iframe without denial.

### Step 2: Remove Sandbox and Styles

**Context**: After loading, manipulate the iframe to remove restrictions for further access.

**Command** ([[commands/iframe-sandbox-removal]]):
```javascript
setTimeout(function(){ifr = document.querySelector('iframe');ifr.style="";ifr.removeAttribute("sandbox");console.log(ifr);},4000)
```

> Delays 4 seconds for load, then clears styles and sandbox attribute. Expected output: Console logs the unrestricted iframe object.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used

- [[commands/iframe-clickjacking-setup]]
- [[commands/iframe-sandbox-removal]]

## Tools Used

- [[tools/Firefox]]

## Tags

- clickjacking
- iframe
- x-frame-options
