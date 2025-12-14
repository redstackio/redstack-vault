---
data: 'curl -o heap.pprof.gz https://influxdb.quality.gitlab.net/debug/pprof/heap'
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
updated_at: '2025-12-14T17:26:17.196Z'
id: 7de334d7-1f9d-4e3e-baa5-835a9e608a20
verified: false
validated: true
submitted: true
---
# curl-download-heap-profile

## Command

```bash
curl -o heap.pprof.gz https://influxdb.quality.gitlab.net/debug/pprof/heap
```

## Description

Downloads the heap profile file for memory analysis in Go applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -o | Output file name | Yes |

## Examples

### Basic Usage

```bash
curl -o heap.pprof.gz https://influxdb.quality.gitlab.net/debug/pprof/heap
```

### Advanced Usage

```bash
curl -o heap.pprof.gz --header "User-Agent: Mozilla" https://influxdb.quality.gitlab.net/debug/pprof/heap
```

## Expected Output

Downloaded gzip file; no stdout, check file existence.

## Related

- [[Related Procedure: Download-Heap-Profile]]
