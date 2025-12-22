---
id: 69960aa4-8578-4ce7-9945-de02db4de51b
name: Bypass-Rate-Limiting-with-X-Forwarded-For-Header
type: procedure
verified: true
submitted: true
created_at: '2020-08-22T16:20:51.836608+00:00'
updated_at: '2023-05-26T01:36:50.691914+00:00'
platforms:
  - Web
tags:
  - '[[tags/Rate Limiting]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Defense Evasion]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-send-multiple-login-requests]]'
  - '[[commands/curl-add-single-x-forwarded-for]]'
  - '[[commands/curl-add-duplicate-x-forwarded-for]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-Rate-Limiting-with-X-Forwarded-For-Header

## Summary

This procedure outlines a technique to bypass rate limiting on web application endpoints, such as login or forgot-password forms, by manipulating the X-Forwarded-For HTTP header. Rate limiting typically tracks requests based on IP address to prevent abuse, but misconfigurations can allow attackers to spoof or duplicate headers, evading the limit and enabling brute-force attacks or repeated submissions.

## Description

Rate limiting is a defense mechanism that restricts the number of requests from a single IP within a time window to mitigate denial-of-service or brute-force attempts. However, if the application parses the X-Forwarded-For header (used for proxy/load balancer scenarios) insecurely—such as by checking it multiple times or trusting duplicates—an attacker can bypass it by setting the header to a new IP value or repeating it. This procedure targets web applications vulnerable to such misconfigurations, often seen in login flows. The technique exploits the application's failure to properly validate or deduplicate proxy headers, allowing unlimited requests under the spoofed identity. It maps to MITRE ATT&CK technique T1190 (Exploit Public-Facing Application) under tactic TA0005 (Defense Evasion), as it circumvents protective controls on exposed web services.

## Requirements

- Access to a proxy tool like [[tools/Burp-Suite]] for intercepting and modifying HTTP requests.
- Knowledge of the target endpoint (e.g., /login or /forgot-password) and required POST parameters (e.g., username, password).
- Network access to the target web application.
- Optional: curl for command-line replication of requests.

## Defense

- Implement robust IP tracking that ignores or validates X-Forwarded-For headers, using only the actual client IP from the TCP connection.
- Use client-side fingerprints (e.g., TLS fingerprints, browser headers) in addition to IP-based limiting.
- Monitor for anomalous header patterns, such as duplicate X-Forwarded-For values, and log them for anomaly detection.
- Employ Web Application Firewalls (WAFs) that detect header manipulation attempts.

## Objectives

1. Trigger and observe rate limiting on the target endpoint to confirm its presence.
2. Attempt a single X-Forwarded-For header modification to verify it does not bypass the limit.
3. Use duplicate X-Forwarded-For headers to successfully evade the rate limit and receive a normal response.
4. Enable repeated requests for further exploitation, such as credential stuffing.

## Instructions

### Step 1: Observe Rate Limiting Behavior

**Context**: First, confirm the endpoint enforces rate limiting by sending multiple identical requests. This establishes a baseline where excessive requests from the same IP result in a 403 Forbidden response.

**Command** ([[commands/curl-send-multiple-login-requests]]):
```bash
for i in {1..10}; do curl -X POST http://target.com/login -d "username=test&password=test" -v; done
```

> This loop sends 10 POST requests to the login endpoint. The -v flag provides verbose output to monitor HTTP status codes. On success (initial requests), expect 200 OK or 401 Unauthorized; after the limit (e.g., 5 requests), expect 403 Forbidden indicating IP blocking.

### Step 2: Attempt Bypass with Single X-Forwarded-For Header

**Context**: Modify the request to include a single X-Forwarded-For header spoofing a different IP. This tests if the application trusts the header but still enforces limiting based on the original or parsed value, resulting in continued blocking.

**Command** ([[commands/curl-add-single-x-forwarded-for]]):
```bash
curl -X POST http://target.com/login -H "X-Forwarded-For: 1.2.3.4" -d "username=test&password=test" -v
```

> Repeat this command multiple times (e.g., 5-10). The header spoofs the originating IP as 1.2.3.4. If the bypass fails, responses remain 403 Forbidden, confirming the application parses but does not fully trust or reset the limit with a single header.

### Step 3: Bypass with Duplicate X-Forwarded-For Headers

**Context**: Exploit the misconfiguration by including the X-Forwarded-For header twice in the request. Some applications process the last occurrence or deduplicate insecurely, treating it as a new IP and resetting the rate limit counter, allowing successful responses.

**Command** ([[commands/curl-add-duplicate-x-forwarded-for]]):
```bash
curl -X POST http://target.com/login -H "X-Forwarded-For: 1.2.3.4" -H "X-Forwarded-For: 5.6.7.8" -d "username=test&password=test" -v
```

> Send this request multiple times. The duplicate headers (first 1.2.3.4, second 5.6.7.8) trick the application into seeing a 'new' IP. Expect 200 OK or 401 Unauthorized responses, indicating the rate limit bypass success. Use this to chain with brute-force tools for further exploitation.

If using [[tools/Burp-Suite]], intercept the request in the Proxy tab, forward to Repeater, add/modify headers in the Raw tab, and replay to replicate these steps graphically.
