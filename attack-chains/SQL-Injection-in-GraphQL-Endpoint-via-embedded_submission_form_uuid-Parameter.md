---
tags:
  - sqli
  - graphql
  - postgresql
  - rails
  - web
type: attack_chain
tools:
  - '[[tools/curl]]'
  - '[[tools/time]]'
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
  - '[[procedures/Monitor-Backend-Logs-for-Errors]]'
  - '[[procedures/Analyze-Code-for-SQL-Injection-Root-Cause]]'
  - '[[procedures/Reproduce-SQL-Injection-Locally]]'
  - '[[procedures/Verify-SQL-Injection-on-Production]]'
  - '[[procedures/Analyze-Logs-for-Exploitation-Evidence]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:00.335Z'
description: >-
  Multi-stage vulnerability discovery and exploitation chain demonstrating SQL
  injection in HackerOne's GraphQL endpoint, allowing arbitrary SQL execution in
  PostgreSQL secure schemas.
skill_level: intermediate
impact_level: high
id: df785bda-ab74-42b1-9634-9f0d3e61af0e
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection in GraphQL Endpoint via embedded_submission_form_uuid Parameter

Multi-stage attack chain demonstrating the discovery, reproduction, and verification of a SQL injection vulnerability in HackerOne's /graphql endpoint, enabling arbitrary SQL execution against PostgreSQL databases with public and secure schemas.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Log Monitoring] --> B[Root Cause Analysis]
    B --> C[Local Reproduction]
    C --> D[Production Verification]
    D --> E[Exploitation Log Analysis]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]
- [[tools/time]]

### Target Environment

- Web platform with Ruby on Rails, GraphQL, PostgreSQL, nginx, and Unicorn
- Access to backend logs (nginx and Rails)
- Local development environment mirroring production (e.g., localhost:8080)

### Initial Access Requirements

- Internal access to backend logs and code
- Network access to production /graphql endpoint
- No prior credentials needed beyond standard user access

## Detailed Attack Procedures

### Step 1: Monitor Backend Logs for Errors
procedure: [[procedures/Monitor-Backend-Logs-for-Errors]]

**Objective**: Identify potential SQL syntax errors indicating injection vulnerabilities.

**Instructions**: Review backend logs for PG::SyntaxError exceptions, which signal unescaped SQL interpolation.

**Expected Output**: Log entries showing syntax errors from malformed queries.

**Success Indicators**:
- PG::SyntaxError observed in logs
- Timestamps correlating to user requests

### Step 2: Analyze Code for SQL Injection Root Cause
procedure: [[procedures/Analyze-Code-for-SQL-Injection-Root-Cause]]

**Objective**: Pinpoint the vulnerable parameter and query construction.

**Instructions**: Examine GraphQL parameter handling in Rails code, focusing on unsanitized interpolation into SET SESSION queries.

**Expected Output**: Identification of embedded_submission_form_uuid as the injection point.

**Success Indicators**:
- Code commit linked to vulnerability introduction
- Confirmation of direct SQL interpolation without escaping

### Step 3: Reproduce SQL Injection Locally
procedure: [[procedures/Reproduce-SQL-Injection-Locally]]

**Objective**: Validate the vulnerability in a controlled environment.

**Instructions**: Use [[commands/curl-local-sqli-repro]] to send a crafted POST request to the local GraphQL endpoint:

```bash
curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

**Expected Output**: Delayed response (30 seconds) confirming SQL execution.

**Success Indicators**:
- Response delay matches pg_sleep duration
- No immediate syntax error

### Step 4: Verify SQL Injection on Production
procedure: [[procedures/Verify-SQL-Injection-on-Production]]

**Objective**: Confirm exploitability in the live environment with time-based blind injection.

**Instructions**: Execute timed curl requests using [[commands/time-curl-prod-30s]] for varying delays:

```bash
(time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27)
```

Follow with shorter delays using [[commands/time-curl-prod-5s]] and [[commands/time-curl-prod-1s]] to measure response times.

**Expected Output**: Response times correlating to pg_sleep values (e.g., ~30s for 30s sleep).

**Success Indicators**:
- Measured delays (e.g., 30.123s for pg_sleep(30))
- Empty JSON response {}

### Step 5: Analyze Logs for Exploitation Evidence
procedure: [[procedures/Analyze-Logs-for-Exploitation-Evidence]]

**Objective**: Check historical logs for signs of prior exploitation.

**Instructions**: Query nginx and Rails logs using regex patterns for suspicious parameters containing single quotes or pg_sleep indicators.

**Expected Output**: Filtered log entries showing request patterns and status codes.

**Success Indicators**:
- No evidence of exploitation (e.g., 104 nginx matches, all 200 status)
- Aggregated Rails logs confirming no abuse

## Attack Chain Summary

### Key Achievements

1. Discovered SQL injection via log monitoring on November 6th, 2018
2. Reproduced arbitrary SQL execution, including schema switching and data extraction potential
3. Verified no prior exploitation through comprehensive log analysis

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
