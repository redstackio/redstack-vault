---
tags:
  - sqli
  - sql-injection
  - database-extraction
  - revive-adserver
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/nano]]'
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - MySQL
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Intercept-HTTP-Request-with-Burp-Suite]]'
  - '[[procedures/Save-Burp-Request-to-File-with-Nano]]'
  - '[[procedures/Exploit-SQL-Injection-with-SQLMap]]'
step_count: 6
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.255Z'
description: >-
  Authenticated SQL injection attack on Revive Adserver v6.0.0 via the 'keyword'
  parameter in admin-search.php, enabling database enumeration, extraction,
  modification, and potential server command execution using Burp Suite and
  SQLMap.
skill_level: intermediate
impact_level: high
id: 00d2b751-7d98-474e-b1b8-2b852b015bb3
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Error-Based and Time-Based SQL Injection in Revive Adserver Admin Search for Full Database Access

Multi-stage attack chain demonstrating exploitation of an SQL injection vulnerability in Revive Adserver v6.0.0, allowing authenticated attackers with manager access to inject payloads into the 'keyword' GET parameter of admin-search.php. The flaw stems from unsanitized input via phpAds_registerGlobalUnslashed() and improper escaping in PEAR MDB2's matchPattern function, enabling error-based (EXTRACTVALUE) and time-based (SLEEP) injections for full database access, data extraction, modification, deletion, and potential server command execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Burp Suite] --> B[Navigate to Endpoint]
    B --> C[Capture Request]
    C --> D[Save Request File]
    D --> E[Run SQLMap Enumeration]
    E --> F[Observe Database Dump]

    style A fill:#e74c3c
    style B fill:#e74c3c
    style C fill:#f39c12
    style D fill:#f39c12
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- [[tools/nano]]
- [[tools/sqlmap]]

### Target Environment

- Revive Adserver v6.0.0 running on PHP with MySQL backend
- Web platform accessible via HTTP
- Services: MySQL on default port 3306 (internal)
- Tech stack: PHP, PEAR MDB2

### Initial Access Requirements

- Authenticated session as manager-level user
- Local or network access to the admin panel (e.g., http://localhost/www/admin/)
- No prior access beyond authentication needed

## Detailed Attack Procedures

### Step 1: Launch Burp Suite for Traffic Interception
procedure: [[procedures/Intercept-HTTP-Request-with-Burp-Suite]]

**Objective**: Set up Burp Suite to monitor and intercept HTTP traffic to the target application.

**Instructions**: Launch Burp Suite and configure its proxy to intercept requests from the built-in browser.

**Expected Output**: Burp Suite interface active with proxy listener on port 8080.

**Success Indicators**:
- Burp Suite starts without errors
- Proxy tab shows listener configured

### Step 2: Navigate to Vulnerable Endpoint
procedure: [[procedures/Intercept-HTTP-Request-with-Burp-Suite]]

**Objective**: Access the admin search page to prepare for payload injection.

**Instructions**: Use Burp's built-in browser to navigate to http://localhost/www/admin/admin-search.php?keyword=FUZZ&compact=t, replacing FUZZ with a test value.

**Expected Output**: The search page loads, ready for request capture.

**Success Indicators**:
- Page renders without errors
- Authentication prompt passes with manager credentials

### Step 3: Capture the HTTP Request
procedure: [[procedures/Intercept-HTTP-Request-with-Burp-Suite]]

**Objective**: Intercept the GET request containing the vulnerable 'keyword' parameter.

**Instructions**: Submit a search query to trigger the request interception in Burp's Proxy > Intercept tab.

**Expected Output**: Captured GET request visible in Burp, showing keyword parameter.

**Success Indicators**:
- Request halted in Burp for inspection
- Parameter 'keyword' present in URL

### Step 4: Save Captured Request to File
procedure: [[procedures/Save-Burp-Request-to-File-with-Nano]]

**Objective**: Export the intercepted request to a file for use with SQLMap.

**Instructions**: In Burp, right-click the request and export it to testsql.txt using the nano editor to save.

**Expected Output**: File testsql.txt created with HTTP request details.

**Success Indicators**:
- File saved successfully
- Contents verify as valid HTTP request with keyword parameter

### Step 5: Run SQLMap to Exploit Vulnerability
procedure: [[procedures/Exploit-SQL-Injection-with-SQLMap]]

**Objective**: Use SQLMap to inject payloads and enumerate databases.

**Instructions**: Execute [[commands/sqlmap-enumerate-databases-via-http-request]] to load the request file and dump database names.

```bash
sqlmap -r testsql.txt --dbs
```

**Expected Output**: SQLMap detects injection and lists accessible databases.

**Success Indicators**:
- Injection confirmed (error-based or time-based)
- Database names outputted

### Step 6: Observe Database Extraction
procedure: [[procedures/Exploit-SQL-Injection-with-SQLMap]]

**Objective**: Validate full database access and potential for further exploitation.

**Instructions**: Review SQLMap output for enumerated databases and proceed to dump tables if needed (e.g., add --tables).

**Expected Output**: List of databases like 'revive_adserver', confirming access.

**Success Indicators**:
- Databases enumerated successfully
- No errors in SQLMap execution
- Potential for data extraction or modification

## Attack Chain Summary

### Key Achievements

1. Intercepted and prepared vulnerable HTTP request
2. Exploited SQL injection to enumerate databases
3. Achieved full read/write access to sensitive adserver data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
