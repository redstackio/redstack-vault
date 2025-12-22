---
tags:
  - sql-injection
  - sqli
  - sqlmap
  - web-vulnerability
  - database
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-detect-sqli-high-risk]]'
platforms:
  - Web
  - Windows
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: eb71faf2-8de2-4791-96d9-235fc17c482b
created_at: '2025-12-14T03:15:05.020Z'
updated_at: '2025-12-14T03:15:05.020Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect-and-Confirm-SQL-Injection-with-sqlmap

## Summary

This procedure uses the sqlmap tool to detect and confirm a SQL Injection vulnerability in the countID parameter of a web endpoint, such as /public/saveCount.cfm on a ColdFusion-based site, by sending crafted payloads and retrieving the database banner to validate exploitation.

## Description

In this attack scenario, the target is a public-facing web application lacking input sanitization on the countID parameter, allowing arbitrary SQL commands to be injected via HTTP requests. The procedure targets Microsoft SQL Server backends but is adaptable. Prerequisites include network access to the endpoint and sqlmap installed. Successful execution confirms the vulnerability, enabling further steps like data exfiltration or command execution, potentially compromising sensitive DoD data.

## Requirements

1. Python 2.7 or 3.x environment with sqlmap installed
2. Direct internet access to the target HTTPS URL (e.g., https://www.██████████/public/saveCount.cfm?countID=4)
3. No authentication required for the endpoint

## Defense

Defensive measures and detection strategies:

- Implement parameterized queries or prepared statements in the application code to prevent SQLi
- Use web application firewalls (WAFs) to block anomalous SQL payloads in requests
- Monitor database logs for unusual queries or error messages indicating injection attempts
- Regularly scan public endpoints with tools like sqlmap in a controlled environment to identify vulnerabilities

## Objectives

1. Confirm SQL Injection vulnerability in the countID parameter
2. Retrieve database server details for further exploitation planning
3. Establish control over the database for data manipulation or exfiltration

## Instructions

### Step 1: Launch sqlmap Against the Target Endpoint

**Context**: This step tests the URL for SQL Injection by automating payload injection and analyzing responses to detect vulnerabilities.

**Command** ([[commands/sqlmap-detect-sqli-high-risk]]):
```bash
python sqlmap.py -u https://www.██████████/public/saveCount.cfm?countID=4 --level=3 --risk=3
```

> This command specifies the target URL with the vulnerable countID=4 parameter. The --level=3 enables more thorough tests including additional injection points, while --risk=3 allows payloads that could alter data or cause denial of service. Expected output includes vulnerability confirmation and the database banner dump.

### Step 2: Analyze Output for Confirmation

**Context**: Review sqlmap's results to verify the injection point and backend details.

**Command** (No additional command; parse sqlmap output):

> Look for messages like "[INFO] the back-end DBMS is Microsoft SQL Server" and the full banner. If successful, proceed to exploitation phases like --dbs for database enumeration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-detect-sqli-high-risk]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- [[sql-injection]]
- [[sqli]]
- [[tools/sqlmap]]
- [[web]]
- [[database]]
