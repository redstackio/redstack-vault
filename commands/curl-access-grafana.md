---
data: 'curl -i https://discovered-grafana.snapchat.com/login'
tags:
  - web-access
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 1d1158cd-9597-449b-8a4a-2389c9a3a136
created_at: '2025-12-11T06:10:16.305Z'
updated_at: '2025-12-11T06:10:16.306Z'
verified: false
validated: true
submitted: true
---
# curl-access-grafana

## Command

```bash
curl -i https://discovered-grafana.snapchat.com/login
```

## Description

This command accesses a Grafana login page with headers to check for guest access availability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include HTTP headers in output | No |
| URL | Target Grafana URL | Yes |

## Examples

### Basic Usage

```bash
curl https://grafana.example.com
```

### Advanced Usage

```bash
curl -i -X GET https://grafana.example.com/dashboards
```

## Expected Output

HTTP response with headers and body, indicating access status.

## Related

- [[tools/curl]]
- [[procedures/Access-Grafana-Dashboards-as-Guest-User]]
