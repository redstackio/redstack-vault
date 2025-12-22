---
id: proc-trigger-csp-bypass-856836
tags:
  - xss
  - csp-bypass
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
updated_at: '2025-12-13T23:52:20.964Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-CSP-Bypass-XSS

## Summary

This procedure visits the simple API endpoint for the multi-version package to trigger the concatenated XSS payload, loading an external script and bypassing CSP.

## Description

With payloads split across versions, the endpoint's HTML generation concatenates requires_python values, forming a complete <script src=...> tag that loads external JS without violating CSP's inline restrictions.

## Requirements

1. Multi-version packages uploaded
2. External script accessible (e.g., test.js)
3. Browser with GitLab access

## Defense

Defensive measures and detection strategies:

- Audit HTML generation for concatenation risks
- CSP reporting to detect bypass attempts
- Restrict external script sources

## Objectives

1. Execute external JavaScript via concatenation
2. Confirm CSP evasion
3. Achieve full client-side compromise

## Instructions

### Step 1: Access Bypass Endpoint

**Context**: Render the endpoint to trigger payload concatenation and script load.

No command; browser visit:

https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_csp_bypass

> Console shows no CSP errors; external script executes (e.g., alert from test.js).

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
- [[csp-bypass]]
- [[trigger]]
