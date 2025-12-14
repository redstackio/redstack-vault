---
id: cmd-curl-retrieve-logs-001
data: 'curl http://localhost:8001/logs/kube-apiserver.INFO'
tags:
  - logs
  - exfil
type: command
output: 'I... Response Body: {"full": "internal response"}...'
executor: bash
platforms:
  - Linux
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:55.675Z'
verified: false
validated: true
submitted: true
---
# retrieve-apiserver-logs

## Command

```bash
curl http://localhost:8001/logs/kube-apiserver.INFO
```

## Description

Fetches kube-apiserver INFO logs via proxy to inspect SSRF leaks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Log endpoint | Yes |

## Examples

### Basic Usage

```bash
curl http://localhost:8001/logs/kube-apiserver.INFO
```

### Advanced Usage

```bash
curl -s http://localhost:8001/logs/kube-apiserver.INFO | grep 'Response Body'
```

## Expected Output

Log lines with timestamps and HTTP details, including response bodies.

## Related

- [[commands/search-log-responses]]
- [[procedures/Inspect-Apiserver-Logs-for-Leaked-Responses]]
