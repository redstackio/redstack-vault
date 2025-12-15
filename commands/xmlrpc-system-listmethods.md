---
data: >-
  curl -X POST http://target.com/xmlrpc.php -H "Content-Type: text/xml" -H
  "Accept: */*" -H "Accept-Language: en" -d
  '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
tags:
  - xmlrpc
  - wordpress
  - verification
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.319Z'
id: c4cd8feb-3065-4456-801b-067b86631e06
verified: false
validated: true
submitted: true
---
# xmlrpc-system-listmethods

## Command

```bash
curl -X POST http://target.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -H "Accept: */*" \
  -H "Accept-Language: en" \
  -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

## Description

Sends an XML-RPC request to the WordPress xmlrpc.php endpoint to list all available methods, used to verify if the endpoint is enabled and responsive.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target.com` | Target WordPress site hostname | Yes |
| `-H "Content-Type: text/xml"` | Sets XML content type | Yes |
| `-d '<methodCall>...' ` | XML payload with system.listMethods | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://example.com/xmlrpc.php -H "Content-Type: text/xml" -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST http://target.com/xmlrpc.php -H "Content-Type: text/xml" -d '<methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
```

## Expected Output

XML response like:

```xml
<methodResponse>
<params>
<param><value><array><data><value><string>pingback.ping</string></value>...</data></array></value></param>
</params>
</methodResponse>
```
Lists methods if successful; faults if endpoint disabled.

## Related

- [[procedures/Verify-xmlrpc-php-Endpoint]]
- [[procedures/Exploit-xmlrpc-php-for-DDoS-via-Pingback]]
