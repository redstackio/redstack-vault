---
tags:
  - clickjacking
  - browser-testing
  - iframe-verification
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.318Z'
sub_techniques: []
id: e3ace0e3-b9dd-4edb-8cbb-97826e3dc6b7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Verify-Page-Framing-in-Browser

## Summary

This procedure loads a locally created HTML file containing an iframe in a web browser to check if the target page (Legal Robot verification) renders without framing restrictions, confirming clickjacking susceptibility.

## Description

Clickjacking exploits occur when pages can be iframed from external sites due to absent or misconfigured headers like X-Frame-Options. This step tests the Legal Robot UAT verification page by opening the pre-created `index.html` in a browser. If the page loads fully, it indicates vulnerability, enabling UI redressing where attackers overlay elements to phish clicks. No special tools beyond a standard browser are needed; outcomes include visual confirmation and potential console log checks for errors.

## Requirements

1. Web browser installed (e.g., Chrome, Firefox)
2. The `index.html` file from the prior procedure
3. Internet connectivity to access the target URL

## Defense

Defensive measures and detection strategies:

- Enforce strict X-Frame-Options headers on all pages, especially sensitive ones
- Audit browser developer tools for iframe attempts during security testing
- Implement client-side frame-busting JavaScript as a fallback
- Log and alert on cross-origin iframe loads in web application firewalls (WAF)

## Objectives

1. Confirm the absence of frame protection headers
2. Visualize the embedded page to assess exploit potential
3. Identify impact, noting low sensitivity on verification page but higher on post-login areas

## Instructions

### Step 1: Open HTML File in Browser

**Context**: Launch the browser and load the local HTML file to simulate an attacker's malicious page embedding the target.

**Command** (Manual Browser Action):
No bash command; use file explorer or browser's "Open File" to load `index.html`.

> Upon loading, inspect the page: the iframe should display the Legal Robot verification content without refusal. Check browser console (F12 > Console) for errors like "Refused to display in a frame". Success shows full rendering, indicating vulnerability.

### Step 2: Validate Iframe Behavior

**Context**: Interact minimally with the iframe to ensure scripts and forms work, mimicking a real attack scenario.

**Command** (Manual Verification):
No command; observe and test basic interactions within the iframe.

> Expected: Page elements load and respond; no blocking. If blocked, vulnerability is mitigated.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[browser-verification]]
- [[ui-redressing]]
