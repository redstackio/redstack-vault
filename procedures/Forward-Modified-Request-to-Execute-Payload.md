---
id: proc-forward-request-execute-001
tags:
  - xss
  - self-xss
  - execution
  - javascript
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.252Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Forward Modified Request to Execute Payload

## Summary

This procedure releases the modified request from Burp Suite, allowing the server to process it and render the page with the injected XSS payload, resulting in JavaScript execution.

## Description

Disabling intercept and forwarding completes the request cycle. The server reflects the payload in the HTML, executing the script in the browser's context. This self-XSS is limited to the attacker's session but demonstrates the vulnerability's presence.

## Requirements

1. Modified request ready in Burp Intercept tab
2. Browser session active
3. No additional tools beyond Burp

## Defense

Defensive measures and detection strategies:

- Validate and encode reflected content server-side
- Use browser extensions to block XSS (e.g., NoScript)
- Audit page source for injected scripts post-load

## Objectives

1. Deliver the payload to the server
2. Trigger rendering and execution
3. Confirm self-XSS via alert and visual elements

## Instructions

### Step 1: Disable Intercept Mode

**Context**: Stop further interceptions to allow the request to proceed.

No specific command; in Burp Proxy > Intercept, click 'Intercept is off'.

> Expected output: Intercept button deactivates.

### Step 2: Forward and Observe

**Context**: Send the request and watch for execution.

No specific command; click 'Forward' in the Intercept tab.

> Expected output: Page loads with alert(205) dialog and marquee element displaying 'nextcloud.com'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[self-xss]]
- [[Execution]]
- [[JavaScript]]
