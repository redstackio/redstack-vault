---
tags:
  - xss
  - bypass
  - payload-testing
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
impact_level: medium
detection_risk: low
sub_techniques: []
id: 63202563-ef63-48dc-9304-060588eb3f6c
created_at: '2025-12-14T03:16:30.916Z'
updated_at: '2025-12-14T03:16:30.916Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-XSS-Bypass-Payloads

## Summary

Test evasion techniques against the greedy XSS filter using encoded payloads like <%0crameset%20src='javascript:alert(1)'> to insert executable HTML without triggering removal.

## Description

This procedure focuses on crafting and validating bypass payloads for Vimeo's filter. By using URL encoding (%0c for newline) and partial tags (e.g., frameset instead of full script), the payload evades stripping while allowing HTML/JS injection. Target environment is web inputs; outcomes include a working payload for storage.

## Requirements

1. Validated filter from prior analysis
2. Browser for manual payload submission
3. Knowledge of URL encoding

## Defense

Defensive measures and detection strategies:

- Normalize inputs by decoding entities and URLs before filtering
- Apply multiple layered sanitization (e.g., regex + allowlist)
- WAF rules to detect encoded XSS patterns

## Objectives

1. Create a payload that survives filtering
2. Confirm insertion in backend responses
3. Ensure JS execution potential

## Instructions

### Step 1: Craft Encoded Payload

**Context**: Build a malformed tag using encoding to break the greedy match.

Use <%0crameset%20src=''> as a base, extending to <%0crameset%20src='javascript:alert(document.domain)'> to test JS.

> Encoding %0c inserts a carriage return, disrupting the '<' to '>' span.

### Step 2: Submit and Inspect

**Context**: Test in a low-impact field to verify evasion.

Enter the payload in a profile description, submit, and check the response payload via DevTools.

> Successful bypass shows the tag stored without full removal.

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
