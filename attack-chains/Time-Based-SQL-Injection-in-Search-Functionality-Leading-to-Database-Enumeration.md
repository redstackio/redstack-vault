---
tags:
  - sql-injection
  - time-based
  - blind
  - mysql
  - web
  - enumeration
type: attack_chain
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
complexity: medium
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Observe-Search-Anomalies-for-Injection]]'
  - '[[procedures/Craft-HTTP-Request-File-for-SQLi-Testing]]'
  - '[[procedures/Exploit-Time-Based-SQL-Injection-with-sqlmap]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:52.764Z'
description: >-
  Multi-stage attack exploiting a time-based SQL injection vulnerability in the
  U.S. Department of State website's search endpoint to enumerate databases and
  potentially access sensitive data.
skill_level: intermediate
impact_level: high
id: 49462302-36fe-4115-98b4-f9b1977c1af6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based SQL Injection in Search Functionality Leading to Database Enumeration

Multi-stage attack chain demonstrating the discovery and exploitation of a time-based SQL injection vulnerability in the search functionality of the U.S. Department of State website, allowing database enumeration and potential unauthorized access to sensitive information.

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
    A[Observe Anomalies] --> B[Craft Request] --> C[Exploit with sqlmap] --> D[Database Enumeration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sqlmap]]

### Target Environment

- Web application with search functionality
- MySQL backend database
- Network access to the target website (e.g., https://www.state.gov)
- No authentication required for search endpoint

### Initial Access Requirements

- Public internet access to the target
- No prior credentials needed
- Basic knowledge of HTTP requests and SQL

## Detailed Attack Procedures

### Step 1: Observe Search Anomalies
procedure: [[procedures/Observe-Search-Anomalies-for-Injection]]

**Objective**: Identify potential SQL injection points by monitoring unusual behavior in search results.

**Instructions**: Navigate to the search endpoint (e.g., /search?query=) and input various test strings to observe gaps or delays in results.

**Expected Output**: Unusual gaps, delays, or errors in search results indicating unsanitized input handling.

**Success Indicators**:
- Anomalous response times or missing results for specific inputs
- Confirmation of potential injection via manual testing

### Step 2: Craft HTTP Request File
procedure: [[procedures/Craft-HTTP-Request-File-for-SQLi-Testing]]

**Objective**: Prepare a reusable HTTP request file capturing the vulnerable POST request for automated testing.

**Instructions**: Use a proxy like Burp Suite to intercept and save the POST request to /search with form-urlencoded data, including necessary headers.

**Expected Output**: A valid request.txt file ready for sqlmap input.

**Success Indicators**:
- File contains complete POST request with search parameter
- Request can be replayed manually without errors

### Step 3: Exploit with sqlmap
procedure: [[procedures/Exploit-Time-Based-SQL-Injection-with-sqlmap]]

**Objective**: Confirm the time-based SQL injection and enumerate databases using automated exploitation.

**Instructions**: Execute [[commands/sqlmap-enumerate-databases]] to test the request file and list databases:

```bash
sqlmap -r request.txt --dbs
```

**Expected Output**: Detection of time-based blind SQL injection and a list of 6 databases (e.g., information_schema, mysql).

**Success Indicators**:
- sqlmap confirms MySQL backend and injection vulnerability
- Successful enumeration of database names without data extraction

## Attack Chain Summary

### Key Achievements

1. Identified time-based SQL injection in search parameter
2. Crafted request file for reproducible testing
3. Enumerated 6 databases, enabling potential full data dump and unauthorized access

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2024-01-01T00:00:00Z*
