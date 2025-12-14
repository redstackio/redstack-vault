---
id: ac-mod_deflate-dos-001
name: Denial of Service via mod_deflate Request Body Decompression Flaw
tags:
  - dos
  - resource-exhaustion
  - apache
  - mod_deflate
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-mod_deflate-Decompression-DoS]]'
step_count: 1
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T17:26:36.559Z'
description: >-
  A remote denial of service attack exploiting a resource consumption flaw in
  Apache httpd's mod_deflate module by sending specially crafted
  DEFLATE-compressed requests to exhaust server memory and CPU.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Denial of Service via mod_deflate Request Body Decompression Flaw

Multi-stage attack chain demonstrating a complete attack workflow targeting the mod_deflate module in Apache httpd.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access] --> B[Resource Exhaustion]
    B --> C[Denial of Service]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Apache httpd server with mod_deflate enabled for request body decompression (DEFLATE input filter)
- Vulnerable versions prior to 2.4.10-dev
- Open HTTP/HTTPS port (typically 80/443)

### Initial Access Requirements

- Network access to the target web server
- No credentials required (remote unauthenticated attack)
- Prior reconnaissance to confirm mod_deflate is active

## Detailed Attack Procedures

### Step 1: Trigger Resource Exhaustion
procedure: [[procedures/Exploit-mod_deflate-Decompression-DoS]]

**Objective**: Send a specially crafted DEFLATE-compressed request to cause the server to allocate excessive memory and CPU during decompression, leading to denial of service.

**Instructions**: Use a tool like curl to send a POST request with a malformed DEFLATE-compressed body that triggers the flaw. The crafted payload exploits the decompression handling to force unbounded resource usage.

First, prepare a crafted DEFLATE payload (e.g., a compressed body with repeating patterns or invalid blocks that cause expansion). Then execute the request using [[commands/curl-deflate-dos]]:

```bash
curl -X POST http://target-server.com/endpoint \
  -H "Content-Encoding: deflate" \
  --data-binary @crafted_deflate_payload.bin
```

Monitor server load during the request to confirm exhaustion.

**Expected Output**: The server becomes unresponsive, with high CPU/memory usage observed via monitoring tools like top or server logs showing decompression errors and resource spikes.

**Success Indicators**:
- Server response time increases dramatically or times out
- CPU utilization spikes to 100% on the target server
- New connections to the server are denied due to resource limits

## Attack Chain Summary

### Key Achievements

1. Successful remote triggering of resource exhaustion without authentication
2. Denial of service on the Apache httpd server, impacting availability
3. Demonstration of the mod_deflate flaw leading to significant performance degradation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Denial of Service]]

### MITRE ATT&CK Tactics

- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
