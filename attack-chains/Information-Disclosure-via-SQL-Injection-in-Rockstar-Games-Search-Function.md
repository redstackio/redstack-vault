---
tags:
  - sqli
  - information-disclosure
  - web
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-sqli-test]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploit-SQL-Injection-for-Error-Disclosure]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  A single-stage attack exploiting a SQL Injection vulnerability in the search
  function to disclose detailed error codes, aiding further reconnaissance.
skill_level: beginner
impact_level: low
id: d5193873-efe7-4928-b22e-98bc990a1197
created_at: '2025-12-14T17:25:12.679Z'
updated_at: '2025-12-14T17:25:12.679Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Information Disclosure via SQL Injection in Rockstar Games Search Function

## Overview

This attack chain demonstrates the exploitation of a SQL Injection vulnerability in the search functionality at https://www.rockstargames.com/search. By injecting malicious payloads into the search input, attackers can trigger unintended error messages that reveal detailed SQL error codes. This information disclosure provides insights into the backend database structure and error handling, potentially aiding in more advanced attacks, though the severity is rated low due to limited direct impact.

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Search Input] --> B[Trigger SQL Error and Disclose Codes]
    B --> C[Analyze Disclosed Information]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or command-line tool like curl

### Target Environment

- Web platform
- Accessible public-facing search endpoint at https://www.rockstargames.com/search
- No authentication required

### Initial Access Requirements

- Direct internet access to the target URL
- No prior credentials or network position needed

## Detailed Attack Procedures

### Step 1: Trigger SQL Injection in Search
procedure: [[procedures/Exploit-SQL-Injection-for-Error-Disclosure]]

**Objective**: Inject a SQL payload into the search field to bypass normal query handling and force the display of detailed error messages containing SQL error codes.

**Instructions**: Use [[commands/curl-sqli-test]] to send a simple SQL injection payload to the search endpoint:

```bash
curl -X GET "https://www.rockstargames.com/search?q=' OR 1=1--" -v
```

Observe the response for error messages. Alternative payloads like `q=1'; SELECT * FROM users--` can be tested to elicit more specific errors.

**Expected Output**: HTTP response containing error messages with details like database type, table names, or query syntax errors (e.g., "SQL syntax error near ' OR 1=1'").

**Success Indicators**:
- Presence of SQL-related error codes in the response body
- Disclosure of backend database information

## Attack Chain Summary

### Key Achievements

1. Successful injection of SQL payload into public search function
2. Disclosure of sensitive error details without authentication
3. Low-risk reconnaissance for potential follow-on vulnerabilities

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01*
