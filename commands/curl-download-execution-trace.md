---
data: 'curl -o trace.out https://influxdb.quality.gitlab.net/debug/pprof/trace'
tags:
  - recon
  - download
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.183Z'
id: 8fb0206c-89d3-4158-a362-8b81ebf4671e
verified: false
validated: true
submitted: true
---
# curl-download-execution-trace

## Command

```bash
curl -o trace.out https://influxdb.quality.gitlab.net/debug/pprof/trace
```

## Description

Fetches execution trace for runtime event analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o | Output file | Yes |

## Examples

### Basic Usage

```bash
curl -o trace.out https://influxdb.quality.gitlab.net/debug/pprof/trace
```

### Advanced Usage

```bash
curl -o trace.out -L https://influxdb.quality.gitlab.net/debug/pprof/trace
```

## Expected Output

Binary file downloaded.

## Related

- [[Related Procedure: Download-Execution-Trace]]
