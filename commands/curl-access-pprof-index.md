---
data: 'curl https://influxdb.quality.gitlab.net/debug/pprof'
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
updated_at: '2025-12-14T17:26:17.209Z'
id: 3b4fd737-3ef7-4be7-a566-45f701d15340
verified: false
validated: true
submitted: true
---
# curl-access-pprof-index

## Command

```bash
curl https://influxdb.quality.gitlab.net/debug/pprof
```

## Description

This command performs a GET request to the Go pprof index endpoint to list available profiles, used in reconnaissance of exposed debugging interfaces.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Target pprof endpoint | Yes |

## Examples

### Basic Usage

```bash
curl https://influxdb.quality.gitlab.net/debug/pprof
```

### Advanced Usage

```bash
curl -v https://influxdb.quality.gitlab.net/debug/pprof
```

## Expected Output

Plain text listing profiles, e.g., "goroutine	Profile the goroutine tree".

## Related

- [[Related Procedure: Access-Go-Pprof-Index]]
