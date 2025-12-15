---
data: 'curl -v http://target-host:9093/#/alerts'
tags:
  - recon
  - access
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
id: b948c1d0-3ebb-42d6-b395-d79de6d66b85
created_at: '2025-12-14T17:31:42.620Z'
updated_at: '2025-12-14T17:31:42.620Z'
verified: false
validated: true
submitted: true
---
# curl-access-alertmanager

## Command

```bash
curl -v http://target-host:9093/#/alerts
```

## Description

This command uses curl to access the Alertmanager web interface or API without authentication, verifying if the service is exposed and unprotected. The verbose (-v) flag shows headers and response details to confirm no auth challenge.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output including headers | No |
| `http://target-host:9093` | Target Alertmanager URL (replace with actual host/port) | Yes |
| `/#/alerts` | Path to alerts page (use /api/v1/alerts for JSON API) | Yes |

## Examples

### Basic Usage

```bash
curl -v http://example.com:9093/#/alerts
```

### Advanced Usage

```bash
curl -X GET -H "Accept: application/json" http://example.com:9093/api/v1/alerts
```

## Expected Output

Successful execution returns HTTP 200 with Alertmanager UI HTML or JSON alert data, e.g., {"data": {"alerts": [...]}}. No 401 Unauthorized indicates vulnerability.

## Related

- [[Related Procedure]]
