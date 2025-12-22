---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: SQL Injection via URL Parameter on DoD Website to Expose Sensitive Data
tags:
  - sqli
  - web
  - dod
  - injection
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Demonstrate-SQL-Injection-via-URL-Parameter]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.923Z'
description: >-
  A single-stage attack exploiting a SQL injection vulnerability in a URL
  parameter on a U.S. Department of Defense website to execute arbitrary SQL
  commands and risk exposing sensitive data.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection via URL Parameter on DoD Website to Expose Sensitive Data

Multi-stage attack chain demonstrating a complete attack workflow.

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
    A[Discovery and Exploitation] --> B[Data Exposure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Target OS/Platform: Web application
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Public internet access to the DoD website

### Initial Access Requirements

- Credential requirements: None (public-facing)
- Network position: External attacker
- Prior access needed: None

## Detailed Attack Procedures

### Step 1: Discovery and Exploitation
procedure: [[procedures/Demonstrate-SQL-Injection-via-URL-Parameter]]

**Objective**: Identify and exploit a SQL injection vulnerability in a URL parameter to execute arbitrary SQL commands and potentially extract sensitive data from the DoD website database.

**Instructions**: Craft a specially formatted URL with a SQL payload to test for injection. Use [[commands/curl-sqli-test]] to send a request to the vulnerable endpoint, such as a search or ID parameter in the URL.

```bash
curl "https://dod-website.example.com/page?id=1' OR '1'='1" -v
```

Observe the response for signs of successful injection, such as error messages revealing database details or unexpected data dumps. Escalate by injecting UNION-based queries to extract data.

```bash
curl "https://dod-website.example.com/page?id=1' UNION SELECT username, password FROM users--" -v
```

**Expected Output**: Database errors, full page dumps, or extracted sensitive data like usernames and passwords in the response body.

**Success Indicators**:
- SQL syntax errors in response indicating lack of sanitization
- Unauthorized data exposure, such as listing of database contents
- Confirmation of arbitrary SQL execution

## Attack Chain Summary

### Key Achievements

1. Identified SQL injection point in URL parameter
2. Demonstrated arbitrary SQL command execution
3. Highlighted risk of sensitive DoD data exposure

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T12:00:00Z*
