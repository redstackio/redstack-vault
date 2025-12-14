---
data: >-
  curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.254/" -H
  "Host: geonode.state.gov"
tags:
  - ssrf
  - test
  - block
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:54.989Z'
id: 542901a0-29ce-452f-988d-d8760a931438
verified: false
validated: true
submitted: true
---
# direct-internal-ip-test

## Command

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.254/" -H "Host: geonode.state.gov"
```

## Description

Attempts a direct request to an internal IP via the proxy to confirm whitelist blocking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | http://internal-ip/ | Yes |
| Host | Target host | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://169.254.169.254/" -H "Host: geonode.state.gov"
```

### Advanced Usage

```bash
curl -X GET "https://geonode.state.gov/proxy/?url=http://127.0.0.1/" -H "Host: geonode.state.gov" -v
```

## Expected Output

Request blocked (e.g., 403 Forbidden or custom error), confirming whitelist enforcement.

## Related

- [[commands/bypass-whitelist-to-internal-ip]]
- [[procedures/Bypass-SSRF-Whitelist-for-Internal-Scanning]]
