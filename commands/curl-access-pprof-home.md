---
data: 'curl https://cortex-ingest.shopifycloud.com/debug/pprof/'
tags:
  - debug
  - pprof
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.345Z'
id: 83568ad5-248f-4d6e-8230-9d15cc69a781
verified: false
validated: true
submitted: true
---
# curl-access-pprof-home

## Command

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/
```

## Description

Fetches the pprof debugging index page listing available profiles.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://.../debug/pprof/` | Pprof root URL | Yes |

## Examples

### Basic Usage

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/
```

### Advanced Usage

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/ | grep heap  # Filter for heap
```

## Expected Output

Available profiles:
	3	allocs
	4	heap
 ...

## Related

- [[Related Procedure]]
