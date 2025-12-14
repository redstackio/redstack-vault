---
id: proc-inject-sqli-payload
tags:
  - sqli
  - payload-injection
  - blind-sqli
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.008Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[T1190.001]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-SQL-Payload-into-Parameter

## Summary

Manually inject SQL payloads into the 'selMajcom' parameter using Burp Suite to confirm the SQL Injection vulnerability through boolean or time-based blind techniques.

## Description

The ASP application concatenates user input directly into SQL queries without sanitization, allowing injection. Test with payloads like MAT' or time-based WAITFOR DELAY to observe response differences or delays, confirming backend SQL Server interaction.

## Requirements

1. Captured request in Burp Suite Repeater
2. Knowledge of SQL Server syntax for blind injections
3. Stable session to avoid timeouts

## Defense

Defensive measures and detection strategies:

- Use prepared statements or parameterized queries in ASP code
- Implement web application firewall (WAF) to block SQL keywords
- Log and alert on response time anomalies

## Objectives

1. Verify SQL Injection vulnerability type (blind time-based)
2. Establish proof-of-concept for further exploitation
3. Identify response indicators for automation

## Instructions

### Step 1: Load into Repeater

**Context**: Prepare the captured request for modification.

In Burp Suite, send the intercepted request to Repeater.

> Request ready for parameter editing.

### Step 2: Inject Payload

**Context**: Modify selMajcom and send to test.

Change selMajcom to MAT'; WAITFOR DELAY '0:0:5'-- and forward the request.

> Expected output: Response delayed by 5 seconds, confirming time-based blind SQLi.

For boolean test: Use MAT' AND 1=1-- vs. MAT' AND 1=2-- and compare responses.

> True condition returns normal page; false differs.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques

- [[T1190.001]]

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[sqli]]
- [[payload-injection]]
