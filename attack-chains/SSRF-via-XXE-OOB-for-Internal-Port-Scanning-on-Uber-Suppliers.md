---
tags:
  - ssrf
  - xxe
  - oob
  - port-scanning
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-send-xxe-payload]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-XXE-OOB-for-SSRF-via-POST-Requests]]'
  - '[[procedures/Analyze-Error-Messages-for-Port-Status-Inference]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Multi-stage attack exploiting SSRF via XXE OOB to perform internal port
  scanning by analyzing error message discrepancies.
skill_level: intermediate
impact_level: high
id: bcb38857-4b30-4204-990a-ea42bdb4eec1
created_at: '2025-12-13T09:00:27.523Z'
updated_at: '2025-12-13T09:00:27.523Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF via XXE OOB for Internal Port Scanning on Uber Suppliers

Multi-stage attack chain demonstrating exploitation of a Server-Side Request Forgery (SSRF) vulnerability via XML External Entity (XXE) Out-of-Band (OOB) on usuppliers.uber.com to scan and identify open internal ports by sending crafted POST requests and analyzing error message variations.

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
    A[Send XXE Payloads] --> B[Analyze Errors]
    B --> C[Identify Open Ports]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None specified; basic HTTP client like curl

### Target Environment

- Web application on usuppliers.uber.com
- Vulnerable to XXE in POST endpoints
- Network access to the target domain

### Initial Access Requirements

- Public access to the web endpoint
- Ability to send HTTP POST requests
- No credentials required

## Detailed Attack Procedures

### Step 1: Send Payloads to Exploit XXE OOB for SSRF
procedure: [[procedures/Exploit-XXE-OOB-for-SSRF-via-POST-Requests]]

**Objective**: Trigger SSRF by sending crafted XML payloads in POST requests to exploit XXE OOB, targeting internal ports.

**Instructions**: Use [[commands/curl-send-xxe-payload]] to send a POST request with an XXE payload that attempts to connect to internal ports, such as:

```bash
curl -X POST https://usuppliers.uber.com/vulnerable-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://internal-ip:port">]><foo>&xxe;</foo>'
```

Repeat with variations in the entity to target different ports and observe responses.

**Expected Output**: Server responses with error messages that vary based on port status.

**Success Indicators**:
- Payload accepted by server
- Error messages returned in responses

### Step 2: Analyze Error Messages
procedure: [[procedures/Analyze-Error-Messages-for-Port-Status-Inference]]

**Objective**: Examine discrepancies in error messages to infer which internal ports are open.

**Instructions**: Collect responses from the previous step and compare error messages. For example, a "connection refused" error might indicate a closed port, while a timeout or different error could indicate an open port. Manually review or script the analysis of response variations.

**Expected Output**: List of inferred open internal ports.

**Success Indicators**:
- Variations in error messages identified
- Open ports successfully mapped

## Attack Chain Summary

### Key Achievements

1. Exploitation of XXE OOB to trigger SSRF
2. Internal port scanning via error analysis
3. Potential for targeted attacks on discovered services

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

*Last updated: 2023-10-01*
