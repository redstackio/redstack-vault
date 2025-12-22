---
id: proc-004
tags:
  - xss
  - shopify
  - web
  - victim-simulation
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
updated_at: '2025-12-13T23:52:55.586Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Simulate-Victim-Access-with-Incognito-Tab

## Summary

This procedure simulates a victim (e.g., another user or app reviewer) accessing the malicious listing by loading the signed URL in an incognito browser tab, isolating the session from the attacker's cookies.

## Description

Incognito mode ensures a clean slate, mimicking how a third-party would view the shared preview URL. This step validates that the signed URL grants access without authentication, setting up the XSS trigger in a realistic victim context.

## Requirements

1. Captured signed URL from prior step
2. Web browser supporting incognito/private mode (e.g., Chrome, Firefox)
3. No attacker session cookies to avoid interference

## Defense

Defensive measures and detection strategies:

- Require authentication for all preview URLs
- Rate-limit signed URL access to prevent abuse
- Log incognito-like accesses via user-agent or IP analysis

## Objectives

1. Load the malicious listing in an isolated session
2. Confirm signed URL usability without login
3. Replicate victim browser environment

## Instructions

### Step 1: Open Incognito Tab

**Context**: Create a fresh browser session.

Press Ctrl+Shift+N (Chrome) or equivalent to open incognito window.

> Expected: New tab with no prior cookies or history.

### Step 2: Load Signed URL

**Context**: Access the preview as a victim would.

Paste the full URL from earlier and press Enter.

> Expected: Page loads, showing the listing preview.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[web]]
