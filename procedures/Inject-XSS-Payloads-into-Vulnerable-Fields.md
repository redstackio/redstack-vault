---
id: proc-inject-xss-payloads
tags:
  - xss
  - injection
  - stored-xss
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
updated_at: '2025-12-14T17:33:06.185Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payloads-into-Vulnerable-Fields

## Summary

Injects malicious JavaScript into approximately 64 text fields in the DoD worksheet form, exploiting inadequate sanitization for stored XSS.

## Description

Post-initial submission, text fields accept HTML/JS without filtering. Payloads persist in storage and execute on view. Targets legal request app; outcomes include payload storage for later execution.

## Requirements

1. Access to post-name form sections
2. Knowledge of XSS payloads
3. Browser dev tools for testing

## Defense

- Implement output encoding (e.g., HTML entity escaping)
- Use Content Security Policy (CSP) to block inline scripts
- WAF rules for common XSS patterns

## Objectives

1. Populate vulnerable fields with JS
2. Ensure payload acceptance
3. Count and target all 64 fields

## Instructions

### Step 1: Identify and Fill Fields

**Context**: Scan for text inputs and inject.

```plaintext
Complete the form, filling in XSS payloads anywhere you can type. Example: <script>alert('XSS')</script>
```

> Fields accept input. Expected: No rejection; 64 fields vulnerable.

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
- [[injection]]
- [[stored-xss]]
