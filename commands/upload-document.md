---
data: 'curl -F ''file=@malicious.docx'' https://pu.vk.com/upload'
tags:
  - upload
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 63a8dc91-242e-47c7-b0f8-bcd672e93d1a
created_at: '2025-12-13T09:00:27.626Z'
updated_at: '2025-12-13T09:00:27.627Z'
verified: false
validated: true
submitted: true
---
# Upload Document

## Command

```bash
curl -F 'file=@malicious.docx' https://pu.vk.com/upload
```

## Description

This command uploads a file to a web endpoint using curl's form data option.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-F 'file=@filename'` | File to upload | Yes |
| `url` | Target upload URL | Yes |

## Examples

### Basic Usage

```bash
curl -F 'file=@malicious.docx' https://pu.vk.com/upload
```

### Advanced Usage

```bash
curl -F 'file=@malicious.docx' -H 'Authorization: Bearer token' https://pu.vk.com/upload
```

## Expected Output

HTTP response indicating successful upload, such as 200 OK.

## Related

- [[procedures/Upload-Malicious-Document-to-Target]]
