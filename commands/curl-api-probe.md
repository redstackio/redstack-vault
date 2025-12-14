---
data: >-
  curl -X POST https://api.example.com/upload-image -H "Content-Type:
  multipart/form-data"
tags:
  - api
  - probe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.149Z'
id: 2c3b1457-10d9-4d06-b28a-997e877ec57b
verified: false
validated: true
submitted: true
---
# curl-api-probe

## Command

```bash
curl -X POST https://api.example.com/upload-image -H "Content-Type: multipart/form-data"
```

## Description

This command probes a legacy API upload endpoint to check accessibility and expected response format without sending a file, helping identify validation weaknesses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `https://api.example.com/upload-image` | The target API endpoint URL | Yes |
| `-H "Content-Type: multipart/form-data"` | Sets the content type for form uploads | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://api.example.com/upload-image -H "Content-Type: multipart/form-data"
```

### Advanced Usage

```bash
curl -v -X POST https://api.example.com/upload-image -H "Content-Type: multipart/form-data"
```

## Expected Output

HTTP response code (e.g., 400 Bad Request) with details on required parameters like 'file', or 200 if the endpoint accepts empty requests, indicating no strict validation.

## Related

- [[Related Procedure]]
