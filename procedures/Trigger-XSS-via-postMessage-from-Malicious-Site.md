---
tags:
  - xss-trigger
  - dom-xss
  - postmessage
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ee7684ff-ca93-4335-a581-de10fd146ee7
created_at: '2025-12-13T23:55:38.316Z'
updated_at: '2025-12-13T23:55:38.316Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-postMessage-from-Malicious-Site

## Summary

This procedure activates the DOM-based XSS by visiting the hosted POC, sending a postMessage that bypasses the origin check in forms2.min.js, leading to arbitrary JS execution or phishing in the target site's context.

## Description

With the POC hosted on the prefix domain, accessing the URL triggers the postMessage to the Marketo handler embedded on www.hackerone.com. The flawed check allows the event to process, executing payloads like window.location = 'phish-site.com' or alert('XSS'). Effective on browsers lacking CSP; in Firefox/Edge, enables limited phishing. Requires no auth; outcomes include confirmed execution via console or behavior changes.

## Requirements

1. Hosted POC on prefix domain
2. Target site (e.g., www.hackerone.com) with Marketo integration
3. Vulnerable browser (no CSP or specific to Firefox/Edge)

## Defense

Defensive measures and detection strategies:

- Upgrade to strict origin validation or use event.origin === target
- Deploy CSP with frame-ancestors and script-src restrictions
- Monitor browser dev tools for unexpected postMessage handling

## Objectives

1. Bypass origin validation via prefix match
2. Execute JS in target domain context
3. Demonstrate impact (redirect/phishing)

## Instructions

### Step 1: Access POC URL

**Context**: Load the malicious page to initiate postMessage.

No specific command; open https://app-sj17.ma/marketo/post2.html in browser targeting www.hackerone.com context (e.g., via iframe or direct if integrated).

> Ensure the page sends postMessage to the expected Marketo origin. Expected: Event dispatched without rejection.

### Step 2: Observe Execution

**Context**: Verify the payload runs in the target site's context.

No specific command; check browser console for JS execution or observe redirect/phishing prompt.

> In CSP-absent browsers, full XSS; in others, limited impact. Expected: Malicious action confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[dom-xss]]
