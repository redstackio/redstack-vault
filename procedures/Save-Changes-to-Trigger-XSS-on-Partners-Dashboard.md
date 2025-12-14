---
tags:
  - xss
  - stored-xss
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: bdf910da-f1e0-41eb-a80d-73ad64cef1a9
created_at: '2025-12-13T23:55:20.842Z'
updated_at: '2025-12-13T23:55:20.842Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Save-Changes-to-Trigger-XSS-on-Partners-Dashboard

## Summary

This procedure saves the app configuration after uploading the malicious SVG, causing the icon to render on partners.shopify.com and execute the stored XSS payload.

## Description

Saving triggers SVG rendering in the dashboard UI, where the onload JavaScript executes due to the bypass. This affects the partner domain directly and sets up persistence for further exploitation. The environment is the web-based app editor; success confirms XSS in a high-privilege context.

## Requirements

1. Malicious SVG uploaded to the sales channel app
2. Browser open on the App info edit page
3. Partner session active

## Defense

Defensive measures and detection strategies:

- Render icons in isolated iframes or sandboxes
- Monitor for JavaScript execution in admin UIs
- Log SVG rendering events and payload attempts

## Objectives

1. Persist the malicious icon in app data
2. Execute XSS immediately on the Partners domain
3. Validate payload for broader impact

## Instructions

### Step 1: Review and Submit Changes

**Context**: Ensure the upload is reflected, then save to trigger rendering.

No specific command; Click "Save" in the App info section.

> Configuration updates. Expected output: Page refreshes, icon renders, and onload alert pops (e.g., "partners.shopify.com").

### Step 2: Verify Execution

**Context**: Check browser console or alert for payload success.

No specific command; Inspect developer tools for JavaScript execution.

> Console shows alert or custom payload output. Expected output: Confirmation of domain-specific XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
