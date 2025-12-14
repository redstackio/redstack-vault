---
id: proc-uuid-trigger-xss
tags:
  - stored-xss
  - session-theft
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.466Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Victim-Access-to-Poisoned-Cache

## Summary

This procedure exploits the poisoned cache by having a victim load the affected .js file, executing the stored XSS to access and exfiltrate their session cookie from `window.INITIAL_STATE.system.cookie`, enabling account takeover.

## Description

Once cached, the .js file is served to any user requesting it, executing the injected `<svg/onload=...>` payload in their browser context. The payload targets the app's global state variable containing the session cookie, sending it to an attacker-controlled endpoint. Applies to client-side JavaScript in web apps.

## Requirements

1. Cache successfully poisoned from prior steps
2. Victim access to the site (e.g., via phishing)
3. Browser executing the .js file

## Defense

Defensive measures and detection strategies:

- Implement output encoding for all dynamic content in JS files
- Use HTTP-only and secure flags on session cookies
- Monitor for unexpected JavaScript execution or data exfiltration in client logs

## Objectives

1. Execute XSS in victim's browser
2. Steal session token from app state
3. Achieve account takeover using the token

## Instructions

### Step 1: Direct Victim to Endpoint

**Context**: Lure the victim to a page loading the poisoned .js, such as a listing page on abritel.fr.

Provide a link to `https://www.abritel.fr/annonces/...` which includes the .js file.

### Step 2: Execute and Exfiltrate

**Context**: On load, the payload runs, alerting or sending `window.INITIAL_STATE.system.cookie` to attacker.

Payload effect: `<svg/onload=alert(document.cookie)>` or fetch to attacker server with cookie data.

> Verify by checking network requests or alert; use stolen token to hijack session.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques

- N/A

## Commands Used

- N/A

## Tools Used

- N/A

## Tags

- [[xss]]
- [[session-hijacking]]
- [[account-takeover]]
