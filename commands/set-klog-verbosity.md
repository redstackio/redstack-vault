---
id: cmd-curl-set-verbosity-001
data: 'curl -XPUT --data "10" http://localhost:8001/debug/flags/v'
tags:
  - debug
  - klog
type: command
output: '10'
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.681Z'
verified: false
validated: true
submitted: true
---
# set-klog-verbosity

## Command

```bash
curl -XPUT --data "10" http://localhost:8001/debug/flags/v
```

## Description

Sets klog verbosity to 10 via debug endpoint to log full HTTP responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-XPUT` | HTTP method | Yes |
| `--data` | Verbosity value | Yes |
| URL | Debug flags endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -XPUT --data "10" http://localhost:8001/debug/flags/v
```

### Advanced Usage

```bash
curl -XPUT --data "5" http://localhost:8001/debug/flags/v
```

## Expected Output

The set value echoed back.

## Related

- [[commands/start-kubectl-proxy]]
- [[procedures/Enable-Kubectl-Proxy-and-Debug-Flags]]
