---
id: ec2fc3a4-972d-4c80-931b-cc703282ac7a
name: WP-JSON API Cache Poisoning via Origin Header for CORS Denial of Service
type: attack_chain
description: >-
  Exploits cache poisoning in WordPress.com WP-JSON API by manipulating Origin
  headers to cause CORS failures and denial of service for cross-origin
  requests.
verified: false
submitted: true
step_count: 4
created_at: '2025-12-11T06:10:15.357Z'
updated_at: '2025-12-11T06:10:15.357Z'
procedures:
  - '[[procedures/WP-JSON-Cache-Poisoning-Procedure]]'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
tactics:
  - '[[Impact]]'
tags:
  - cache-poisoning
  - cors
  - dos
  - wordpress
platforms:
  - Web
  - WordPress.com
tools:
  - '[[tools/Browser-JavaScript-Console]]'
  - '[[tools/fetch-API]]'
  - '[[tools/publicwww.com]]'
commands:
  - '[[commands/fetch-wp-json-poison]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1499]]'
  - '[[T1190]]'
---

# WP-JSON API Cache Poisoning via Origin Header for CORS Denial of Service

Multi-stage attack chain demonstrating cache poisoning of the WP-JSON API on WordPress.com sites by echoing arbitrary Origin headers, leading to CORS misconfigurations and denial of service for legitimate cross-origin requests. This can disrupt frontend functionalities like headless WordPress setups.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initiate from External Origin] --> B[Poison Cache with Fetch Requests]
    B --> C[Switch Origins and Test]
    C --> D[Observe CORS Denial of Service]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Browser-JavaScript-Console]]
- [[tools/fetch-API]]
- [[tools/publicwww.com]] (optional for target discovery)

### Target Environment

- Web platform on WordPress.com
- WP-JSON API endpoints exposed
- Edge caches in use

### Initial Access Requirements

- Access to a web browser
- Ability to open HTTPS websites from different origins
- No credentials required; targets public-facing API

## Detailed Attack Procedures

### Step 1: Initiate from External Origin - [[procedures/WP-JSON-Cache-Poisoning-Procedure]]

**Procedure**: [[procedures/WP-JSON-Cache-Poisoning-Procedure]]

**Objective**: Set up the initial cross-origin context to begin poisoning the cache.

**Instructions**: Open an external HTTPS website (e.g., https://nathandavison.com) in your browser to trigger CORS behavior.

**Expected Output**: Browser console ready for JavaScript execution.

**Success Indicators**:
- External site loaded successfully
- JavaScript console accessible

### Step 2: Poison Cache with Fetch Requests - [[procedures/WP-JSON-Cache-Poisoning-Procedure]]

**Procedure**: [[procedures/WP-JSON-Cache-Poisoning-Procedure]]

**Objective**: Send multiple fetch requests to poison the cache with a specific Origin header.

**Instructions**: In the browser JavaScript console, execute the fetch command [[commands/fetch-wp-json-poison]] multiple times:

```javascript
fetch('https://██████████.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json))
```

This echoes the request's Origin in the Access-Control-Allow-Origin header and caches it without proper keying.

**Expected Output**: JSON response from WP-JSON API, with the header cached.

**Success Indicators**:
- Successful fetch responses logged
- No immediate errors

### Step 3: Switch Origins and Attempt Fetch - [[procedures/WP-JSON-Cache-Poisoning-Procedure]]

**Procedure**: [[procedures/WP-JSON-Cache-Poisoning-Procedure]]

**Objective**: Test the poisoned cache from a different origin to trigger CORS failure.

**Instructions**: Switch to another HTTPS website and execute the same fetch command [[commands/fetch-wp-json-poison]]:

```javascript
fetch('https://██████████.com/wp-json/?dontreallypoison1').then(res => res.json()).then(json => console.log(json))
```

**Expected Output**: Attempted fetch from new origin encounters poisoned cache.

**Success Indicators**:
- Request sent from new origin
- Cache serves poisoned response

### Step 4: Observe CORS Error - [[procedures/WP-JSON-Cache-Poisoning-Procedure]]

**Procedure**: [[procedures/WP-JSON-Cache-Poisoning-Procedure]]

**Objective**: Confirm the denial of service due to mismatched CORS headers.

**Instructions**: In the browser console, observe the CORS error where the cached Access-Control-Allow-Origin does not match the new origin.

**Expected Output**: Browser blocks the response with a CORS failure error.

**Success Indicators**:
- CORS error message in console
- Legitimate cross-origin requests denied

## Attack Chain Summary

### Key Achievements

1. Successful cache poisoning of WP-JSON API responses
2. Induced CORS failures for cross-origin requests
3. Denial of service for dependent services like headless frontends

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Impact]]

---

*Last updated: 2023-10-01*
