---
tags:
  - xss
  - dom-xss
  - iframe
  - referrer-spoofing
type: procedure
tools:
  - '[[tools/Node.js]]'
  - '[[tools/Express]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 47aa9eb0-9f3a-4a0e-b5b1-21adecb2dc64
created_at: '2025-12-13T23:56:19.666Z'
updated_at: '2025-12-13T23:56:19.666Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trigger-DOM-XSS-via-Iframe-Referrer-Spoofing

## Summary

This procedure triggers the DOM-based XSS by accessing a malicious page that embeds the vulnerable Acronis promo page in an iframe, causing the `document.referrer` to be spoofed to the attacker's domain/path, leading to the load and execution of arbitrary JavaScript from the attacker's '/marketo/common.js'.

## Description

The vulnerability stems from unvalidated `document.referrer` use in `document.write` to construct script src in the Acronis client-side JS. By serving a page with an iframe src to the vulnerable URL (e.g., https://promo.acronis.com/GL-Trial-MassTransit.html), the referrer becomes the attacker's localhost:5000, injecting the path and loading attacker JS. This executes in the victim's browser context, allowing theft of cookies or other attacks. Prerequisites: Running malicious server from prior procedure.

## Requirements

1. Active Express server hosting the iframe page and payload JS
2. Web browser on attacker's or victim's machine
3. Network access to localhost:5000 (or public IP for remote)
4. Vulnerable target page accessible

## Defense

Defensive measures and detection strategies:

- Avoid `document.write` for script loading; use safer alternatives like `script.src`
- Implement strict referrer validation or ignore referrer for script sources
- Enable XSS filters in browsers and audit client-side code for referrer dependencies
- Log and alert on anomalous script loads from external referrers

## Objectives

1. Spoof referrer to inject attacker-controlled script path
2. Execute malicious JS in victim browser
3. Demonstrate impact like alerts or data exfiltration

## Instructions

### Step 1: Prepare Malicious HTML

**Context**: Ensure the served page includes the iframe to embed the vulnerable content.

No command; verify `index.js` serves HTML with `<iframe src="https://promo.acronis.com/GL-Trial-MassTransit.html"></iframe>`.

> The iframe load sets referrer to attacker's URL.

### Step 2: Access the Page in Browser

**Context**: Visit the malicious page to initiate the referrer spoof and script load.

Open http://localhost:5000 in a browser.

> The page loads, iframe fetches Acronis content, which writes script src based on referrer (attacker's /marketo/common.js), executing the payload.

### Step 3: Verify Execution

**Context**: Confirm XSS trigger by observing JS effects.

Inspect browser console or wait for alert.

> Expected: Malicious code runs, e.g., alert pops up.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Node.js]]
- [[tools/Express]]

## Tags

- xss
- iframe
- referrer
