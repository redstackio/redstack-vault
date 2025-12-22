---
id: proc-uuid-2-1171403
tags:
  - clickjacking
  - xss
  - html
  - css
  - iframe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:12.740Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[JavaScript]]'
---
# Create-Clickjacking-HTML-Page-to-Chain-with-XSS

## Summary

This procedure creates a malicious HTML page using clickjacking to overlay an invisible iframe on a background mimicking the legitimate site, chaining it with a reflected XSS payload to execute JavaScript upon victim click without direct awareness.

## Description

Clickjacking exploits the absence of frame-busting protections (e.g., no X-Frame-Options header) to embed the vulnerable site in an iframe, made invisible via opacity:0 and positioned over a decoy background image. When the victim clicks the overlay, it interacts with the iframed page, triggering the XSS payload in the ?URL= parameter. This targets web applications like DoD sites, enabling stealthy JavaScript execution for data theft. Requires basic HTML/CSS knowledge and a background image resembling the target.

## Requirements

1. Text editor for HTML/CSS creation
2. Background image ('1.png') mimicking target site elements
3. Confirmed XSS-vulnerable URL from prior reconnaissance
4. Local testing environment (browser)

## Defense

Defensive measures and detection strategies:

- Set X-Frame-Options: DENY or SAMEORIGIN header to prevent iframe embedding
- Implement frame-busting JavaScript to detect and break out of iframes
- Use CSP frame-ancestors directive to restrict embedding domains
- Monitor for anomalous traffic from unknown referrers or embedded contexts

## Objectives

1. Construct invisible iframe overlay for user interaction deception
2. Integrate XSS payload into iframe src to chain exploits
3. Verify click triggers JavaScript execution seamlessly

## Instructions

### Step 1: Set Up HTML Structure

**Context**: Create the base page with body background and positioning elements.

Write HTML: <html><head><style>body { background-image: url('1.png'); background-position: 300px 5px; } div { position: absolute; top: 200px; left: 900px; }</style></head><body><div>Click here</div></body></html>

> This positions the clickable area over the mimicked background.

### Step 2: Embed Invisible Iframe

**Context**: Add iframe with XSS payload and opacity to hide it.

Insert: <iframe src="https://███████?URL=javascript:alert(document.domain)//%0D%0A\"https://google.com" id="xxx" width="100%" height="100%" style="opacity:0; position:absolute; top:0; left:0;"></iframe>

> %0D%0A handles line breaks; opacity:0 makes it invisible while capturing clicks.

### Step 3: Test Chaining

**Context**: Load page and simulate click to confirm XSS trigger.

Open HTML in browser, click the div area, and check for alert execution in iframe context.

> Success: Alert fires without visible iframe, proving chain efficacy.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Drive-by Compromise]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[xss]]
