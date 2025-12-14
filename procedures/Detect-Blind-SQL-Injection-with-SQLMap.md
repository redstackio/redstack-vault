---
tags:
  - sqli
  - blind-sqli
  - detection
  - sqlmap
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-test-blind-sqli]]'
platforms:
  - Web
  - MySQL
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7ec97dfe-00ba-4344-9cb3-3f7022663463
created_at: '2025-12-14T03:15:05.107Z'
updated_at: '2025-12-14T03:15:05.107Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect-Blind-SQL-Injection-with-SQLMap

## Summary

This procedure uses SQLMap to test and confirm a Blind SQL Injection vulnerability in a web application's parameter, such as filter[event], by leveraging boolean-based and time-based techniques to infer database responses without direct output.

## Description

In a scenario targeting a public-facing DoD web app, the filter[event] parameter lacks proper sanitization, allowing SQL payload injection. SQLMap automates the detection by sending payloads that alter query responses based on true/false conditions or execution delays, enabling enumeration of the current database name. This step is crucial for verifying exploitability before full data extraction in a blind environment where no error messages are returned.

## Requirements

1. SQLMap installed and accessible via command line
2. Direct HTTP access to the target URL with the vulnerable parameter
3. Knowledge of the DBMS (MySQL in this case) for optimized payloads

## Defense

Defensive measures and detection strategies:

- Implement parameterized queries or prepared statements in backend code to prevent injection
- Deploy a Web Application Firewall (WAF) to detect anomalous SQL patterns or delays
- Enable database logging to monitor unusual query volumes or structures

## Objectives

1. Confirm SQLi vulnerability in the target parameter
2. Enumerate basic database information like the current DB name
3. Assess risk level without triggering full alerts

## Instructions

### Step 1: Launch SQLMap Detection Test

**Context**: Initiate automated testing on the filter[event] parameter using boolean and time-based blind techniques at maximum level and risk for comprehensive coverage.

**Command** ([[commands/sqlmap-test-blind-sqli]]):
```bash
sqlmap -u "███████" --technique=BT --level=5 --risk=3 --threads=10 -p 'filter[event]' --dbms='MySQL' --batch --current-db --random-agent
```

> This command targets the redacted URL, uses 10 threads for speed, randomizes User-Agent to evade detection, and focuses on MySQL-specific payloads. Expected output includes vulnerability confirmation and the current database name if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-test-blind-sqli]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- blind-sqli
- detection
