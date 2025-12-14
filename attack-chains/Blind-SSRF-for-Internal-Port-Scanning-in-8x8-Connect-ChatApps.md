---
tags:
  - ssrf
  - blind-ssrf
  - port-scanning
  - internal-network
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Blind-SSRF-for-Internal-Port-Scanning]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:46:09.490Z'
description: >-
  A multi-stage attack chain exploiting a Blind Server-Side Request Forgery
  (SSRF) vulnerability in the 8x8 Connect ChatApps module to perform internal
  port scanning and reveal network topology.
skill_level: intermediate
impact_level: high
id: e6ec4d2f-6b98-4bc6-b833-64743ed03b76
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Vulnerability Scanning]]'
---
# Blind SSRF for Internal Port Scanning in 8x8 Connect ChatApps

Multi-stage attack chain demonstrating a complete attack workflow exploiting a Blind SSRF vulnerability to scan internal ports.

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
    A[Initial Access via API] --> B[Blind SSRF Exploitation]
    B --> C[Internal Port Scanning]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-post-ssrf]]

### Target Environment

- Web platform with 8x8 Connect application
- Access to /api/v2/chats/image-check endpoint
- Network access to the public-facing API

### Initial Access Requirements

- No authentication required for the endpoint
- Ability to send HTTP POST requests
- Basic knowledge of JSON payloads

## Detailed Attack Procedures

### Step 1: Exploit Blind SSRF for Port Scanning
procedure: [[procedures/Exploit-Blind-SSRF-for-Internal-Port-Scanning]]

**Objective**: Send crafted requests to the vulnerable endpoint to trigger SSRF and infer open internal ports based on response behaviors like timing or success/failure.

**Instructions**: Use [[commands/curl-post-ssrf]] to send a POST request to the /api/v2/chats/image-check endpoint with a JSON payload containing a malicious URL targeting localhost on various ports. Modify the port in the URL (e.g., :22, :80) and observe responses to detect open ports.

```bash
curl -X POST https://connect.8x8.com/api/v2/chats/image-check \
  -H "Content-Type: application/json" \
  -d '{"url":"http://127.0.0.1:22/?a=a.png"}'
```

Repeat for different ports, such as 80, 443, 3306, etc., and note differences in response times or error messages indicating open services.

**Expected Output**: JSON response from the endpoint; successful SSRF may return faster responses or specific error codes for open ports, while closed ports time out or fail differently.

**Success Indicators**:
- Varied response times or error patterns correlating to port states
- Confirmation of open internal services like SSH (port 22) or HTTP (port 80)

## Attack Chain Summary

### Key Achievements

1. Successful exploitation of Blind SSRF to bypass URL validation
2. Inference of internal network topology through port scanning
3. Potential exposure of sensitive internal services without direct access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Vulnerability Scanning]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2024-01-01T00:00:00Z*
