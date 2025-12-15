---
data: 'curl -s https://████.jetblue.com/metrics'
tags:
  - recon
  - http
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 1f66a549-02d9-4b37-b6c7-25692a65f3b1
created_at: '2025-12-14T17:25:13.462Z'
updated_at: '2025-12-14T17:25:13.462Z'
verified: false
validated: true
submitted: true
---
# curl-access-grafana-metrics

## Command

```bash
curl -s https://████.jetblue.com/metrics
```

## Description

Fetches the unauthenticated Grafana /metrics endpoint to disclose server metrics. Use -s for silent output to avoid progress bars.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| URL | Target metrics endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -s https://████.jetblue.com/metrics | head -20
```

### Advanced Usage

```bash
curl -s https://████.jetblue.com/metrics | grep 'go_threads'
```

## Expected Output

Prometheus-formatted text with metrics like # HELP process_cpu_seconds_total Total user and system CPU time spent.

## Related

- [[Related Procedure: Access-Grafana-Metrics-Without-Authentication]]
