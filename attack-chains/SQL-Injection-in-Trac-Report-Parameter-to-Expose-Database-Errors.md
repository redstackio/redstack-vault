---
id: ac-uuid-001
name: SQL Injection in Trac Report Parameter to Expose Database Errors
tags:
  - sqli
  - web
  - trac
  - database-error
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-SQL-Injection-in-Trac-Report-Parameter]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.322Z'
description: >-
  Demonstrates exploitation of an unsanitized 'report' parameter in the Trac
  ticket query endpoint to trigger SQL errors and potentially extract database
  information.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection in Trac Report Parameter to Expose Database Errors

Multi-stage attack chain demonstrating a complete attack workflow targeting the Trac ticket system on the Tor Project's website.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Web Query] --> B[Trigger SQL Injection]
    B --> C[Expose Database Errors]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[tools/curl]]

### Target Environment

- Web platform with Trac ticket system
- Services: Trac query endpoint
- Tech stack: Trac, Python
- Network access: Public internet to https://trac.torproject.org

### Initial Access Requirements

- No credentials required
- Direct public access to the Trac query URL
- No prior access needed

## Detailed Attack Procedures

### Step 1: Trigger SQL Injection
procedure: [[procedures/Trigger-SQL-Injection-in-Trac-Report-Parameter]]

**Objective**: Append a single quote to the 'report' parameter in the Trac query URL to break the SQL query and expose error messages revealing database structure.

**Instructions**: Construct and access the malicious URL using a browser or [[commands/curl-test-sqli-report]] to send the request:

```bash
curl "https://trac.torproject.org/projects/tor/query?status=closed&report=1'" -v
```

This injects a single quote after the report ID '1', causing a SQL syntax error if input is unsanitized.

**Expected Output**: HTTP response containing a SQL error message, such as a syntax error indicating unescaped input in the backend query.

**Success Indicators**:
- SQL syntax error displayed in the response body
- Database-related details leaked, like table names or query fragments

## Attack Chain Summary

### Key Achievements

1. Identified lack of input sanitization in the 'report' parameter
2. Triggered SQL error to confirm vulnerability
3. Demonstrated potential for further SQL injection to extract or manipulate ticket data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
