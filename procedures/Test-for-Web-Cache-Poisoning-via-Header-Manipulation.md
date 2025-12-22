---
tags:
  - web-cache-poisoning
  - header-manipulation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-set-x-forwarded-host]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6c16eaca-6cd1-4435-9ab4-f0f14fdc72fe
created_at: '2025-12-13T09:00:33.969Z'
updated_at: '2025-12-13T09:00:33.969Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test for Web Cache Poisoning via Header Manipulation

## Summary

This procedure tests for web cache poisoning vulnerabilities by manipulating headers like X-Forwarded-Host to determine if the target improperly handles or validates them, potentially allowing cache poisoning that affects multiple users.

## Description

The procedure involves sending crafted requests to the target endpoint on okmedia.insideok.ru to check for reflection of unvalidated host values in responses. If vulnerable, this can lead to injection of malicious content into the cache, enabling attacks like stored XSS. It targets web applications with caching mechanisms and requires network access to the endpoint.

## Requirements

1. Network access to the target URL (okmedia.insideok.ru)
2. Tool for sending HTTP requests with custom headers (e.g., curl)
3. Basic understanding of HTTP headers and caching behavior

## Defense

Defensive measures and detection strategies:

- Implement strict validation and sanitization of untrusted headers like X-Forwarded-Host
- Use cache keys that exclude untrusted inputs and monitor for anomalous header values in logs

## Objectives

1. Identify if X-Forwarded-Host is reflected without validation
2. Confirm potential for cache poisoning
3. Assess risk of injecting malicious content

## Instructions

### Step 1: Send Test Request with Modified Header

**Context**: Send a request with a benign modified X-Forwarded-Host to check for reflection.

**Command** ([[commands/curl-set-x-forwarded-host]]):
```bash
curl -H "X-Forwarded-Host: test.example.com" https://okmedia.insideok.ru/
```

> This command sets a custom host header and retrieves the response; look for 'test.example.com' in the output to indicate vulnerability.

### Step 2: Analyze Response for Vulnerability

**Context**: Examine the response to see if the injected host is used in links or scripts without sanitization.

**Command** ([[commands/curl-set-x-forwarded-host]]):
```bash
curl -H "X-Forwarded-Host: test.example.com" https://okmedia.insideok.ru/ | grep "test.example.com"
```

> Pipe the output to grep to confirm if the test host appears, signaling improper handling.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-set-x-forwarded-host]]

## Tools Used

- [[tools/curl]]

## Tags

- web-cache-poisoning
- header-manipulation
