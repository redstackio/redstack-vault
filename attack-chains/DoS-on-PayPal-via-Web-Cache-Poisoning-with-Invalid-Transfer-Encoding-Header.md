---
id: ac-paypal-cache-poisoning-dos
tags:
  - web-cache-poisoning
  - dos
  - transfer-encoding
  - paypal
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Craft-Malicious-Request-with-Invalid-Transfer-Encoding]]'
  - '[[procedures/Poison-Cache-for-JavaScript-Resources]]'
  - '[[procedures/Induce-Denial-of-Service-via-Poisoned-Cache]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:27:03.001Z'
description: >-
  A multi-step attack exploiting improper validation of the Transfer-Encoding
  header to poison web caches, replacing JavaScript files with error responses
  and causing denial of service on PayPal's core functionality.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Denial of Service]]'
---
# DoS on PayPal via Web Cache Poisoning with Invalid Transfer-Encoding Header

Multi-stage attack chain demonstrating a complete attack workflow exploiting web cache poisoning to disrupt PayPal's website functionality.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Malicious Request] --> B[Poison Cache] --> C[Trigger DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform (HTTPS-enabled sites with caching layers like CDNs)
- Required services/ports: HTTP/HTTPS on port 443
- Network access requirements: Direct internet access to target domain

### Initial Access Requirements

- No credentials required
- External network position (no internal access needed)
- Prior access not needed; attack targets public-facing web cache

## Detailed Attack Procedures

### Step 1: Craft and Send Malicious Request
procedure: [[procedures/Craft-Malicious-Request-with-Invalid-Transfer-Encoding]]

**Objective**: Send an HTTP request with an invalid Transfer-Encoding header to bypass validation and initiate cache poisoning.

**Instructions**: Use [[commands/curl-invalid-transfer-encoding]] to craft and send the request to the target endpoint:

```bash
curl -X POST https://www.paypal.com/ -H "Transfer-Encoding: invalid" -d "dummy payload"
```

Monitor the response for a 501 Not Implemented error, indicating the server processed the invalid header without proper sanitization.

**Expected Output**: HTTP 501 Not Implemented response from the server.

**Success Indicators**:
- Server accepts and responds to the invalid header without rejection
- No immediate error blocking the request

### Step 2: Poison Cache for JavaScript Resources
procedure: [[procedures/Poison-Cache-for-JavaScript-Resources]]

**Objective**: Leverage the invalid header to store a poisoned response in shared cache layers, targeting JavaScript files on a subdomain.

**Instructions**: Target resources on www.paypalobjects.com by sending requests that influence the cache. Use [[commands/curl-cache-poison-js]] to poison the cache for a specific JS file:

```bash
curl https://www.paypalobjects.com/path/to/script.js -H "Transfer-Encoding: invalid" -v
```

Repeat for multiple JS endpoints to ensure broad cache contamination. Verify by requesting the JS file from a different IP or incognito session.

**Expected Output**: Subsequent requests to the JS file return 501 Not Implemented instead of the actual script content.

**Success Indicators**:
- Cached responses show poisoned error pages
- JS files are inaccessible via cache hits

### Step 3: Induce Denial of Service
procedure: [[procedures/Induce-Denial-of-Service-via-Poisoned-Cache]]

**Objective**: Observe and confirm the DoS impact as users receive broken functionality due to missing JS files.

**Instructions**: Simulate user traffic by accessing paypal.com from cached clients. Use [[commands/curl-simulate-user]] to request the main site and check for broken JS loads:

```bash
curl https://www.paypal.com/ -v
```

Inspect browser console or network tab for failed JS loads returning 501 errors, leading to non-functional UI elements like login or payment forms.

**Expected Output**: Site loads but core features fail due to missing JavaScript, e.g., buttons not responding or forms not submitting.

**Success Indicators**:
- User sessions experience degraded functionality
- Widespread impact on cached users until cache expires or is cleared

## Attack Chain Summary

### Key Achievements

1. Successfully poisoned web cache using invalid Transfer-Encoding header
2. Replaced critical JS files with error responses on subdomain
3. Caused DoS disrupting PayPal's core website operations for affected users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Network Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
