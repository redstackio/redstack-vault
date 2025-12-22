---
tags:
  - web-cache-poisoning
  - http-headers
  - paypal
type: procedure
tools: []
tactics:
  - '[[Lateral Movement]]'
commands:
  - '[[commands/curl-send-crafted-http-request]]'
platforms:
  - Web
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 69143e28-9d69-4c0c-a91e-d8f7023ce077
created_at: '2025-12-13T09:01:16.922Z'
updated_at: '2025-12-13T09:01:16.922Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Poison Web Cache Using Invalid Transfer-Encoding Header

## Summary

This procedure exploits a web cache poisoning vulnerability by sending an HTTP request with an invalid Transfer-Encoding header, causing the cache to store an error response that replaces legitimate content, such as JavaScript files, leading to denial of service.

## Description

The attack targets web caching systems that improperly handle invalid Transfer-Encoding headers. By crafting a request to paypal.com that affects resources on www.paypalobjects.com, the cache stores a '501 Not Implemented' error. This poisoned response is then served to users, disrupting access to critical JavaScript files and causing DoS on core PayPal functionality. The procedure was discovered through testing various HTTP request headers.

## Requirements

1. Access to an HTTP client like curl
2. Public network access to paypal.com and www.paypalobjects.com
3. Knowledge of target JavaScript file paths

## Defense

Defensive measures and detection strategies:

- Implement strict validation of HTTP headers in caching systems
- Monitor for anomalous HTTP requests with invalid headers in web server logs

## Objectives

1. Poison the web cache with an error response
2. Replace legitimate JavaScript files in the cache
3. Achieve denial of service on affected resources

## Instructions

### Step 1: Craft and Send Invalid Header Request

**Context**: Send a request with an invalid Transfer-Encoding header to trigger the cache poisoning.

**Command** ([[commands/curl-send-crafted-http-request]]):
```bash
curl -H "Transfer-Encoding: invalid" -H "Host: www.paypalobjects.com" https://www.paypal.com/path/to/js/file.js
```

> This command sends the invalid header, causing the server to respond with '501 Not Implemented', which poisons the cache for the specified resource.

### Step 2: Repeat for Multiple Resources if Needed

**Context**: Target additional JavaScript files to broaden the DoS impact.

**Command** ([[commands/curl-send-crafted-http-request]]):
```bash
curl -H "Transfer-Encoding: invalid" -H "Host: www.paypalobjects.com" https://www.paypal.com/another/path/to/js/file.js
```

> Repeat the request for other critical files to ensure widespread cache poisoning.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques



## Commands Used

- [[commands/curl-send-crafted-http-request]]

## Tools Used



## Tags

- [[web-cache-poisoning]]
- [[http-headers]]
