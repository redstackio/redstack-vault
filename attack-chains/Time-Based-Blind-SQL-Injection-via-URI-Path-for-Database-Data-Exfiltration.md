---
tags:
  - sqli
  - blind-sqli
  - time-based
  - web
  - database-exfiltration
type: attack_chain
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-test-time-based-sqli]]'
  - '[[commands/sqlmap-time-based-extraction]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-Time-Based-Blind-SQL-Injection]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  A multi-stage attack exploiting a blind SQL injection vulnerability in the URI
  path of a web application to infer and extract sensitive database information
  using time-based delays.
skill_level: intermediate
impact_level: high
id: c8b963d3-0652-4476-89c2-c3304f130ffd
created_at: '2025-12-14T17:26:17.741Z'
updated_at: '2025-12-14T17:26:17.741Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based Blind SQL Injection via URI Path for Database Data Exfiltration

Multi-stage attack chain demonstrating exploitation of a blind SQL injection vulnerability in the URI path of the Mars web application to extract sensitive data via time-based inference.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Test Time-Based Injection]
    B --> C[Extract Database Data]
    C --> D[Exfiltrate Sensitive Information]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sqlmap]]
- curl (standard HTTP client)

### Target Environment

- Web application with SQL backend (e.g., MySQL, PostgreSQL)
- Exposed URI path handling user input directly in SQL queries
- Network access to the web server (port 80/443 typically)

### Initial Access Requirements

- No credentials required (public-facing application)
- Direct network connectivity to the target web app
- Basic knowledge of SQL syntax and HTTP requests

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint

procedure: [[procedures/Exploit-Time-Based-Blind-SQL-Injection]]

**Objective**: Locate the URI path susceptible to SQL injection by testing for input reflection in database queries.

**Instructions**: Use manual probing or automated scanning to identify endpoints. Start with common paths like /api/user?id=1 and append SQL payloads to check for injection points.

Execute [[commands/curl-test-time-based-sqli]] to probe the URI path:

```bash
curl "http://mars.example.com/vulnerable/path'; SLEEP(5); --" -w "%{time_total}\n"
```

**Expected Output**: A response delay of approximately 5 seconds indicates a successful injection point.

**Success Indicators**:
- HTTP response time exceeds baseline by the sleep duration
- No error messages, but consistent delays confirm blind injection

### Step 2: Test Time-Based Injection

procedure: [[procedures/Exploit-Time-Based-Blind-SQL-Injection]]

**Objective**: Confirm the blind SQL injection vulnerability using time-based techniques to infer boolean conditions without direct output.

**Instructions**: Craft payloads that cause database delays based on true/false conditions. For example, use conditional SLEEP functions to test database version or structure.

Execute [[commands/curl-test-time-based-sqli]] with a conditional payload:

```bash
curl "http://mars.example.com/vulnerable/path' AND IF(1=1, SLEEP(5), 0); --" -w "%{time_total}\n"
```

**Expected Output**: Delay on true conditions (e.g., 5 seconds), no delay on false, allowing inference of data.

**Success Indicators**:
- Selective delays based on payload conditions
- Ability to chain conditions for bit-by-bit data extraction

### Step 3: Extract Database Data

procedure: [[procedures/Exploit-Time-Based-Blind-SQL-Injection]]

**Objective**: Systematically extract sensitive data such as user credentials or database schema by binary searching with time delays.

**Instructions**: Use automated tools for efficiency. Enumerate database name, tables, and columns via conditional delays, then dump data character by character.

Execute [[commands/sqlmap-time-based-extraction]] to automate extraction:

```bash
sqlmap -u "http://mars.example.com/vulnerable/path" --technique=T --dbms=mysql --dump
```

**Expected Output**: Inferred data output via timing analysis, such as database contents printed to console.

**Success Indicators**:
- Successful extraction of database structure (e.g., table names)
- Retrieval of sensitive data like user records

## Attack Chain Summary

### Key Achievements

1. Identification of blind SQLi in URI path without visible errors
2. Inference of database details using time-based delays
3. Critical data exfiltration leading to unauthorized access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

*Last updated: 2023-10-01T00:00:00Z*
