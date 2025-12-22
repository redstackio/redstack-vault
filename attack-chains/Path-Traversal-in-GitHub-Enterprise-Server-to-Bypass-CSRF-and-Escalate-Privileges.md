---
tags:
  - path-traversal
  - csrf-bypass
  - privilege-escalation
  - github-enterprise
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Identify-Vulnerable-GitHub-Enterprise-Server-Instance]]'
  - '[[procedures/Exploit-Path-Traversal-for-CSRF-Bypass]]'
  - '[[procedures/Escalate-Privileges-via-Forged-Requests]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
description: >-
  Exploitation of a path traversal vulnerability in GitHub Enterprise Server to
  bypass CSRF protections and achieve privilege escalation
skill_level: intermediate
impact_level: high
id: 35b931ff-a486-4fbe-a4ce-093311764c9d
created_at: '2025-12-11T03:47:39.294Z'
updated_at: '2025-12-11T03:47:39.294Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0004]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1078]]'
---
# Path Traversal in GitHub Enterprise Server to Bypass CSRF and Escalate Privileges

Multi-stage attack chain demonstrating exploitation of a path traversal vulnerability in the GitHub Enterprise Server management console to bypass CSRF protections and escalate privileges. This attack targets versions prior to 3.5, requiring a logged-in user in the management console, and was patched in versions 3.1.19, 3.2.11, 3.3.6, and 3.4.1 under CVE-2022-23732.

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
    A[Initial Access] --> B[Exploit Vulnerability]
    B --> C[Privilege Escalation]
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None specific; web browser or HTTP client sufficient

### Target Environment

- GitHub Enterprise Server versions prior to 3.5
- Management Console service exposed
- Network access to the target server

### Initial Access Requirements

- Ability to interact with a logged-in user's session in the management console
- No prior credentials needed beyond targeting an active session

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Instance - [[procedures/Identify-Vulnerable-GitHub-Enterprise-Server-Instance]]

**Procedure**: [[procedures/Identify-Vulnerable-GitHub-Enterprise-Server-Instance]]

**Objective**: Confirm the target is running a vulnerable version of GitHub Enterprise Server and identify the management console endpoint.

**Expected Output**: Verification of version and active management console.

**Success Indicators**:
- Target version is prior to 3.5
- Management console is accessible and a user is logged in

### Step 2: Exploit Path Traversal - [[procedures/Exploit-Path-Traversal-for-CSRF-Bypass]]

**Procedure**: [[procedures/Exploit-Path-Traversal-for-CSRF-Bypass]]

**Objective**: Use path traversal to bypass CSRF protections in the management console.

**Expected Output**: Successful traversal allowing request forgery.

**Success Indicators**:
- CSRF token checks are bypassed
- Ability to submit forged requests

### Step 3: Escalate Privileges - [[procedures/Escalate-Privileges-via-Forged-Requests]]

**Procedure**: [[procedures/Escalate-Privileges-via-Forged-Requests]]

**Objective**: Forge requests on behalf of the logged-in user to escalate privileges.

**Expected Output**: Elevated access achieved.

**Success Indicators**:
- Privileges escalated to higher level
- Control over management console functions

## Attack Chain Summary

### Key Achievements

1. Identification of vulnerable GitHub Enterprise Server
2. Bypass of CSRF via path traversal
3. Privilege escalation through forged requests

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

*Last updated: 2023-10-01*
