---
id: ac-uuid-001
name: Denial of Service via Crafted Content-Type Header in Rack
tags:
  - dos
  - rack
  - ruby
  - cve-2024-25126
  - resource-exhaustion
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Ruby
submitted: true
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Rack-Content-Type-DoS]]'
step_count: 1
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:48.731Z'
description: >-
  A single-stage attack exploiting inefficient parsing in Rack's media type
  parser to cause CPU exhaustion and deny service to web applications built with
  Ruby on Rails or similar frameworks using vulnerable Rack versions.
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Denial of Service via Crafted Content-Type Header in Rack

Multi-stage attack chain demonstrating a complete attack workflow. This chain focuses on exploiting a vulnerability in Rack's content type parsing to induce CPU exhaustion, leading to denial of service on affected web applications.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Send Crafted Request] --> B[Resource Exhaustion]
    B --> C[Service Disruption]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#e74c3c
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-send-crafted-header]]

### Target Environment

- Web applications using Rack versions >= 0.4 and < 3.0.9.1 or < 2.2.8.1
- Ruby-based frameworks like Rails
- Exposed HTTP endpoint (e.g., port 80 or 443)

### Initial Access Requirements

- Network access to the target web application
- No authentication required for public endpoints
- Ability to send HTTP requests

## Detailed Attack Procedures

### Step 1: Send Malicious Request
procedure: [[procedures/Exploit-Rack-Content-Type-DoS]]

**Objective**: Deliver a specially crafted Content-Type header to trigger inefficient parsing in Rack's media type parser, causing excessive CPU consumption and denying service to the application.

**Instructions**: Identify a target endpoint on the vulnerable Rack application. Use [[commands/curl-send-crafted-header]] to send an HTTP POST request with a malicious Content-Type header that includes nested or excessively long parameters, such as repeated charset definitions, to exploit the parsing inefficiency.

```bash
curl -X POST http://target-app.com/vulnerable-endpoint \
  -H "Content-Type: text/plain; charset=utf-8; charset=utf-8; charset=utf-8" \
  -d "dummy payload"
```

Repeat the request multiple times or automate with a script to amplify the effect, leading to resource exhaustion.

**Expected Output**: The server response may be delayed or timeout due to CPU spikes; monitoring tools like top or htop on the server would show high CPU usage from the Rack process.

**Success Indicators**:
- Server response time increases significantly (>10 seconds)
- CPU utilization on the target server exceeds 90%
- Application logs show parsing errors or hangs in media type processing

## Attack Chain Summary

### Key Achievements

1. Successful delivery of crafted Content-Type header to vulnerable Rack instance
2. Induction of CPU exhaustion leading to DoS
3. Disruption of service availability for the web application

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2024-10-01T00:00:00Z*
