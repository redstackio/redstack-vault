---
data: 'curl -X POST -F ''file=@malicious.svg'' https://emblem-editor-endpoint'
tags:
  - upload
  - http
type: command
executor: bash
platforms:
  - Linux
  - Windows
id: a47b80ef-bbf7-4bbd-8bc8-3d6ca210e766
created_at: '2025-12-13T09:00:28.090Z'
updated_at: '2025-12-13T09:00:28.090Z'
verified: false
validated: true
submitted: true
---
# upload-svg-payload

## Command

```bash
curl -X POST -F 'file=@malicious.svg' https://emblem-editor-endpoint
```

## Description

Uploads a malicious SVG file to the target emblem editor endpoint for processing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-F 'file=@filename'` | File to upload | Yes |
| `url` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F 'file=@malicious.svg' https://target.com/upload
```

### Advanced Usage

```bash
curl -X POST -F 'file=@malicious.svg' -H 'Authorization: token' https://target.com/upload
```

## Expected Output

HTTP response indicating successful upload and processing.

## Related

- [[commands/create-malicious-svg]]
- [[procedures/Render-Extracted-Data-on-Emblem]]
