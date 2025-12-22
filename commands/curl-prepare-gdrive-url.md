---
id: c1d2e3f4-h5i6-7890-defg-4567890123
data: 'curl -I "https://drive.google.com/uc?id=YOUR_FILE_ID&export=download"'
tags:
  - ssrf
  - testing
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: application/octet-stream
  ...
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:24:56.342Z'
verified: false
validated: true
submitted: true
---
# curl-prepare-gdrive-url

## Command

```bash
curl -I "https://drive.google.com/uc?id=YOUR_FILE_ID&export=download"
```

## Description

This command performs a HEAD request to verify if a Google Drive file is publicly accessible via its direct download URL, used in preparing SSRF payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I, --head` | Fetch headers only | Yes |
| `https://drive.google.com/uc?id=FILE_ID&export=download` | Direct download URL for the Google Drive file | Yes |

## Examples

### Basic Usage

```bash
curl -I "https://drive.google.com/uc?id=1ABC123def&export=download"
```

### Advanced Usage

```bash
curl -I -L "https://drive.google.com/uc?id=1ABC123def&export=download" --max-redirs 5
```

## Expected Output

HTTP headers indicating 200 OK status and content disposition for the file download, confirming accessibility without authentication.

## Related

- [[Related Procedure|procedures/Prepare-Malicious-Google-Drive-URL]]
