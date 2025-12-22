---
tags:
  - web-cache-poisoning
  - dos
  - paypal
  - http-headers
type: attack_chain
tools: []
tactics:
  - '[[Lateral Movement]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-send-crafted-http-request]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Poison-Web-Cache-Using-Invalid-Transfer-Encoding-Header]]'
  - '[[procedures/Verify-Cache-Poisoning-Impact-on-JavaScript-Files]]'
step_count: 2
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Endpoint Denial of Service]]'
description: >-
  Exploitation of web cache poisoning vulnerability on PayPal to cause denial of
  service by poisoning cached JavaScript files
skill_level: intermediate
impact_level: high
id: 2724eb38-ba36-4225-a262-f2a490dbc4a5
created_at: '2025-12-13T09:01:16.925Z'
updated_at: '2025-12-13T09:01:16.925Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Lateral Movement]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Endpoint Denial of Service]]'
---
# Web Cache Poisoning on PayPal via Invalid Transfer-Encoding Header Leading to DoS

Multi-stage attack chain demonstrating web cache poisoning on paypal.com to replace critical JavaScript files with error responses, resulting in denial of service.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Crafted Request] --> B[Verify Poisoned Cache]
    B --> C[DoS Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specified, but HTTP client like curl is recommended

### Target Environment

- Web platform
- Services: paypal.com, www.paypalobjects.com
- Network access requirements: Public internet access to PayPal domains

### Initial Access Requirements

- No credentials required
- External network position
- Ability to send HTTP requests to public-facing web services

## Detailed Attack Procedures

### Step 1: Send Crafted HTTP Request to Poison Cache
procedure: [[procedures/Poison-Web-Cache-Using-Invalid-Transfer-Encoding-Header]]

**Objective**: Exploit the vulnerability by sending an invalid Transfer-Encoding header to poison the web cache with an error response.

**Instructions**: Use [[commands/curl-send-crafted-http-request]] to send the crafted request targeting JavaScript files on www.paypalobjects.com via paypal.com:

```bash
curl -H "Transfer-Encoding: invalid" -H "Host: www.paypalobjects.com" https://www.paypal.com/path/to/js/file.js
```

**Expected Output**: The server responds with '501 Not Implemented', which gets cached.

**Success Indicators**:
- Request sent successfully
- Cache stores the error response

### Step 2: Verify Cache Poisoning and DoS Impact
procedure: [[procedures/Verify-Cache-Poisoning-Impact-on-JavaScript-Files]]

**Objective**: Confirm that the poisoned cache serves error messages instead of legitimate JavaScript files, leading to DoS.

**Instructions**: Attempt to access the affected JavaScript file normally, such as by loading the PayPal page or directly requesting the file. Observe if the '501 Not Implemented' error is served from the cache.

```bash
curl https://www.paypalobjects.com/path/to/js/file.js
```

**Expected Output**: '501 Not Implemented' error instead of the JavaScript content.

**Success Indicators**:
- Error response served to users
- Core functionality disrupted (e.g., JavaScript fails to load)

## Attack Chain Summary

### Key Achievements

1. Successful poisoning of web cache with invalid header
2. Replacement of essential JavaScript files with error messages
3. Denial of service on PayPal core functionality

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Adversary-in-the-Middle]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Lateral Movement]]
- [[Impact]]

*Last updated: 2023-10-01*
