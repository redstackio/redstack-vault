---
tags:
  - sqli
  - detection
  - sqlmap
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-detect-sqli-post]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:25.867Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: a8d0293a-806b-489a-897f-19edc0eaaac1
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect-SQL-Injection-with-sqlmap

## Summary

This procedure uses sqlmap to automatically test a web endpoint for SQL injection vulnerabilities in a specific POST parameter, focusing on a PHP-based comment submission form with MySQL backend.

## Description

In this attack scenario, the target is a public-facing web application vulnerable to SQL injection due to unsanitized input in the 'staff_student' POST parameter. Sqlmap is configured with high-level testing, aggressive risk payloads, a tamper script to evade WAFs, and random user agents. The procedure identifies potential injection points without requiring manual payload crafting, suitable for penetration testing of web forms. Expected outcomes include confirmation of injectable parameters and DBMS type.

## Requirements

1. Sqlmap installed and accessible via Python 3
2. Network access to the target HTTPS endpoint
3. Knowledge of the POST data structure for the form
4. No authentication barriers on the endpoint

## Defense

Defensive measures and detection strategies:

- Implement input parameterization or prepared statements in PHP/MySQL queries
- Deploy WAF rules to detect sqlmap signatures and anomalous payloads
- Monitor application logs for unusual query patterns or high request volumes from single IPs

## Objectives

1. Identify SQL injection vulnerabilities in the 'staff_student' parameter
2. Confirm MySQL as the backend DBMS
3. Establish a foundation for further exploitation like database enumeration

## Instructions

### Step 1: Prepare and Launch Sqlmap Scan

**Context**: Configure sqlmap to target the specific POST request and parameter, using evasion techniques to avoid detection during the scan.

**Command** ([[commands/sqlmap-detect-sqli-post]]):
```bash
python3 sqlmap.py -l=5 --risk=3 --tamper=space2comment --random-agent -u "https://target.com/olc/xxxcomments/comment_post.php" --data="staff_student=STUDENT&scn=xxx&check25=0&check20=0&check20=1&check26=0&check27=0&check29=0&check24=0&comments=xx&Submit=Submit+Comments" -p staff_student --dbms=mysql
```

> This command runs sqlmap at maximum level (5) for thorough payload testing and high risk (3) to include time-based techniques. The tamper script replaces spaces with /**/ to bypass filters, random agents mimic legitimate traffic, and -p focuses on 'staff_student'. Expected output includes identification of injection points and request counts.

### Step 2: Analyze Output for Vulnerability Confirmation

**Context**: Review sqlmap's verbose output to verify the vulnerability without proceeding to exploitation.

**Command**: No new command; parse output from Step 1.

> Look for messages indicating 'parameter 'staff_student' is vulnerable' and details on tested payloads. If successful, proceed to confirmation of types.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-detect-sqli-post]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- detection
- web-exploit
