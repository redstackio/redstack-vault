---
tags:
  - xss
  - bypass
  - javascript
  - payload
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
detection_risk: medium
sub_techniques: []
id: 9cc2364a-92a0-457e-8a79-9b578482b901
created_at: '2025-12-14T03:15:31.110Z'
updated_at: '2025-12-14T03:15:31.110Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-XSS-Payload-to-Bypass-Filters-in-Internet-Explorer

## Summary

This procedure crafts a specialized XSS payload using a malformed <script> tag to evade filters in the gm.com search function, enabling JavaScript execution in Internet Explorer.

## Description

Site filters may block standard <script> tags, but adding extraneous attributes (e.g., 'xxx') and omitting the closing tag can confuse parsers, especially in older browsers like IE. This targets DOM-based XSS where the search parameter is injected into a script context. Prerequisites: confirmed vulnerable parameter from prior recon. Expected outcomes: arbitrary JS execution, such as alerting cookies for session theft proof-of-concept.

## Requirements

1. Vulnerable search endpoint identified.
2. Internet Explorer for payload testing.
3. Knowledge of site's filter behaviors.

## Defense

Defensive measures and detection strategies:

- Use strict script blocking in filters (e.g., WAF rules for malformed tags).
- Encode all outputs with browser-specific escaping.
- Log and alert on suspicious payloads in GET parameters.

## Objectives

1. Bypass XSS filters with malformed syntax.
2. Execute JS in victim browser context.
3. Demonstrate impact like data exfiltration.

## Instructions

### Step 1: Design Malformed Payload

**Context**: Create a payload that adds an invalid attribute to disrupt filter matching while preserving IE's parsing.

Construct: <script xxx>alert(document.cookie)</script> (no closing </script>, extra 'xxx').

> This evades regex-based filters expecting standard tags; IE injects it into DOM, executing the alert.

### Step 2: Inject and Test Payload

**Context**: Deliver the payload via the search parameter and verify execution.

Load https://www.gm.com/search?search=%3Cscript%20xxx%3Ealert(document.cookie)%3C/script%3E in IE. Observe for alert popup with cookie data.

> URL-encode the payload (%3C for <, etc.). Success: JS runs, confirming bypass and exploitation.

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
- [[bypass]]
- [[JavaScript]]
