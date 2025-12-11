---
tags:
  - crlf-injection
  - vulnerability-identification
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
detection_risk: low
sub_techniques: []
id: c761b79c-5ccb-4c6c-ad7e-169bca72ab77
created_at: '2025-12-11T06:10:16.132Z'
updated_at: '2025-12-11T06:10:16.132Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Identify Vulnerable Endpoint and Parameter

## Summary

This procedure involves testing the /subscriptions/mobile/landing endpoint on ads.twitter.com with the 't' parameter to identify if it is vulnerable to CRLF injection by accepting URL-encoded CRLF sequences (%0d%0a), allowing header injection.

## Description

The attack targets improper sanitization in web parameters, enabling attackers to split HTTP responses and inject arbitrary headers. This is tested on public-facing Twitter Ads endpoints, with potential for escalation to more severe attacks. Prerequisites include access to a web browser or curl for sending requests.

## Requirements

1. Access to ads.twitter.com endpoints
2. Tool like curl or a browser for sending HTTP requests
3. Knowledge of URL encoding for CRLF sequences

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization to strip CRLF characters from parameters
- Monitor HTTP responses for unexpected headers or anomalies in logs

## Objectives

1. Confirm vulnerability in the 't' parameter
2. Verify header injection capability
3. Document initial findings for further exploitation

## Instructions

### Step 1: Test Parameter with CRLF Sequence

**Context**: Send a request with encoded CRLF to check if it injects into the response.

**Command** ([[commands/curl-header-injection-test]]):

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/landing?ref=gl-tw-tw-promote-mode?t=%0d%0atest:tested'
```

> This command tests the injection of a custom 'test:tested' header; inspect the response for confirmation.

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
- [[vulnerability-identification]]
