---
id: cmd-curl-download-test
data: >-
  curl -X GET
  "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid/path"
  -b "cookie=logged_in_session"
tags:
  - web-testing
  - nextcloud
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:25.028Z'
verified: false
validated: true
submitted: true
---
# curl-nextcloud-download-test

## Command

```bash
curl -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid/path" -b "cookie=logged_in_session"
```

## Description

This command tests the Nextcloud file download endpoint by sending invalid parameters to trigger an error page, checking for unescaped output and path disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP GET method | Yes |
| `URL` | Target endpoint with `files=%00` (null byte) and `dir=/invalid/path` | Yes |
| `-b "cookie=..."` | Session cookie for authentication | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid/path" -b "cookie=logged_in_session"
```

### Advanced Usage

```bash
curl -s -X GET "https://nextcloud.example.com/index.php/apps/files/ajax/download.php?files=%00&dir=/invalid/path" -b "cookie=logged_in_session" | grep -i error
```

## Expected Output

An HTML error page response with reflected parameters and potentially full server paths like `/var/www/nextcloud/data/...` in the message.

## Related

- [[commands/curl-nextcloud-xss-payload]]
- [[procedures/Identify-Vulnerable-File-Download-Endpoint-in-Nextcloud]]
