---
id: 3c5cc7a3-cf40-4d0e-97e4-518a5f8f738f
name: Web-Cache-Deception-Unkeyed-Input-Cache-Poisoning
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:41.278214+00:00'
updated_at: '2023-04-06T03:56:41.293010+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
sub_techniques: []
tags:
  - '[[tags/Methodology 2]]'
  - '[[tags/Web Cache Deception]]'
  - cache-poisoning
  - unkeyed-input
commands:
  - '[[commands/curl-cache-poisoning-x-forwarded-host]]'
platforms:
  - Web
tools: []
validated: true
---

# Web-Cache-Deception-Unkeyed-Input-Cache-Poisoning

## Summary

This procedure demonstrates how to perform Web Cache Deception using un-keyed input to poison a web application's cache. By manipulating un-keyed headers like X-Forwarded-Host, an attacker can trick the cache into storing malicious content, which is then served to victims when they request the resource, enabling attacks such as phishing or malware delivery.

## Description

Web Cache Deception exploits caching mechanisms in web applications or CDNs by poisoning the cache with responses that include attacker-controlled content. In this methodology, un-keyed inputs—such as certain HTTP headers not used in cache key generation—are manipulated to inject malicious payloads. For example, setting the X-Forwarded-Host header to include a script tag can cause the cached response to reflect that payload. This technique is effective against applications that cache responses based on URL alone, ignoring header variations. It requires identifying vulnerable endpoints and can lead to persistent delivery of malicious content without direct interaction with the victim. The attack is particularly dangerous in shared caching environments like CDNs, where poisoned content affects multiple users.

## Requirements

1. Access to send HTTP requests to the target web application (e.g., via network connectivity).
2. A vulnerable web application or CDN that caches responses based on URL without keying on specific headers (e.g., X-Forwarded-Host).
3. Tools for crafting and sending custom HTTP requests, such as curl or a proxy like Burp Suite.
4. Knowledge of the target's domain and a non-cacheable parameter (e.g., 'buster') to isolate the poison.

## Defense

- Implement strict cache keying that includes sensitive headers (e.g., X-Forwarded-Host) in cache validation.
- Use input validation and sanitization on all headers to prevent injection of malicious content.
- Deploy cache-busting mechanisms or short TTLs for dynamic content.
- Monitor for anomalous requests with unusual header values and cache hit rates.
- Enable web application firewalls (WAFs) to detect and block header manipulation attempts.

## Objectives

1. Identify un-keyed inputs in HTTP headers that can be used for cache poisoning.
2. Craft and send a poisoned request to inject malicious content into the cache.
3. Verify that the poisoned cache serves the malicious payload to subsequent requests.

## Instructions

### Step 1: Identify Un-Keyed Inputs

**Context**: Review common HTTP headers and values that are often un-keyed in caching logic. These can be manipulated to poison the cache without affecting the cache key. Focus on headers like User-Agent, Cookie, and X-Forwarded-Host, as they are frequently overlooked.

Un-keyed inputs to target:
- Values: User-Agent
- Values: Cookie
- Header: X-Forwarded-Host
- Header: X-Host
- Header: X-Forwarded-Server
- Header: X-Forwarded-Scheme (in combination with X-Forwarded-Host)
- Header: X-Original-URL (Symfony-specific)
- Header: X-Rewrite-URL (Symfony-specific)

Use a proxy tool to inspect responses and confirm if these headers influence the cached content without changing the cache key.

### Step 2: Craft and Send Poisoned Request

**Context**: Construct a GET request to a cacheable resource, appending a unique 'buster' parameter to ensure the poison is isolated. Modify the X-Forwarded-Host header to inject a malicious payload, such as a script tag. This tricks the server into generating a response that embeds the payload, which gets cached.

**Command** ([[commands/curl-cache-poisoning-x-forwarded-host]]):
```bash
curl -X GET "http://$_TARGET_URL?buster=$BUSTER_PARAM" \
  -H "Host: $_TARGET_DOMAIN" \
  -H "X-Forwarded-Host: $_POISON_PAYLOAD" \
  -v
```

> This command sends a request with a buster parameter (e.g., a random string) to avoid poisoning unrelated caches. The X-Forwarded-Host header injects the payload (e.g., 'test"><script>alert(1)</script>'). If vulnerable, the server caches the response including the injected content. Expected output includes a 200 OK with Cache-Control headers indicating caching, and the response body reflecting the payload (e.g., in meta tags or HTML).

### Step 3: Verify Cache Poisoning

**Context**: Send a follow-up request without the buster or poison to check if the malicious content is served from cache. Monitor for the payload execution in the response.

Use the same curl command without the poison header:
```bash
curl -X GET "http://$_TARGET_URL" -H "Host: $_TARGET_DOMAIN" -v
```

> Look for the injected payload in the response body and Cache-Control headers showing a cache hit. Success is confirmed if the malicious script appears without re-sending the poison.
