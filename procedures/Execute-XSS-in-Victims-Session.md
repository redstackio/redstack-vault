---
tags:
  - xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d87a6d0e-6e4c-468a-9dbd-81981f625546
created_at: '2025-12-13T23:56:03.992Z'
updated_at: '2025-12-13T23:56:03.992Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute XSS in Victim's Session

## Summary

This procedure executes the XSS payload in the victim's authenticated session to perform unauthorized actions like creating new scripts.

## Description

With the embedded app re-authenticated in the victim's context, post the malicious message to the iframe to trigger the javascript: URL, executing arbitrary JS. This leads to impacts like script creation in apps. Final step in the chain.

## Requirements

1. Re-authenticated session
2. Iframed app in victim context
3. Malicious postMessage ready

## Defense

Defensive measures and detection strategies:

- Sanitize URLs in SDK functions
- Detect anomalous script creations

## Objectives

1. Post malicious message
2. Execute payload
3. Perform unauthorized action

## Instructions

### Step 1: Prepare Iframe

**Context**: Ensure the embedded app is iframed in victim's session.

> Load the app page.

### Step 2: Send Malicious Message

**Context**: Post the setWindowLocation message with XSS payload.

> Use postMessage to trigger execution, e.g., creating a new script as PoC.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- execution
