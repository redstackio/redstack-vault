---
data: 'curl "https://████?███=value" -w "%{time_total}s\n"'
tags:
  - http
  - baseline
  - timing
type: command
output: 'Normal response time (e.g., 0.234s)'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:04.884Z'
id: 6f543d74-d207-47d3-9809-5e1dc8e0299e
verified: false
validated: true
submitted: true
---
# curl-normal-request

## Command

```bash
curl "https://████?███=value" -w "%{time_total}s\n"
```

## Description

This command sends a standard HTTP request to the target endpoint to establish baseline response time for comparison with injected payloads in SQLi testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target endpoint without payload | Yes |
| -w "%{time_total}s\n" | Outputs total response time | Yes |

## Examples

### Basic Usage

```bash
curl "https://example.com/search?q=test" -w "%{time_total}s\n"
```

### Advanced Usage

```bash
curl -H "User-Agent: Mozilla" "https://example.com" -w "%{time_total}s\n"
```

## Expected Output

Quick response with page content and time under 1 second, serving as a control for anomaly detection.

## Related

- [[Related Procedure: Confirm-Time-Based-SQL-Injection-with-Sleep]]
