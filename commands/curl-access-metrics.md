---
data: 'curl https://influxdb.quality.gitlab.net/metrics/'
tags:
  - recon
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.177Z'
id: 0584f7f3-782c-44f7-bb70-b3c4e4ebc8ea
verified: false
validated: true
submitted: true
---
# curl-access-metrics

## Command

```bash
curl https://influxdb.quality.gitlab.net/metrics/
```

## Description

Retrieves Prometheus metrics from exposed endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```bash
curl https://influxdb.quality.gitlab.net/metrics/
```

### Advanced Usage

```bash
curl -s https://influxdb.quality.gitlab.net/metrics/ | grep go_
```

## Expected Output

Metrics text like "go_goroutines{quantile="0.5"} 10".

## Related

- [[Related Procedure: Access-Metrics-Endpoint]]
