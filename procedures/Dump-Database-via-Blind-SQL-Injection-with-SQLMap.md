---
tags:
  - sqli
  - blind-sqli
  - exploitation
  - data-exfiltration
  - sqlmap
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-dump-database]]'
platforms:
  - Web
  - MySQL
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 73a32a70-e1dd-48ba-b5f2-0eb198b09459
created_at: '2025-12-14T03:15:05.098Z'
updated_at: '2025-12-14T03:15:05.098Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Dump-Database-via-Blind-SQL-Injection-with-SQLMap

## Summary

This procedure exploits a confirmed Blind SQL Injection to dump the entire database contents using SQLMap, extracting tables with sensitive data like API keys and auth tokens in a DoD web application context.

## Description

Following vulnerability confirmation, this step shifts to data collection by instructing SQLMap to reconstruct and export all database elements via blind inference. In the DoD app scenario, this reveals over 300 tables including auth_member_sessions and api_key, enabling attackers to harvest credentials for further compromise. The process relies on the same injection point but escalates to full enumeration, potentially taking longer due to the blind nature.

## Requirements

1. Confirmed injectable parameter from prior detection
2. SQLMap tool with sufficient resources for multi-threaded dumping
3. Stable network connection to handle prolonged interactions

## Defense

Defensive measures and detection strategies:

- Use input validation and escaping for all user-supplied parameters in SQL queries
- Monitor for high query volumes or unusual delays indicative of blind exploitation
- Implement rate limiting and anomaly detection on web app traffic

## Objectives

1. Extract full database schema and data
2. Identify and exfiltrate sensitive information like tokens and logs
3. Demonstrate impact of the vulnerability

## Instructions

### Step 1: Execute Database Dump

**Context**: Use SQLMap's dump functionality to pull all tables and rows through the blind SQLi vector, building on the confirmed vulnerability.

**Command** ([[commands/sqlmap-dump-database]]):
```bash
sqlmap -u "███████" --technique=BT --level=5 --risk=3 --threads=10 -p 'filter[event]' --dbms='MySQL' --batch --dump --random-agent
```

> This replaces the enumeration flag with --dump to retrieve everything, outputting to files like table CSV dumps. Expect detailed logs of extracted data, including sensitive tables like media_set and operational configs.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-dump-database]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- blind-sqli
- exfiltration
