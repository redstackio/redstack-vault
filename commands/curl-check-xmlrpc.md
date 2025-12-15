---
id: cmd-curl-check-xmlrpc
data: >-
  curl -s -X POST http://target.com/xmlrpc.php -d
  '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
tags:
  - recon
  - web
type: command
output: XML response with method list if enabled
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.526Z'
verified: false
validated: true
submitted: true
---
# curl-check-xmlrpc

## Command

```bash
curl -s -X POST http://target.com/xmlrpc.php -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

## Description

This command uses curl to send a POST request to the xmlrpc.php endpoint with a system.listMethods call, verifying if XML-RPC is enabled on a WordPress site. Use it during reconnaissance to detect the vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode, suppresses progress meter | Yes |
| `-X POST` | Specifies POST method | Yes |
| `http://target.com/xmlrpc.php` | Target endpoint URL | Yes |
| `-d '<payload>'` | XML payload for the method call | Yes |

## Examples

### Basic Usage

```bash
curl -s -X POST http://example.com/xmlrpc.php -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

### Advanced Usage

```bash
curl -s -X POST https://example.com/xmlrpc.php --data-urlencode '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>' -H 'User-Agent: Mozilla/5.0'
```

## Expected Output

If enabled: `<?xml version="1.0"?><methodResponse><params><param><value><array><data><value><string>demo.sayHello</string></value>...</data></array></value></param></params></methodResponse>`. If disabled: HTTP 404 or empty response.

## Related

- [[Related Procedure: Verify-WordPress-xmlrpc.php-Accessibility]]
