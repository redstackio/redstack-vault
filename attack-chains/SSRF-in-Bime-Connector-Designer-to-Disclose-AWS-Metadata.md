---
id: ac-uuid-001
name: SSRF in Bime Connector Designer to Disclose AWS Metadata
tags:
  - ssrf
  - aws
  - metadata
  - cloud
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-SSRF-in-Bime-Connector-Designer]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.692Z'
description: >-
  A server-side request forgery vulnerability in the Bime Connector Designer
  allows attackers to make arbitrary internal requests, leading to the exposure
  of sensitive AWS instance metadata.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SSRF in Bime Connector Designer to Disclose AWS Metadata

Multi-stage attack chain demonstrating exploitation of SSRF in Bime's Connector Designer to access internal AWS resources.

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
    A[Access Connector Designer] --> B[Configure Malicious URL]
    B --> C[Trigger Request and Exfiltrate Metadata]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or proxy tool like Burp Suite

### Target Environment

- Bime platform with Connector Designer feature enabled
- AWS-hosted instance (EC2) with metadata service accessible internally
- Network access to the Bime web application

### Initial Access Requirements

- Valid user account on Bime platform (authenticated access to Connector Designer)
- No special privileges required beyond standard user

## Detailed Attack Procedures

### Step 1: Exploit SSRF via Connector Configuration
procedure: [[procedures/Exploit-SSRF-in-Bime-Connector-Designer]]

**Objective**: Configure a connector in the Bime Designer to force the server to request internal AWS metadata endpoints, disclosing sensitive information.

**Instructions**: Log in to the Bime platform and navigate to the Connector Designer. Create a new connector for REST or Elastic Search, and in the URL field, input an internal AWS metadata URL such as `http://169.254.169.254/latest/meta-data/`. Save and trigger the connector to execute the request. The response will include leaked metadata like instance ID, IAM roles, or security credentials if present.

**Expected Output**: The connector execution returns AWS metadata in the response, such as JSON with instance details.

**Success Indicators**:
- Metadata fields (e.g., instance-id, local-hostname) appear in the connector output
- No validation errors on internal URLs

## Attack Chain Summary

### Key Achievements

1. Successful SSRF exploitation without authentication bypass
2. Disclosure of AWS instance metadata enabling further cloud resource access
3. Demonstration of arbitrary internal request capability

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
