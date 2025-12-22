---
data: >-
  curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@test.txt"
  -v
tags:
  - file-upload
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 16b42aa9-2ee7-4711-a51b-6fcd97fd8aa3
created_at: '2025-12-14T05:32:13.788Z'
updated_at: '2025-12-14T05:32:13.788Z'
verified: false
validated: true
submitted: true
---
# curl-test-upload

## Command

```bash
curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@test.txt" -v
```

## Description

This command tests file upload by posting a local test.txt file to the .ashx endpoint using multipart form data, checking for acceptance of non-image types.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-F "file=@test.txt"` | Form field with file attachment | Yes |
| `-v` | Verbose mode | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@test.txt" -v
```

### Advanced Usage

```bash
curl -X POST https://mobile.starbucks.com.sg/upload.ashx -F "file=@test.txt" -F "type=image" -v
```

## Expected Output

HTTP 200 OK with possible JSON response like {"success": true, "path": "/uploads/test.txt"}, confirming upload without rejection.

## Related

- [[Related Procedure: Test-Unrestricted-File-Upload]]
