---
id: proc-uuid-3
tags:
  - clickjacking
  - ui-manipulation
  - xss-chain
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:46:26.528Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Chain with Clickjacking to Force Victim Interaction

## Summary

This procedure chains a confirmed XSS vulnerability with clickjacking by embedding the target site in an iframe and overlaying deceptive elements to trick users into triggering the XSS payload, enabling execution despite CSRF protections.

## Description

Clickjacking exploits the absence of frame protections to overlay invisible iframes, positioning fake buttons over real elements. When combined with XSS, it forces interaction with the vulnerable URL parameter. Using Burp Suite, generate an HTML PoC that loads the target in an iframe, injects the XSS URL, and uses XMLHttpRequest to render the malicious response.

## Requirements

1. Confirmed XSS payload from prior injection
2. Hosting capability for the clickjacking HTML page
3. Burp Suite for PoC generation and testing

## Defense

Defensive measures and detection strategies:

- Set X-Frame-Options: DENY or SAMEORIGIN to prevent iframe embedding
- Implement frame-busting JavaScript on pages
- Educate users on phishing and monitor for anomalous clicks or iframe loads

## Objectives

1. Bypass non-interactive XSS limitations
2. Trick victims into submitting the payload
3. Achieve arbitrary code execution in authenticated contexts

## Instructions

### Step 1: Generate Clickjacking PoC

**Context**: Use Burp Suite to create an HTML page with iframe and overlay.

In Burp Suite's Collaborator or manual editor, craft HTML with <iframe src="https://█████/████&url=malicious"> and CSS to make it transparent, overlaying a fake button at the vulnerable element's position.

> The iframe loads the target; clicking the overlay submits the XSS URL via form or JS.

### Step 2: Host and Test the PoC

**Context**: Deploy the HTML and simulate victim interaction.

Host the PoC on a server (e.g., local Python http.server) and visit it. Click the fake button to trigger the iframe's XMLHttpRequest with the XSS payload.

> Expected output: XSS executes in the iframe's context, alerting or running arbitrary JS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[clickjacking]]
- [[ui-manipulation]]
- [[xss-chain]]
