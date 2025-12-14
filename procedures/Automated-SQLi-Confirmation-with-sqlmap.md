---
id: proc-uuid-2
tags:
  - sqli
  - sqlmap
  - automation
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-verify-injection]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.025Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Automated-SQLi-Confirmation-with-sqlmap

## Summary

This procedure uses sqlmap to automate the detection and characterization of SQL injection vulnerabilities in the username parameter of a login endpoint, confirming boolean-based blind and time-based blind techniques on a MySQL backend.

## Description

Following manual verification, sqlmap is employed against the /olc/setlogin.php endpoint to thoroughly test injection points. With high level (5) and risk (3) settings, it probes extensively, using tamper scripts for evasion and random agents to mimic legitimate traffic. This reveals injection types, DBMS version, and web technologies, enabling targeted follow-up exploitation like data enumeration.

## Requirements

1. Installed sqlmap tool (Python-based)
2. Target URL and POST data details
3. Network access to the HTTPS endpoint

## Defense

Defensive measures and detection strategies:

- Deploy intrusion detection systems (IDS) to flag sqlmap-like traffic patterns
- Enforce input validation and output encoding in PHP applications
- Rate-limit login attempts to hinder automated probing

## Objectives

1. Identify specific SQL injection techniques
2. Confirm MySQL as the DBMS and version
3. Assess evasion needs for further attacks

## Instructions

### Step 1: Launch sqlmap with Detection Settings

**Context**: Target the username parameter in POST data, specifying MySQL and evasion options to confirm injection without triggering redirects.

**Command** ([[commands/sqlmap-verify-injection]]):
```bash
python3 sqlmap.py --level=5 --risk=3 --tamper=space2comment --random-agent -u https://target.com/olc/setlogin.php --data="username=admin&password=pass" -p username --dbms=mysql
```

> If prompted about following redirects (302), answer 'n'. This tests payloads like OR 1=1 for boolean blind and SLEEP for time-based. Expected output: Injection techniques identified, MySQL >=5.0.12, Apache server.

### Step 2: Review and Validate Output

**Context**: Analyze sqlmap's report for vulnerability details and prepare for enumeration.

**Command** (No new command; parse output):

> Look for lines like 'boolean-based blind' and 'time-based blind'. Success if multiple techniques confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-verify-injection]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- sqlmap
