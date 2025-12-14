---
id: cmd-uuid-placeholder-001
data: >-
  curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type:
  multipart/form-data" -F "file=@test.txt"
  https://target.com/talos/api/v1/files/upload
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
updated_at: '2025-12-14T17:25:18.113Z'
verified: false
validated: true
submitted: true
---
# curl-file-upload

## Command

```bash
curl -X POST -H "Authorization: Bearer YOUR_TOKEN" -H "Content-Type: multipart/form-data" -F "file=@test.txt" https://target.com/talos/api/v1/files/upload
```

## Description

This command uploads a file to a web API endpoint using multipart form data, targeting the vulnerable file upload functionality to trigger memory leak disclosure.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Authorization: Bearer YOUR_TOKEN"` | Authentication header with Bearer token | Yes (if auth required) |
| `-H "Content-Type: multipart/form-data"` | Sets content type for file upload | Yes |
| `-F "file=@test.txt"` | Uploads the file specified by path | Yes |
| `https://target.com/talos/api/v1/files/upload` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "file=@test.txt" https://target.com/talos/api/v1/files/upload
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: Bearer abc123" -F "file=@test.txt" -v https://target.com/talos/api/v1/files/upload
```

## Expected Output

JSON response indicating upload success, e.g., {"status": "success", "file_id": "123", "s3_url": "https://s3..."}. Verbose mode (-v) shows headers and any errors.

## Related

- [[Related Procedure: Exploit-File-Upload-Memory-Leak]]
