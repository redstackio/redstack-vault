---
tags:
  - xss
  - trigger
  - execution
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
updated_at: '2025-12-14T03:15:53.529Z'
sub_techniques: []
id: 565ab6bb-e3e3-4214-94d6-3fe4ce340aab
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-View

## Summary

This procedure demonstrates triggering the stored XSS by viewing the page that renders the injected payload, leading to JavaScript execution in the browser.

## Description

When the stored data is output without proper encoding, the payload executes in the context of any viewing user, potentially compromising their session or prompting malicious actions.

## Requirements

1. Payload successfully stored from prior steps.
2. Access to view the stored data (e.g., as an admin or another user).
3. Victim browser with JavaScript enabled.

## Defense

Defensive measures and detection strategies:

- Encode outputs when rendering user data (e.g., HTML-encode < > " ').
- Implement XSS auditors or WAF rules to block execution of onload handlers.

## Objectives

1. Execute the payload to confirm vulnerability.
2. Observe impacts like alerts, theft, or defacement.
3. Escalate to real payloads for production exploitation.

## Instructions

### Step 1: Navigate to Stored Data View

**Context**: Load the page or report that displays the additional information containing the payload.

No command; revisit the form or relevant view page.

> Upon rendering, the SVG onload triggers confirm(666). Expected: JavaScript alert dialog; in attack, replace with exfiltration code like sending document.cookie to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[trigger]]
- [[Execution]]
