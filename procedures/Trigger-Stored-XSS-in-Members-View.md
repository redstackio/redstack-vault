---
tags:
  - xss
  - execution
  - trigger
type: procedure
tools: []
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
updated_at: '2025-12-14T03:15:31.446Z'
sub_techniques: []
id: f24a60cf-ffd1-44b5-9fc6-5291722a110a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-in-Members-View

## Summary

This procedure triggers the stored XSS payload by rendering the malicious asset name in the Veris members view, executing JavaScript in the browser.

## Description

By clicking a symbol or link on the member's details page, the unsanitized asset name is loaded, executing the payload. Target: https://sandbox.veris.in/portal/members/. Requires prior asset creation. Outcome: Alert or arbitrary JS run, enabling theft/phishing in victim sessions.

## Requirements

1. Malicious asset associated with member/group
2. Access to members page
3. Victim-like browser session (same origin)

## Defense

Defensive measures and detection strategies:

- Output encode all dynamic content in views (e.g., htmlspecialchars)
- CSP headers to block inline scripts
- Monitor JS errors and alerts in client logs

## Objectives

1. Execute payload in target context
2. Demonstrate arbitrary code impact
3. Highlight reflection flaw

## Instructions

### Step 1: Interact with Members Page

**Context**: Load member details to force asset name rendering and payload eval.

No command; browser interaction:

- Go to https://sandbox.veris.in/portal/members/
- Find affected member (e.g., 'Test Member')
- Click the symbol/icon for assets/groups

> Expected: `<script>alert(1);</script>` executes, showing alert '1'. Enhance payload for real attacks (e.g., keylogger).

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
- [[trigger]]
