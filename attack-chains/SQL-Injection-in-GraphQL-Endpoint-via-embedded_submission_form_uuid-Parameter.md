---
tags:
  - sql-injection
  - graphql
  - postgresql
  - rails
type: attack_chain
tools:
  - '[[tools/Curl-for-HTTP-Requests]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - PostgreSQL
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-SQL-Syntax-Error-in-Backend-Logs]]'
  - '[[procedures/Identify-SQL-Injection-Root-Cause-in-GraphQL-Handling]]'
  - '[[procedures/Reproduce-SQL-Injection-with-Malicious-Payload]]'
  - '[[procedures/Verify-Injection-Using-Timing-Attacks-with-pg_sleep]]'
  - '[[procedures/Investigate-Logs-for-Potential-Exploitation]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:09.965Z'
description: >-
  Multi-stage attack chain demonstrating discovery and exploitation of SQL
  injection in HackerOne's GraphQL endpoint, allowing arbitrary SQL execution in
  PostgreSQL schemas.
skill_level: intermediate
impact_level: high
id: 74754ec8-b57c-4db4-9100-c2579d468463
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection in GraphQL Endpoint via embedded_submission_form_uuid Parameter

Multi-stage attack chain demonstrating a complete attack workflow for discovering and exploiting a SQL injection vulnerability in the GraphQL endpoint of a Ruby on Rails application using PostgreSQL.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Log Discovery] --> B[Root Cause Analysis]
    B --> C[Payload Reproduction]
    C --> D[Timing Verification]
    D --> E[Exploitation Investigation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Curl-for-HTTP-Requests]]

### Target Environment

- Web platform with Ruby on Rails and GraphQL
- PostgreSQL database with public and secure schemas
- Access to backend logs (for discovery and investigation)
- Ports: 8080 (local), 443 (production HTTPS)

### Initial Access Requirements

- Network access to the /graphql endpoint
- Ability to monitor backend logs (internal access for discovery)
- No credentials required for public-facing exploitation

## Detailed Attack Procedures

### Step 1: Log Discovery
procedure: [[procedures/Discover-SQL-Syntax-Error-in-Backend-Logs]]

**Objective**: Identify potential SQL injection points by observing syntax errors in backend logs.

**Instructions**: Monitor the application's backend logs for PostgreSQL exceptions indicating unsanitized input.

**Expected Output**: PG::SyntaxError exception logged on November 6th, 2018, pointing to issues in GraphQL parameter handling.

**Success Indicators**:
- Exception observed in logs
- Indications of SQL syntax issues related to parameters

### Step 2: Root Cause Analysis
procedure: [[procedures/Identify-SQL-Injection-Root-Cause-in-GraphQL-Handling]]

**Objective**: Analyze the code to pinpoint the unsanitized parameter causing the injection.

**Instructions**: Review the Ruby on Rails code where the `embedded_submission_form_uuid` parameter is interpolated into PostgreSQL SET SESSION statements without sanitization.

**Expected Output**: Confirmation that GraphQL parameters are directly used in schema-switching queries, allowing injection.

**Success Indicators**:
- Identification of vulnerable code path
- Understanding of schema switching mechanism

### Step 3: Payload Reproduction
procedure: [[procedures/Reproduce-SQL-Injection-with-Malicious-Payload]]

**Objective**: Craft and send a malicious payload to confirm SQL injection execution.

**Instructions**: Use [[commands/curl-local-sql-injection-reproduce]] for local testing, then [[commands/curl-prod-sql-injection-reproduce]] for production confirmation. Observe response delays.

```bash
curl -X POST http://localhost:8080/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

```bash
curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%2830%29%3B--%27
```

**Expected Output**: Response delay of approximately 30 seconds, confirming SQL execution.

**Success Indicators**:
- Delayed response indicating pg_sleep execution
- No immediate errors, but confirmed injection

### Step 4: Timing Verification
procedure: [[procedures/Verify-Injection-Using-Timing-Attacks-with-pg_sleep]]

**Objective**: Validate the injection by measuring response times with varying sleep durations.

**Instructions**: Execute timed requests using [[commands/time-curl-1s-sleep]], [[commands/time-curl-5s-sleep]], [[commands/time-curl-10s-sleep]], and [[commands/time-curl-30s-sleep]] to correlate delays with payload.

```bash
time curl -X POST https://hackerone.com/graphql?embedded_submission_form_uuid=1%27%3BSELECT%201%3BSELECT%20pg_sleep%281%29%3B--%27
```

**Expected Output**: Response times matching sleep durations (e.g., ~1.631s for 1s sleep, ~10.557s for 10s sleep) with empty JSON response {}.

**Success Indicators**:
- Consistent delays across multiple tests
- Empty responses without syntax errors

### Step 5: Exploitation Investigation
procedure: [[procedures/Investigate-Logs-for-Potential-Exploitation]]

**Objective**: Check for signs of prior exploitation or abuse of the vulnerability.

**Instructions**: Query access and Rails logs using regular expressions to filter requests with suspicious parameters (e.g., single quotes in embedded_submission_form_uuid).

**Expected Output**: Log entries analyzed, confirming no exploitation occurred, but highlighting potential for information extraction from secure schemas.

**Success Indicators**:
- No evidence of abuse (e.g., non-200 responses or pg_sleep in wild)
- Assessment of high confidentiality risk

## Attack Chain Summary

### Key Achievements

1. Discovered SQL injection via log analysis
2. Reproduced and verified arbitrary SQL execution in PostgreSQL context
3. Assessed impact on schema switching and data confidentiality without actual exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
