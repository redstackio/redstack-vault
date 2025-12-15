---
data: 'curl https://cortex-ingest.shopifycloud.com/debug/pprof/cmdline?debug=1'
tags:
  - debug
  - cmdline
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.344Z'
id: 412cfb47-d61f-47d0-b5bc-c811b5bec3fa
verified: false
validated: true
submitted: true
---
# curl-access-pprof-cmdline

## Command

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/cmdline?debug=1
```

## Description

Exposes the command-line arguments used to start the Golang process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `?debug=1` | Enable debug output | Yes |
| `https://.../cmdline` | Cmdline endpoint | Yes |

## Examples

### Basic Usage

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/cmdline?debug=1
```

### Advanced Usage

```bash
curl https://cortex-ingest.shopifycloud.com/debug/pprof/cmdline?debug=1 | tr ' ' '\n'  # Line-break args
```

## Expected Output

/path/to/cortex -config=/etc/config.yaml -server.port=80

## Related

- [[Related Procedure]]
