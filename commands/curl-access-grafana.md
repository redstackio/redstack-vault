---
data: 'curl -v https://TARGET'
tags:
  - access
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: d27ed0ef-5b37-4614-a368-9e7edf9994ad
created_at: '2025-12-11T03:47:39.541Z'
updated_at: '2025-12-11T03:47:39.541Z'
verified: false
validated: true
submitted: true
---
# curl-access-grafana

## Command

```bash
curl -v https://TARGET
```

## Description

Tests access to a web endpoint with verbose output to check headers and responses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode | No |

## Examples

### Basic Usage

```bash
curl https://grafana.snapchat.com
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Test" https://grafana.snapchat.com
```

## Expected Output

HTTP response with content if accessible.

## Related

- #curl
- [[procedures/Access-Grafana-as-Guest-User]]
