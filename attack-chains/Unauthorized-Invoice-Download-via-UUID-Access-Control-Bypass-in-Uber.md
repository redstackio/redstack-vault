---
tags:
  - broken-access-control
  - idor
  - uuid-bypass
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Bypass-Access-Controls-to-Download-Arbitrary-Invoices]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:36.659Z'
description: >-
  A broken access control vulnerability in Uber's invoice download feature
  allowing unauthorized users to access any invoice using its UUID without
  authentication or ownership verification.
skill_level: beginner
impact_level: high
id: 2637ef80-6dc8-41d5-86eb-0c017c574515
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Unauthorized Invoice Download via UUID Access Control Bypass in Uber

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via UUID] --> B[Download Invoice]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform
- Access to Uber's invoice download endpoint
- Knowledge of invoice UUID (can be guessed or enumerated)

### Initial Access Requirements

- No credentials required due to the vulnerability
- Network access to Uber's web services
- No prior access needed

## Detailed Attack Procedures

### Step 1: Access Invoice Download Endpoint
procedure: [[procedures/Bypass-Access-Controls-to-Download-Arbitrary-Invoices]]

**Objective**: Bypass authentication and authorization to download any user's invoice using a known or guessed UUID.

**Instructions**: Obtain or guess an invoice UUID, then use [[commands/curl-uuid-invoice-download]] to request the invoice from the endpoint without any auth headers.

```bash
curl -X GET "https://uber.com/api/invoice/download/{UUID}" -o stolen_invoice.pdf
```

Replace `{UUID}` with the target invoice's UUID. No authentication token is needed due to the flaw.

**Expected Output**: The invoice PDF file is downloaded successfully, containing sensitive financial data.

**Success Indicators**:
- HTTP 200 response with file content
- Downloaded file opens as a valid invoice PDF
- File contains data not belonging to the attacker's account

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls to access unauthorized invoices
2. Exposed sensitive financial information of other users
3. Demonstrated high-impact data exposure with minimal effort

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
