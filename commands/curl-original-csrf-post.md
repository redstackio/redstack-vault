---
data: >-
  curl -X POST 'https://liberapay.com/~153780/identity' -H 'Cookie:
  session=your_session_cookie' -d 'csrf_token=Jsf9LQiIMR362WsEP0elX54Ml4HTSCmv'
  -d 'FirstName=Test' -d 'LastName=User' -d 'CountryOfResidence=US' -d
  'Nationality=US' -d 'Birthday=1990-01-01'
tags:
  - http
  - post
  - csrf
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:03.154Z'
id: 5179765e-027d-4d03-ab59-126f8b71d649
verified: false
validated: true
submitted: true
---
# curl-original-csrf-post

## Command

```bash
curl -X POST 'https://liberapay.com/~153780/identity' \
  -H 'Cookie: session=your_session_cookie' \
  -d 'csrf_token=Jsf9LQiIMR362WsEP0elX54Ml4HTSCmv' \
  -d 'FirstName=Test' \
  -d 'LastName=User' \
  -d 'CountryOfResidence=US' \
  -d 'Nationality=US' \
  -d 'Birthday=1990-01-01'
```

## Description

This command performs a baseline POST request to Liberapay's identity update endpoint using curl, including a valid session cookie and original CSRF token, to test normal form submission functionality.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H 'Cookie: ...'` | Sets the session cookie header for authentication | Yes |
| `-d 'csrf_token=...'` | Provides the CSRF token value | Yes |
| `-d 'FirstName=...'` | Form data for first name | Yes |
| `-d 'LastName=...'` | Form data for last name | Yes |
| `-d 'CountryOfResidence=...'` | Form data for country | Yes |
| `-d 'Nationality=...'` | Form data for nationality | Yes |
| `-d 'Birthday=...'` | Form data for birthday | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://liberapay.com/~153780/identity' -H 'Cookie: session=abc123' -d 'csrf_token=original_token' -d 'FirstName=John'
```

### Advanced Usage

Add verbose output with `-v` for debugging:

```bash
curl -v -X POST 'https://liberapay.com/~153780/identity' -H 'Cookie: session=abc123' -d 'csrf_token=original_token' -d 'FirstName=John' -d 'LastName=Doe'
```

## Expected Output

HTTP/1.1 200 OK response body indicating successful update, such as JSON confirmation or redirect. No CSRF errors.

## Related

- [[commands/curl-reused-csrf-post]]
- [[procedures/Exploit-Reusable-CSRF-Tokens-for-Identity-Update]]
