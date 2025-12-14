---
data: go tool pprof heap.pprof.gz
tags:
  - analysis
  - go
  - profiling
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:17.164Z'
id: 6ecb2f67-5eea-40e7-93da-023cfdcbb89c
verified: false
validated: true
submitted: true
---
# go-tool-pprof-analyze

## Command

```bash
go tool pprof heap.pprof.gz
```

## Description

Analyzes a pprof heap profile to identify memory hotspots.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| profile_file | Input pprof file | Yes |

## Examples

### Basic Usage

```bash
go tool pprof heap.pprof.gz
```

### Advanced Usage

```bash
go tool pprof -http=:8080 heap.pprof.gz
```

## Expected Output

Interactive prompt: (pprof) top - shows allocation leaders.

## Related

- [[Related Procedure: Download-Heap-Profile]]
