---
tags:
  - xss
  - trigger
  - javascript-execution
  - flash
type: procedure
tools:
  - '[[tools/xss-swf-Malicious-Flash-File]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.423Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8553bfd0-8529-4005-8542-9b01e471eb01
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-Vimeo-Hubnut-Pages

## Summary

This procedure triggers the stored XSS by visiting the attacker's Hubnut page on Vimeo's domains, causing the Flash widget to load the injected payload and execute JavaScript from an external SWF file.

## Description

After payload injection, the Hubnut pages on player.vimeo.com and vimeo.com load the user's profile data into the Flash file hubnut.swf, which renders the display name unescaped. The <img> tag fetches the external SWF, executing JavaScript in the browser context, such as alerting the domain or stealing cookies. This affects any victim viewing the page, demonstrating cross-domain impact.

## Requirements

1. Injected payload already stored in the user profile from prior procedure.
2. Knowledge of the user's Vimeo URL identifier (e.g., from profile settings).
3. Web browser to visit the Hubnut URLs.

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs before Flash rendering and block external resource loads.
- Use Content Security Policy (CSP) to restrict script execution and external fetches.
- Log and alert on Flash file interactions with unexpected domains.

## Objectives

1. Execute arbitrary JavaScript in the victim's browser on affected domains.
2. Validate the XSS for proof-of-concept or exploitation.
3. Facilitate data exfiltration or session takeover.

## Instructions

### Step 1: Retrieve Vimeo URL Identifier

**Context**: Obtain the unique identifier needed for Hubnut URLs.

**Command** (Browser Action):

Navigate to https://vimeo.com/settings/profile and copy the 'Vimeo URL' value (e.g., 'user36690798').

> This identifier is used to construct the target Hubnut paths.

### Step 2: Visit Player Hubnut Page

**Context**: Load the Hubnut on player.vimeo.com to trigger the payload.

**Command** (Browser Action):

Navigate to https://player.vimeo.com/hubnut/user/[identifier] (e.g., https://player.vimeo.com/hubnut/user/user36690798).

> The Flash file loads, fetches the SWF via the injected <img>, and executes alert(document.domain).

### Step 3: Visit Main Hubnut Page

**Context**: Repeat on vimeo.com for broader impact.

**Command** (Browser Action):

Navigate to https://vimeo.com/hubnut/user/[identifier] (e.g., https://vimeo.com/hubnut/user/user36690798).

> Similar execution occurs, confirming cross-domain vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/xss-swf-Malicious-Flash-File]]

## Tags

- xss-trigger
- javascript
- domain-execution
