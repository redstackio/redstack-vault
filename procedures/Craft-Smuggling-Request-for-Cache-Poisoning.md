---
tags:
  - cache-poisoning
  - http-request-smuggling
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/craft-poisoning-request]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 16bf070e-03f5-4278-b698-d9c485423771
created_at: '2025-12-14T00:11:25.430Z'
updated_at: '2025-12-14T00:11:25.430Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft Smuggling Request for Cache Poisoning

## Summary

This procedure crafts an HTTP Request Smuggling payload to poison the cache by injecting a malicious redirect or content, enabling stored XSS on subsequent requests.

## Description

Using the identified smuggling vulnerability, construct a request that smuggles malicious content into the cache. For PayPal, this converts a page request into a cached redirect, poisoning the sign-in page.

## Requirements

1. Confirmed smuggling vulnerability
2. Payload for redirect or XSS
3. Tool for sending crafted HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement strict cache key validation
- Monitor cache hits for anomalous content

## Objectives

1. Inject malicious content into cache
2. Create persistent poisoning
3. Enable XSS delivery

## Instructions

### Step 1: Build Poisoning Payload

**Context**: Create a smuggling request with poisoning content.

**Command** ([[commands/craft-poisoning-request]]):

```bash
POST /signin HTTP/1.1
Host: paypal.com
Content-Length: 100
Transfer-Encoding: chunked

# Malicious chunk here
```

> Inject redirect to XSS payload.

### Step 2: Send and Confirm

**Context**: Transmit the request and verify poisoning.

**Command** ([[commands/craft-poisoning-request]]):

```bash
# Use tool to send
```

> Check cache response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/craft-poisoning-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[cache-poisoning]]
- [[http-request-smuggling]]
