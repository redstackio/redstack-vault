---
data: >-
  curl -H "Authorization: Token token=YOUR_TOKEN"
  https://api.hackerone.com/v1/programs/PROGRAM_HANDLE
tags:
  - api
  - get
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:29.203Z'
id: fc8f0958-7439-4ae9-ae79-8199c953a14a
verified: false
validated: true
submitted: true
---
# curl-api-fetch-program

## Command

```bash
curl -H "Authorization: Token token=YOUR_TOKEN" https://api.hackerone.com/v1/programs/PROGRAM_HANDLE
```

## Description

Fetches details of a specific HackerOne program using the API token, verifying access to program metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H` | Authorization header | Yes |
| `YOUR_TOKEN` | API token | Yes |
| `PROGRAM_HANDLE` | Program identifier (e.g., sandbox-test) | Yes |

## Examples

### Basic Usage

```bash
curl -H "Authorization: Token token=abc123" https://api.hackerone.com/v1/programs/sandbox-test
```

### Advanced Usage

```bash
curl -H "Authorization: Token token=YOUR_TOKEN" https://api.hackerone.com/v1/programs/PROGRAM_HANDLE?include=team
```

## Expected Output

JSON with program info, e.g., {"data": {"handle": "sandbox-test", "name": "Test Program"}} and HTTP 200.

## Related

- [[Related Procedure: Perform-API-Operations-with-Curl]]
