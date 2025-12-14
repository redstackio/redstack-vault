---
id: proc-433792-fuzz-parameters
tags:
  - fuzzing
  - sqli
  - parameter-testing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fuzz-new-param]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:07.773Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Fuzz-Parameters-for-SQL-Injection-Vulnerabilities

## Summary

This procedure tests URL parameters in identified endpoints for SQL injection flaws by injecting test payloads like quotes, unions, or boolean conditions to elicit errors or unusual behaviors.

## Description

Fuzzing involves systematically altering inputs to backend APIs, such as the 'new' parameter in AgileCRM's addstats endpoint, to detect lack of sanitization. In this scenario, testing revealed the 'new' parameter's vulnerability to Blind SQLi without direct error messages, relying on response anomalies.

## Requirements

1. Proxy tool or browser extension for request modification (e.g., Burp Suite Community)
2. Knowledge of SQL syntax for payloads
3. Access to the vulnerable endpoint

## Defense

Defensive measures and detection strategies:

- Parameterize all database queries using prepared statements
- Implement input validation and WAF rules for SQL keywords
- Log and alert on repeated fuzzing attempts

## Objectives

1. Identify injectable parameters
2. Confirm potential for SQL execution
3. Prepare for payload confirmation

## Instructions

### Step 1: Craft Base Request

**Context**: Replicate the original request and prepare to modify parameters.

**Command** ([[commands/curl-fuzz-new-param]]):
```bash
curl 'https://stats2.agilecrm.com/addstats?callback=jQuery&guid=abc&sid=123&url=https://rocket.chat/&agile=def&domain=rocket.chat&new=\' '
```

> Inject a single quote into 'new' to test for SQL breakage; look for response changes or errors indicating injection.

### Step 2: Escalate Fuzzing

**Context**: Try advanced payloads like boolean or union-based to probe deeper.

Modify the request iteratively, e.g., append ' OR 1=1 --' to 'new', observing for consistent responses versus anomalies.

> Expected output: Subtle differences in response time or content hinting at vulnerability without explicit errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fuzz-new-param]]

## Tools Used


## Tags

- [[fuzzing]]
- [[sqli]]
