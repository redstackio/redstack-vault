---
id: d4e5f6g7-h8i9-0123-defg-456789012345
name: Trigger-XSS-via-Poisoned-Cache
type: procedure
verified: false
submitted: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.641Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - javascript-execution
  - session-theft
commands:
  - '[[commands/curl-trigger-xss]]'
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-XSS-via-Poisoned-Cache

## Summary

This procedure loads the poisoned .js endpoint in a browser to execute the stored XSS payload, alerting and extracting the victim's session token from the application's INITIAL_STATE.

## Description

Once the cache is poisoned, any user loading the endpoint (e.g., via image src or direct script include) executes the injected SVG onload handler. The payload accesses window.INITIAL_STATE.system.cookie to steal the HASESSIONV3 token, enabling credential theft in a web context without server-side execution.

## Requirements

1. Poisoned cache from prior step
2. Victim browser session with valid login
3. JavaScript-enabled browser

## Defense

Defensive measures and detection strategies:

- CSP headers to block inline script execution (e.g., script-src 'self')
- Validate and sanitize all cached JS content for tags like <svg>
- Monitor client-side errors or alerts in browser logs
- Use HttpOnly flags on sensitive cookies to prevent JS access

## Objectives

1. Execute arbitrary JS in victim context
2. Exfiltrate session token via alert or network request
3. Prepare token for impersonation

## Instructions

### Step 1: Load Poisoned Endpoint

**Context**: Fetch and execute the cached JS in a browser to trigger the payload.

**Command** ([[commands/curl-trigger-xss]]):
```bash
curl https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd > poisoned.js
```

> Save the response, then open poisoned.js in a browser or <script src="poisoned.js"></script> on a test page.

### Step 2: Observe Execution

**Context**: In the browser, the payload runs, alerting the cookie value.

**Command** ([[commands/curl-trigger-xss]]):
```bash
# Direct browser visit: https://www.abritel.fr/annonces/location-vacances/france_midi-pyrenees_46_stcere_dt0.php.js?xxxd
```

> Expected output: Alert popup with HASESSIONV3=... token; copy for next steps.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-xss]]

## Tools Used


## Tags

- [[xss]]
- [[javascript-execution]]
- [[session-theft]]
