---
id: proc-uuid-3
tags:
  - xss
  - waf-bypass
type: procedure
tools:
  - '[[tools/Akamai-WAF]]'
  - '[[tools/Mozilla-Firefox]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-xss-bypass]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:38.843Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Akamai-WAF-for-Reflected-XSS

## Summary

This procedure evades Akamai WAF filters on the media_url parameter to achieve reflected XSS using obscure tags like <brute> and events like onbeforescriptexecute, leading to JavaScript execution.

## Description

Standard XSS payloads are blocked by the WAF, but crafted ones inspired by evasion techniques (e.g., brutelogic) bypass it. The payload closes HTML contexts and triggers JS in supporting browsers like Firefox on data.gov /issue/.

## Requirements

1. Knowledge of WAF rules.
2. Firefox for testing.
3. URL-encoded payloads.

## Defense

Defensive measures and detection strategies:

- Update WAF rules to detect obscure tags and events.
- Implement strict input validation beyond WAF.

## Objectives

1. Evade WAF blocking.
2. Execute arbitrary JS.
3. Confirm impact on user sessions.

## Instructions

### Step 1: Craft and Submit XSS Payload

**Context**: Use <brute> tag and onbeforescriptexecute to inject JS without common blocked elements.

**Command** ([[commands/curl-xss-bypass]]):
```bash
curl -X POST 'https://www.data.gov/issue/' -d 'media_url=catalog.data.gov/dataset/consumer-complaint-database"%3E%3C/div%3E%3C/div%3E%3Cbrute onbeforescriptexecute=confirm(document.domain)>'
```

> No block; response reflects payload.

### Step 2: Execute in Browser

**Context**: Visit the reflected URL in Firefox to trigger the confirm dialog.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-xss-bypass]]

## Tools Used

- [[tools/Akamai-WAF]]
- [[tools/Mozilla-Firefox]]

## Tags

- [[xss]]
- [[waf-bypass]]
