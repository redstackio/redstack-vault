---
id: cmd-add-trusted-normal
data: >-
  curl -X POST -d "url=http://nextcloud.remote.server.com/"
  https://target-nextcloud/index.php/apps/federation/trusted-servers
tags:
  - ssrf
  - nextcloud
type: command
output: >-
  {"message":"Client error response [url] http://google.com/status.php [status
  code] 404 [reason phrase] Not Found"}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:48.716Z'
verified: false
validated: true
submitted: true
---
# add-trusted-server-normal

## Command

```bash
curl -X POST -d "url=http://nextcloud.remote.server.com/" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

## Description

This command demonstrates normal usage of the Nextcloud trusted-servers endpoint by adding a federated server URL, which triggers a server-side cURL request. It helps understand baseline behavior before exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-d "url=..."` | URL parameter for the trusted server | Yes |
| `https://target-nextcloud/...` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "url=http://nextcloud.remote.server.com/" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

### Advanced Usage

```bash
curl -X POST -d "url=http://example.com/" -H "Content-Type: application/x-www-form-urlencoded" https://target-nextcloud/index.php/apps/federation/trusted-servers
```

## Expected Output

HTTP/1.1 400 Bad Request with JSON: {"message":"Client error response [url] http://google.com/status.php [status code] 404 [reason phrase] Not Found"}, showing the cURL attempt.

## Related

- [[commands/ssrf-probe-port-80]]
- [[procedures/Identify-Nextcloud-Trusted-Servers-Endpoint]]
