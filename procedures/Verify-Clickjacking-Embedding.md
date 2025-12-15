---
tags:
  - clickjacking
  - verification
  - iframe
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
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:28:12.405Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 28fef29e-7a3b-4cc8-a9b2-515b4fe87f21
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
  - '[[Steal Web Session Cookie]]'
---
# Verify-Clickjacking-Embedding

## Summary

This procedure tests the clickjacking PoC by loading the HTML in a browser, confirming that the vulnerable Nextcloud page embeds fully in the iframe without frame policy restrictions, setting up for potential user interaction hijacking.

## Description

Verification involves opening the PoC HTML locally or on a server and using browser tools to inspect iframe loading. Success means the target site renders completely, allowing overlays to capture actions like clicks on login buttons or keystrokes for credentials, which could lead to account takeover or data exfiltration in a real attack.

## Requirements

1. Web browser with developer tools
2. Local file access to the PoC HTML
3. Vulnerable subdomain confirmed from earlier steps

## Defense

Defensive measures and detection strategies:

- Add X-Frame-Options: SAMEORIGIN to prevent cross-origin embedding
- Monitor network traffic for unexpected iframe requests
- Deploy client-side protections like NoScript or frame-busting JavaScript

## Objectives

1. Confirm unrestricted iframe embedding
2. Validate invisibility and overlay functionality
3. Assess potential for action hijacking

## Instructions

### Step 1: Load PoC in Browser

**Context**: Open the HTML file to initiate embedding and observe initial load.

**Command** (Browser action):

> Double-click poc.html or serve via local server (e.g., python -m http.server) and navigate to http://localhost:8000/poc.html.

> The page should load with the iframe content invisible; check source to confirm src attribute.

### Step 2: Inspect and Test Interactions

**Context**: Use dev tools to verify full rendering and simulate user actions.

**Command** (Browser dev tools):

> Press F12, go to Elements tab, expand iframe. In Console, test: document.querySelector('iframe').contentDocument – should access embedded DOM without errors.

> Adjust opacity temporarily to 1 to visually confirm Nextcloud loads fully. Test clicks: they should interact with embedded elements if no overlay blocks.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[verification]]
- [[browser-testing]]
