---
tags:
  - ci-exposure
  - access-control
  - credential-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud
complexity: low
procedures:
  - '[[procedures/Access-Publicly-Exposed-CI-Instance]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of an improperly secured internal Continuous Integration instance
  at Snapchat, resulting in unauthorized access to source code and credentials
skill_level: beginner
impact_level: high
id: 43cedbb0-b5f3-4a11-8ab8-88d65714080f
created_at: '2025-12-11T06:10:25.017Z'
updated_at: '2025-12-11T06:10:25.017Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Publicly Accessible CI Instance Leading to Source Code and Credential Disclosure

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
    A[Initial Access] --> B[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (basic web access tools like a browser or curl)

### Target Environment

- Web and Cloud platforms
- Continuous Integration service exposed publicly
- Network access requirements: Public internet access to the target URL

### Initial Access Requirements

- No credentials required
- External network position
- No prior access needed

## Detailed Attack Procedures

### Step 1: Discover and Access Exposed CI Instance - [[procedures/Access-Publicly-Exposed-CI-Instance]]

**Procedure**: [[procedures/Access-Publicly-Exposed-CI-Instance]]

**Objective**: Identify and directly access the publicly exposed internal Continuous Integration instance to retrieve sensitive data such as source code and credentials.

**Expected Output**: Successful retrieval of internal source code and instance credentials without authentication.

**Success Indicators**:
- Ability to browse or download files from the CI instance
- Exposure of sensitive information like API keys or source repositories

Use standard web reconnaissance to locate the exposed endpoint (e.g., via search engines or subdomain enumeration if needed), then directly navigate to it using a web browser or tool like curl:

```bash
curl https://exposed-ci-instance.snapchat.internal/
```

Verify access by checking for unprotected directories or build artifacts containing source code and credentials.

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to internal CI tools
2. Disclosure of source code repositories
3. Exposure of instance credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

*Last updated: [TIMESTAMP]*
