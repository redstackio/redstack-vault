---
tags:
  - crlf-injection
  - poc-crafting
type: procedure
tools:
  - '[[tools/Browser]]'
  - '[[tools/Bandicam]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-header-injection-test]]'
  - '[[commands/curl-set-cookie-injection]]'
  - '[[commands/curl-variation-test]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7c54a2ac-4fe3-43ed-a5a4-649f7547508f
created_at: '2025-12-11T06:10:16.126Z'
updated_at: '2025-12-11T06:10:16.126Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Craft PoC for Header Injection

## Summary

This procedure crafts a proof-of-concept URL to demonstrate CRLF injection by adding a custom header like 'test:tested' into the HTTP response from the vulnerable endpoint.

## Description

By encoding CRLF sequences in the URL parameter, attackers can manipulate the HTTP response structure. This is applicable to web applications with unsanitized inputs, leading to header injection. Use a browser to submit the URL and inspect network responses.

## Requirements

1. Web browser for testing
2. Ability to inspect HTTP responses
3. Target endpoint accessibility

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all user inputs for special characters
- Use web application firewalls to detect CRLF patterns

## Objectives

1. Create injectable URL
2. Submit and verify header presence
3. Capture evidence of injection

## Instructions

### Step 1: Submit PoC URL

**Context**: Access the URL to trigger the injection.

**Command** ([[commands/curl-header-injection-test]]):

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/landing?ref=gl-tw-tw-promote-mode?t=%0d%0atest:tested'
```

> Expect the response to include the injected header; use browser dev tools for verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-header-injection-test]]

## Tools Used

- [[tools/Browser]]

## Tags

- [[commands/curl-header-injection-test]]
- [[poc-crafting]]
