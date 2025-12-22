---
id: fda4fd5d-2dbb-4bf8-a5e5-8a24c92d5262
name: curl-upload-to-target
type: command
executor: bash
data: curl -F "file=@$_FILE_PATH" -F "submit=Upload" $_TARGET_URL
output: null
created_at: '2023-04-06T03:56:40.894377+00:00'
updated_at: '2023-04-06T03:56:40.905214+00:00'
platforms:
  - linux
  - web
tags:
  - upload
  - http
verified: true
validated: true
---

# curl-upload-to-target

## Command

```bash
curl -F "file=@$_FILE_PATH" -F "submit=Upload" $_TARGET_URL
```

## Description

This command simulates a multipart form upload of a file to a web application's upload endpoint, commonly used to deliver polyglot files in file upload attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILE_PATH | Local path to the file to upload (e.g., .htaccess) | Yes |
| $_TARGET_URL | URL of the upload form endpoint (e.g., http://target.com/upload.php) | Yes |
| -F "submit=Upload" | Form field for submission button (adjust based on form) | No |

## Examples

### Basic Usage

```bash
curl -F "file=@image.jpg" http://target.com/upload
```

### Advanced Usage with Headers

```bash
curl -F "file=@$_FILE_PATH" $_TARGET_URL -H "User-Agent: Mozilla/5.0"
```

## Expected Output

Upload successful. File saved as /uploads/image.xbm

or HTTP 200 with confirmation message. Errors indicate validation failure.

## Related

- [[procedures/Image-Based-htaccess-Upload-Bypass]]
