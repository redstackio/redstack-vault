---
data: >-
  curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d
  "image=SomeContent&filename=test&extension=png"
tags:
  - http-post
  - file-upload
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.043Z'
id: f7284be9-7696-4155-9a15-5327b7d19197
verified: false
validated: true
submitted: true
---
# saveimage-normal-post

## Command

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=SomeContent&filename=test&extension=png"
```

## Description

Sends a legitimate POST request to the saveImage.php endpoint to test normal PNG file creation in the uploads directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| image | Image stream data (placeholder: SomeContent) | Yes |
| filename | Base filename (e.g., test) | Yes |
| extension | File extension (e.g., png) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=SomeContent&filename=test&extension=png"
```

### Advanced Usage

Add -v for verbose output:

```bash
curl -v -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=SomeContent&filename=test&extension=png"
```

## Expected Output

HTTP 200 OK response; file created as preview-test.png, accessible at /view/data/image/preview-test.png.

## Related

- [[commands/saveimage-traversal-php]]
- [[procedures/Test-Legitimate-File-Upload-via-saveImage]]
