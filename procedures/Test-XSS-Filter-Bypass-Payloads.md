---
id: proc-vimeo-test-bypass-2
tags:
  - xss
  - bypass
  - payload-testing
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
updated_at: '2025-12-14T17:28:20.664Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test XSS Filter Bypass Payloads

## Summary

This procedure tests crafted payloads to evade a greedy XSS regex filter, using encoding and malformations to prevent string removal in web input processing.

## Description

Targeting Vimeo's filter, payloads like `<%0crameset%20src=''>` exploit the regex by breaking expected tag structures with carriage returns (%0c) and spaces. Testing involves iterative submissions to confirm bypass without triggering secondary encoding, enabling storage of executable HTML/JS. Prerequisites include identified filter from prior analysis; outcomes validate payloads for injection.

## Requirements

1. Knowledge of the filter mechanism from analysis
2. Access to input forms
3. Browser console for real-time payload evaluation

## Defense

Defensive measures and detection strategies:

- Employ multi-layer sanitization (e.g., DOMPurify for JS contexts)
- Log and alert on encoded or malformed inputs
- Regular fuzzing of filters during security audits

## Objectives

1. Validate a payload that survives regex removal
2. Ensure compatibility across input types
3. Identify contexts where encoding fails

## Instructions

### Step 1: Craft Initial Payload

**Context**: Build a malformed tag to confuse the greedy regex.

Use URL encoding for line breaks: `<%0crameset%20src=''>`. Submit to a test field and inspect the response.

> Payload should insert without full stripping, appearing as raw text in database echoes.

### Step 2: Iterate and Refine

**Context**: Test variations for robustness.

Try `< %0aimg src=x onerror=alert(1)>` or similar. Monitor for filter evasion in multiple submissions.

> Success if payload stores intact, ready for exploitation testing.

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
