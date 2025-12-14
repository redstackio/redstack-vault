---
id: proc-trigger-xss-001
name: Trigger-XSS-on-Khan-Academy-Pages
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.271Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss
  - execution
  - dom-injection
platforms:
  - Web
tools:
  - '[[tools/Browser-DevTools]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trigger-XSS-on-Khan-Academy-Pages

## Summary

This procedure loads affected Khan Academy pages to render the malicious Graphie, injecting and executing JavaScript via the DOM-based XSS vulnerability.

## Description

The Graphie renderer on khanacademy.org inserts SVG onload or JSON scripts directly, executing on victim browsers. Use devtools for simulation. Expected outcome: Arbitrary JS execution, e.g., alerts or session theft.

## Requirements

1. Propagated malicious asset on CDN
2. Target page URL using the Graphie

## Defense

Defensive measures and detection strategies:

- Escape all user-controlled content in renderers
- CSP to block inline scripts
- Monitor for anomalous JS execution in browser logs

## Objectives

1. Execute payload on page load
2. Demonstrate impact like account takeover
3. Validate in controlled environment

## Instructions

### Step 1: Load Affected Page

**Context**: Navigate to page embedding the Graphie.

Browse to e.g., a math exercise on khanacademy.org using the hash.

> Renderer fetches and inserts. Expected output: JS execution (alert).

### Step 2: Simulate with DevTools

**Context**: Override for testing without propagation.

In [[tools/Browser-DevTools]], enable Network > Override content, replace JSON/SVG response with malicious version.

> Forces injection. Expected output: DOM shows script, console logs execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-DevTools]]

## Tags

- [[xss]]
- [[Execution]]
