---
data: 'curl "https://influxdb.quality.gitlab.net/debug/pprof/goroutine?debug=1"'
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
updated_at: '2025-12-14T17:26:17.203Z'
id: 65f49991-914b-472b-86be-5876f27472cd
verified: false
validated: true
submitted: true
---
# curl-retrieve-goroutine-traces

## Command

```bash
curl "https://influxdb.quality.gitlab.net/debug/pprof/goroutine?debug=1"
```

## Description

Retrieves verbose stack traces from goroutines via pprof, exposing runtime details for discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ?debug=1 | Enables full debug output | Yes |

## Examples

### Basic Usage

```bash
curl "https://influxdb.quality.gitlab.net/debug/pprof/goroutine?debug=1"
```

### Advanced Usage

```bash
curl -s "https://influxdb.quality.gitlab.net/debug/pprof/goroutine?debug=1" | grep runtime
```

## Expected Output

Text with stack dumps, e.g., "goroutine 1 [running]: runtime.main()".

## Related

- [[Related Procedure: Retrieve-Goroutine-Stack-Traces]]
