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
  - Browser
  - Tor Browser
submitted: true
created_at: '[TIMESTAMP]'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.400Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d0dfdc68-5282-4a4c-812d-be005fd40298
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Visit-Website-Link

## Summary

This procedure triggers the reflected XSS payload in Tor Browser's about:tbupdate page by clicking the 'visit our website' link, executing the injected javascript: URI for arbitrary JavaScript.

## Description

After injecting the javascript: URI via the query string, the 'visit our website' link on the page processes the parameter insecurely, leading to JS execution. This occurs in a NoScript-whitelisted context, potentially allowing tracking, fingerprinting, or user-assisted bypasses like bookmarking, though limited by the URI_SAFE_FOR_UNTRUSTED_CONTENT flag.

## Requirements

1. Tor Browser with the injected URL already loaded (from prior procedure)
2. Visibility of the 'visit our website' link on the page
3. No tools required; manual click interaction

## Defense

Defensive measures and detection strategies:

- Sanitize link handlers to strip or validate javascript: schemes
- Add content security policies (CSP) to about: pages
- Log and alert on JS execution from internal pages

## Objectives

1. Execute the injected JavaScript payload
2. Demonstrate impact like alerts or data exfiltration attempts
3. Highlight limitations due to privilege flags

## Instructions

### Step 1: Locate and Click Link

**Context**: Interact with the page element that triggers the query string processing.

On the loaded about:tbupdate page, locate and click the 'visit our website' link.

```plaintext
Click: 'visit our website'
```

> This action causes the page to process the javascript: URI from the query string, executing the payload (e.g., alert(1)). An alert dialog should pop up confirming execution.

**Expected Output**: JavaScript alert(1) displays, or equivalent payload effect.

### Step 2: Validate Execution and Impact

**Context**: Assess the execution context and any potential for further exploitation.

After execution, check the browser console for errors and verify no privilege escalation occurs.

> Manual check: Open developer tools (F12) and inspect for JS events. Note that chrome privileges are blocked.

**Expected Output**: JS runs in untrusted content context; potential for tracking scripts if payload is modified.

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
