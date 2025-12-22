---
tags:
  - idor
  - web
  - access-control
  - hashing
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-IDOR-in-Semrush-Marketplace]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:48.188Z'
description: >-
  Exploiting an Insecure Direct Object Reference (IDOR) vulnerability in the
  Semrush marketplace due to length restrictions in the hashing function,
  allowing unauthorized access to marketplace objects.
id: 117d627d-5d28-480c-93d5-1f6e5ee2f6c5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Account Discovery]]'
---
# IDOR in Semrush Marketplace via Hashing Length Restriction

Multi-stage attack chain demonstrating a complete attack workflow targeting the Semrush marketplace at https://market.semrush.com/. The vulnerability stems from length restrictions in the hashing function used for object references, enabling attackers to bypass access controls and access unauthorized marketplace objects, potentially leading to data exposure or manipulation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Marketplace] --> B[Exploit IDOR]
    B --> C[Unauthorized Object Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for parameter manipulation

### Target Environment

- Web platform
- Access to https://market.semrush.com/
- No specific ports or services beyond standard HTTPS (443)

### Initial Access Requirements

- Valid user account on Semrush marketplace (authenticated session)
- Network access to the internet
- No prior elevated access needed, but authentication enables the attack surface

## Detailed Attack Procedures

### Step 1: Exploit IDOR for Unauthorized Access
procedure: [[procedures/Exploit-IDOR-in-Semrush-Marketplace]]

**Objective**: Bypass access controls by manipulating object references limited by hashing function length restrictions to access unauthorized marketplace objects.

**Instructions**: Authenticate to the Semrush marketplace, identify an endpoint using hashed object IDs (e.g., via browser inspection), and manipulate the hash parameter to reference other objects. Use a proxy tool to intercept and modify requests, or directly alter URLs in the browser.

For example, if a legitimate object URL is `https://market.semrush.com/object/hash123`, attempt to shorten or guess adjacent hashes due to length limits, such as `https://market.semrush.com/object/hash12` to access unintended objects.

Verify access by checking for data from other users' objects, like listings or details not owned by the attacker.

**Expected Output**: Successful response containing unauthorized object data, such as private marketplace listings or user information.

**Success Indicators**:
- Response returns data not belonging to the authenticated user
- No access denied errors for manipulated references
- Potential exposure of sensitive marketplace objects

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls via IDOR exploitation
2. Accessed unauthorized marketplace objects
3. Demonstrated critical impact leading to data exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
