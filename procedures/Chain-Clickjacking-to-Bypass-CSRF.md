---
id: proc-uuid-3-1149144
tags:
  - clickjacking
  - csrf-bypass
  - ui-redress
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.524Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Chain-Clickjacking-to-Bypass-CSRF

## Summary

This procedure chains clickjacking with the XSS vulnerability to trick authenticated users into triggering the endpoint via an overlaid iframe, bypassing CSRF protections inherent to XMLHttpRequest-based fetches.

## Description

Clickjacking exploits the lack of frame protections by embedding the target site in an iframe, scaling it down, and overlaying deceptive elements. A user click on the fake button interacts with the hidden iframe, submitting the malicious URL parameter and executing the XSS. This enables exploitation without direct links to the payload. Requires hosting the PoC HTML and luring victims.

## Requirements

1. Vulnerable endpoint confirmed with XSS
2. Hosting for PoC HTML page
3. No X-Frame-Options header on target

## Defense

Defensive measures and detection strategies:

- Set X-Frame-Options: DENY or SAMEORIGIN
- Implement frame-busting JavaScript
- Educate users on phishing and unexpected clicks

## Objectives

1. Embed target in iframe without blocking
2. Trick user interaction to trigger XSS
3. Achieve execution in authenticated context

## Instructions

### Step 1: Generate PoC HTML

**Context**: Use Burp Suite to craft the clickjacking page.

In [[tools/Burp-Suite-Professional]], create an HTML file with iframe:

```html
<iframe src="https://█████/████" style="position:absolute; top:0; left:0; width:400px; height:300px; opacity:0.5; z-index:0;"></iframe>
<button style="position:absolute; z-index:1;">Fake Click Button</button>
```

Position so button click hits the iframe's vulnerable element.

### Step 2: Host and Test

**Context**: Serve the PoC and verify click triggers the endpoint.

Host on attacker domain and access in browser. Click should submit the URL with XSS payload.

**Expected Output**: Iframe loads, click executes request, XSS fires.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[clickjacking]]
- [[csrf-bypass]]
