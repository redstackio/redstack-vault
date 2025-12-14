---
id: cmd-uuid-101
data: 'curl -v "https://resizer.line-apps.com/form?url=$EXTERNAL_URL"'
tags:
  - recon
  - web
  - test
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.213Z'
verified: false
validated: true
submitted: true
---
# curl-basic-test

## Command

```bash
curl -v "https://resizer.line-apps.com/form?url=$EXTERNAL_URL"
```

## Description

This command tests the resizer service endpoint with a benign external URL to verify functionality and HTTP acceptance before SSRF exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode for detailed output | Yes |
| `url=` | External test URL (e.g., http://httpbin.org/get) | Yes |
| `$EXTERNAL_URL` | Placeholder for public URL | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://resizer.line-apps.com/form?url=http://httpbin.org/get"
```

### Advanced Usage

```bash
curl -v "https://resizer.line-apps.com/form?url=https://example.com/image.jpg"
```

## Expected Output

HTTP response with 200 status, echoed request details, or processed image confirmation.

## Related

- [[Related Procedure|procedures/Identify-Resizer-SSRF-Endpoint]]
