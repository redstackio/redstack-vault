---
id: p-craft-payload-bypass
tags:
  - xss
  - waf-bypass
  - payload-crafting
type: procedure
tools:
  - '[[tools/Google-Search]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.945Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft Payload to Bypass Kona WAF and Chrome XSS Auditor

## Summary

This procedure crafts an encoded JavaScript payload using multiple '&' characters to exploit PHP's FILTER_SANITIZE_STRING partial stripping, evading Kona WAF rules and Chrome's XSS Auditor while enabling attribute injection in pagination links.

## Description

Attackers research sanitization behaviors and construct payloads that manipulate string filtering to appear benign to protections but functional post-processing. The scenario targets data.gov's query handling, where '&' causes tag stripping that inadvertently preserves the malicious onmouseover event. Outcomes include a working payload for injection. Prerequisites: Knowledge of PHP filters and WAF mechanics.

## Requirements

1. Access to [[tools/Google-Search]] for PHP filter research
2. URL encoder/decoder tool (built-in browser dev tools)
3. Target endpoint with known reflection

## Defense

Defensive measures and detection strategies:

- Upgrade to stricter filters like FILTER_SANITIZE_FULL_SPECIAL_CHARS
- Tune WAF to detect multi-'&' patterns in queries
- Enable browser XSS Auditor and monitor for bypass attempts

## Objectives

1. Create payload that survives sanitization
2. Neutralize WAF and auditor detections
3. Enable JavaScript event injection

## Instructions

### Step 1: Research Sanitization

**Context**: Understand how FILTER_SANITIZE_STRING handles '&' and tags.

Use [[tools/Google-Search]] to query "PHP FILTER_SANITIZE_STRING ampersand stripping" and note that multiple '&' lead to partial tag removal without full payload destruction.

> Expected: Insight into why 3+ '&' bypasses protections.

### Step 2: Encode and Test Payload

**Context**: Build and iteratively test the injection string.

Construct zzz'onmou<seover=1&ale<rt('xsp'<)<;1; //, URL-encode as needed, and append as ?&q&zzz'onmou<seover=1&ale<rt('xsp'<)<;1; //. Load in browser and check network logs for no blocks.

> Success: Payload reflects as onmouseover=alert('xsp') in source.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Search]]

## Tags

- waf-bypass
- xss
