---
id: ac-mtn-sqli-dump-001
tags:
  - sqli
  - web
  - database
  - recon
  - exploitation
type: attack_chain
tools:
  - '[[tools/Google-Dorks]]'
  - '[[tools/SQLMap]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Reconnaissance-Using-Google-Dorks-for-MTN-Sites]]'
  - '[[procedures/Testing-SQL-Injection-in-URL-Parameters]]'
  - '[[procedures/Manual-SQL-Injection-Exploitation]]'
  - '[[procedures/Automated-SQL-Injection-with-SQLMap]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.513Z'
description: >-
  Multi-stage attack exploiting SQL injection in the customerId URL parameter on
  admyntec.co.za to extract sensitive MTN user data from the database.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection in URL Path to Dump MTN Database

Multi-stage attack chain demonstrating reconnaissance, vulnerability testing, manual exploitation, and automated dumping of a SQL database via injection in the customerId URL parameter on an MTN-associated site.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance] --> B[Vulnerability Testing]
    B --> C[Manual Exploitation]
    C --> D[Automated Dumping]
    D --> E[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Google-Dorks]]
- [[tools/SQLMap]]

### Target Environment

- Web platform with SQL backend (e.g., MySQL or similar)
- Publicly accessible URL with dynamic parameters in path
- No authentication required for initial testing

### Initial Access Requirements

- Internet access for Google searching
- No prior credentials needed; targets public-facing web app
- Network position: External attacker

## Detailed Attack Procedures

### Step 1: Reconnaissance
procedure: [[procedures/Reconnaissance-Using-Google-Dorks-for-MTN-Sites]]

**Objective**: Identify potential vulnerable endpoints on MTN-associated domains like admyntec.co.za.

**Instructions**: Use [[commands/google-dork-mtn-site]] to search for MTN-related pages:

```bash
google search: site:admyntec.co.za intitle:"MTN"
```

**Expected Output**: List of URLs, such as admin or customer pages with parameters.

**Success Indicators**:
- Discovery of URLs with dynamic parameters like customerId
- Confirmation of in-scope association with mtn.co.za

### Step 2: Vulnerability Testing
procedure: [[procedures/Testing-SQL-Injection-in-URL-Parameters]]

**Objective**: Confirm SQL injection vulnerability in the customerId parameter.

**Instructions**: Append a single quote to the customerId value in the URL, e.g., /path/customerId/1' and observe the response.

**Expected Output**: SQL error message indicating unsanitized input, such as a database syntax error.

**Success Indicators**:
- Error page revealing SQL details (e.g., table names or query fragments)
- No 404 or sanitized response

### Step 3: Manual Exploitation
procedure: [[procedures/Manual-SQL-Injection-Exploitation]]

**Objective**: Execute arbitrary SQL to probe database structure.

**Instructions**: Modify the URL to close the query with ') --, e.g., /path/customerId/1') --, to comment out the rest and run a test like UNION SELECT.

**Expected Output**: Altered page content or further errors confirming control over the query.

**Success Indicators**:
- Successful query alteration without breaking the app
- Database version or table info leaked

### Step 4: Automated Dumping
procedure: [[procedures/Automated-SQL-Injection-with-SQLMap]]

**Objective**: Enumerate and extract full database contents.

**Instructions**: Run [[commands/sqlmap-exploit-url]] on the vulnerable URL:

```bash
sqlmap -u "http://admyntec.co.za/path/customerId=1" --dbs --dump
```

**Expected Output**: List of databases, tables, and dumped data including user info.

**Success Indicators**:
- Successful DB enumeration
- Downloaded sensitive data (e.g., customer records)

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable MTN-associated endpoint via dorking
2. Confirmed and exploited SQLi to access database
3. Dumped entire database for sensitive user data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
