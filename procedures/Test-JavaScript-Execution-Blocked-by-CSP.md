---
id: proc-uuid-3
tags:
  - csp
  - javascript-block
  - xss-limit
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:52:33.820Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Test JavaScript Execution Blocked by CSP

## Summary

This procedure tests injection of JavaScript payloads to confirm Content-Security-Policy (CSP) blocks execution, limiting XSS to HTML-only impacts.

## Description

Snapchat's CSP header (e.g., script-src 'self' snapchat.com domains) prevents inline or external JS execution outside trusted sources. Injecting <script>alert(1)</script> via the username parameter reflects but does not run, reducing risk but allowing non-JS exploits.

## Requirements

1. Browser with console access
2. Previous payload crafting setup
3. Mobile User-Agent

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP with no unsafe-inline
- Audit CSP violations in server logs
- Block repeated injection attempts

## Objectives

1. Attempt JS execution
2. Confirm CSP enforcement
3. Identify exploitation boundaries

## Instructions

### Step 1: Craft JS Payload

**Context**: Extend HTML payload with script tag.

Use https://www.snapchat.com/add/%22%3E%3Cscript%3Ealert(1)%3C/script%3E.

> Expected: Encoded payload ready.

### Step 2: Load and Monitor Console

**Context**: Observe failure to execute.

Load URL with mobile User-Agent; check DevTools console.

> Expected: No alert; CSP error like "Refused to execute inline script".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csp]]
- [[javascript-block]]
