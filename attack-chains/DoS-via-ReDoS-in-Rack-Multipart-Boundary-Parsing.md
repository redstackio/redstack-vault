---
id: ac18ee8d-c687-4d77-800a-0baa17201432
name: DoS via ReDoS in Rack Multipart Boundary Parsing
type: attack_chain
description: >-
  A denial of service attack exploiting a ReDoS vulnerability in Rack's
  multipart parsing to consume excessive CPU resources in Ruby on Rails
  applications.
verified: false
submitted: true
step_count: 1
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.838Z'
procedures:
  - '[[procedures/Submit-Crafted-Multipart-POST-to-Trigger-ReDoS-in-Rack]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
tags:
  - dos
  - redos
  - rack
  - ruby
  - rails
  - multipart
platforms:
  - Web
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---

# DoS via ReDoS in Rack Multipart Boundary Parsing

Multi-stage attack chain demonstrating a complete attack workflow targeting vulnerable Rack-based applications.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Crafted Request] --> B[DoS Execution]
    B --> C[Resource Exhaustion]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP clients like curl)

### Target Environment

- Ruby on Rails applications using Rack >= 2.0.0 for multipart parsing
- Web server exposing endpoints that handle multipart/form-data POST requests (e.g., file uploads)
- Vulnerable Ruby versions before 3.2 without memoization

### Initial Access Requirements

- Network access to the target web application
- No authentication required if the endpoint is public
- Ability to send custom HTTP requests

## Detailed Attack Procedures

### Step 1: Submit Crafted Multipart Request
procedure: [[procedures/Submit-Crafted-Multipart-POST-to-Trigger-ReDoS-in-Rack]]

**Objective**: Exploit the ReDoS vulnerability in Rack's RFC2183 boundary parsing to cause excessive CPU consumption and deny service to the application.

**Instructions**: Craft a multipart POST request with a boundary string designed to trigger catastrophic backtracking in the vulnerable regex. Use [[commands/curl-multipart-redos-rack]] to send the request to a vulnerable upload endpoint:

```bash
curl -X POST http://target.example.com/upload \
  -H "Content-Type: multipart/form-data; boundary=evil-boundary" \
  --data-binary @crafted_payload.txt
```

Monitor server CPU usage during the request to confirm the DoS effect.

**Expected Output**: The request hangs or takes excessively long (seconds to minutes), while CPU spikes to 100% on the server parsing the multipart data.

**Success Indicators**:
- Server response delayed or timed out
- High CPU utilization observed on the target application server
- Application becomes unresponsive to subsequent requests

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of ReDoS in Rack's boundary parsing
2. Consumption of excessive CPU resources leading to DoS
3. Impact on Rails applications without updated Ruby or Rack mitigations

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Impact]]

---
*Last updated: 2024-01-01T00:00:00Z*
