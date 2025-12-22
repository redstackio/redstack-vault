---
tags:
  - sqli
  - mysql
  - error-based
  - version-extraction
type: procedure
tools:
  - '[[tools/Firefox]]'
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.205Z'
sub_techniques: []
id: f46a50b2-38f4-4372-b0e3-e1e530c78bfd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-MySQL-Version-via-SQL-Injection

## Summary

This procedure exploits a SQL injection vulnerability in a web application's URL parameter to extract the MySQL database version using an error-based technique with the updatexml function, confirming the backend and potential exploit paths.

## Description

In a scenario where a web application, such as an Airforce subdomain, fails to sanitize single quotes in the `id=` parameter, attackers can inject SQL payloads to trigger errors that leak information. This step focuses on using MySQL's updatexml to force an XPath error that concatenates and displays the version. It requires no special tools beyond a browser and assumes public access to the endpoint. Successful execution reveals the version, aiding in tailoring further attacks like database dumping.

## Requirements

1. Access to a vulnerable web endpoint (e.g., https://subdomain.airforce.mil/page?id=)
2. Web browser for URL manipulation
3. Knowledge of MySQL error-based injection

## Defense

Defensive measures and detection strategies:

- Implement prepared statements or parameterized queries to sanitize inputs
- Use web application firewalls (WAF) to block SQL keywords like 'updatexml' and 'concat'
- Monitor server logs for XPath or SQL errors and anomalous URL parameters

## Objectives

1. Confirm MySQL as the backend database
2. Extract version for compatibility checks with known exploits
3. Validate injection point for deeper reconnaissance

## Instructions

### Step 1: Construct and Append Payload

**Context**: Append the SQL payload to the vulnerable `id=` parameter to trigger an updatexml error that leaks the version.

Visit the URL with the payload: https://subdomain.airforce.mil/page?id=' and updatexml(null,concat(0x0a,version()),null)-- -@hackerone.mil

> This injects a comment to neutralize trailing query parts and uses concat with 0x0a (newline) for readability in the error. Expected output is an error page showing the version in the XPath syntax error message.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]
- [[tools/Web-Browser]]

## Tags

- [[sqli]]
- [[mysql]]
- [[error-based]]
