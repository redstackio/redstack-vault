---
id: proc-inject-firefox-xss
tags:
  - xss
  - dom-xss
  - firefox
  - svg-payload
type: procedure
tools:
  - '[[tools/DominatorPro]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.351Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Firefox-XSS-Payload-via-URL-Hash

## Summary

This procedure crafts and delivers a Firefox-specific URL hash payload exploiting the prettyPhoto plugin's inadequate sanitization, injecting an SVG element that executes JavaScript on load for arbitrary code execution.

## Description

In Firefox, the prettyPhoto plugin parses hash parameters like hashIndex without escaping special characters, allowing SVG tags with onload attributes to be inserted into the DOM. The root cause is a weak regex replacement in hashRel processing (`hashRel.replace(/([ #;&,.+\\*'!\"^$[]()=>\\|/])/g,'\\\\$1')`), which fails to neutralize executable content. This enables client-side attacks like alert popping or more severe actions (e.g., cookie theft) without server involvement. Prerequisites include browser access to the site; outcomes confirm XSS via domain alert.

## Requirements

1. Firefox browser
2. Access to eng.uber.com
3. Knowledge of SVG onload payloads

## Defense

Defensive measures and detection strategies:

- Sanitize all URL hash inputs with strict whitelisting
- Use browser extensions to block XSS (e.g., NoScript)
- Log and monitor for anomalous JavaScript alerts or DOM mutations

## Objectives

1. Inject executable SVG code via URL hash
2. Trigger onload execution in Firefox DOM
3. Validate with domain alert for proof-of-concept

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the hash to mimic prettyPhoto's gallery format, embedding the SVG payload to bypass parsing.

No command; manually construct: `http://eng.uber.com/#prettyPhoto[i]/x,<svg/onload=alert(document.domain)>/x`

> The `/x,` prefix tricks the plugin into treating the SVG as content; onload fires on DOM insertion.

### Step 2: Navigate and Execute

**Context**: Load the URL to process the hash and observe execution.

Open the constructed URL in Firefox.

> Expected output: Alert box shows "eng.uber.com". Use developer tools to inspect injected SVG in DOM.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DominatorPro]]

## Tags

- [[xss]]
- [[dom-xss]]
