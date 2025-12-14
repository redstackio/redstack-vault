---
id: proc-paypal-invalid-header-craft
tags:
  - web-cache-poisoning
  - transfer-encoding
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-invalid-transfer-encoding]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:02.997Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-Request-with-Invalid-Transfer-Encoding

## Summary

This procedure crafts and sends an HTTP request with an invalid Transfer-Encoding header to a target web application, exploiting poor header validation to set the stage for cache poisoning attacks.

## Description

In the context of PayPal's vulnerability, the Transfer-Encoding header was not properly sanitized, allowing an invalid value like 'invalid' to be processed. This leads to the server generating a 501 Not Implemented response, which can be stored in caches if not filtered. The attack targets public-facing web apps with shared caching (e.g., CDNs), requiring only external network access. Expected outcome: Server accepts the request, enabling subsequent poisoning steps.

## Requirements

1. Network access to the target HTTPS endpoint (e.g., https://www.paypal.com/)
2. Tool like curl for crafting HTTP requests
3. Basic understanding of HTTP headers and caching mechanisms

## Defense

Defensive measures and detection strategies:

- Validate and strip unknown Transfer-Encoding values at the edge (e.g., via WAF rules)
- Implement cache key normalization to exclude suspicious headers
- Monitor for anomalous 501 responses in logs and cache hit rates

## Objectives

1. Trigger server processing of invalid header without rejection
2. Generate a poisonable error response
3. Prepare for cache contamination

## Instructions

### Step 1: Prepare the Malicious Request

**Context**: Identify the target endpoint and construct the request with the invalid header to test acceptance.

**Command** ([[commands/curl-invalid-transfer-encoding]]):
```bash
curl -X POST https://www.paypal.com/ -H "Transfer-Encoding: invalid" -d "dummy payload" -v
```

> This command sends a POST request with the invalid header. The -v flag enables verbose output to inspect headers and response. Expected output includes a 501 status if the header is processed.

### Step 2: Verify Header Processing

**Context**: Confirm the server did not reject the header outright, indicating vulnerability to poisoning.

**Command** ([[commands/curl-invalid-transfer-encoding]]):
```bash
curl -X GET https://www.paypal.com/ -H "Transfer-Encoding: invalid" -v
```

> Use GET for idempotent testing. Look for the 501 response in verbose logs, confirming the header influenced the response generation.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-invalid-transfer-encoding]]

## Tools Used

- [[tools/curl]]

## Tags

- web-cache-poisoning
- transfer-encoding
