---
id: proc-induce-click-001
tags:
  - clickjacking
  - social-engineering
  - privilege-escalation
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:04.768Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Induce-Click-to-Trigger-Role-Change

## Summary

This procedure involves luring the victim to interact with the malicious page, causing them to click the invisible overlay, which triggers an unintended role change in the framed Respondly application, achieving privilege escalation.

## Description

With the invisible setup complete, the attacker uses social engineering (e.g., phishing) to direct the victim to the page. A seemingly innocuous element (or the page itself) prompts a click that hits the overlay, propagating to the hidden role switch. This exploits user trust, leading to unauthorized actions like elevating from user to admin roles.

## Requirements

1. Hosted malicious HTML page (local or remote server)
2. Social engineering vector (email, link sharing)
3. Victim with active Respondly session (logged in)

## Defense

Defensive measures and detection strategies:

- User training on verifying URLs and avoiding unsolicited links
- Server-side logging of role changes with anomaly detection (e.g., sudden escalations)
- Browser extensions to detect clickjacking (e.g., frame-busting scripts)

## Objectives

1. Deceive user into clicking the overlay
2. Execute the role change in the background
3. Confirm privilege escalation without alerting the user

## Instructions

### Step 1: Host and Distribute Page

**Context**: Make the PoC accessible to the victim.

Serve the HTML via a web server or file:// protocol for testing. Share via phishing email: "Click here for Respondly update."

No code; use tools like Python's http.server for hosting:

(Informational: python -m http.server 8000)

> Expected: Victim visits page, sees blank or decoy content.

### Step 2: Monitor and Verify Impact

**Context**: Confirm the click triggers the action.

Use dev tools or proxy (e.g., Burp) to watch for POST requests to role-change endpoints in Respondly.

> Expected: API call like /api/role/update with new role; victim's account shows changes on login.

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
- [[privilege-escalation]]
