---
id: c65527c6-c514-4a21-b1bf-81dc9f9d4650
name: access-signup-page
type: command
executor: bash
data: curl -X GET "$_TARGET_URL/signup?redirectUrl=$_TEST_REDIRECT" -v
output: null
created_at: '2023-04-06T03:56:31.693074+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Web
tags:
  - recon
  - web
verified: true
validated: true
---

# access-signup-page

## Command

```bash
curl -X GET "$_TARGET_URL/signup?redirectUrl=$_TEST_REDIRECT" -v
```

## Description

Accesses the signup page of a target website and tests for the presence of a redirect parameter by including a test URL. Use this to initially probe for open redirect vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the target website (e.g., https://famous-website.tld) | Yes |
| $_TEST_REDIRECT | Benign test redirect URL (e.g., https://example.com) | Yes |
| -v | Verbose output to show headers and redirects | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://famous-website.tld/signup?redirectUrl=https://example.com" -v
```

### With Follow Redirects

```bash
curl -X GET "https://famous-website.tld/signup?redirectUrl=https://example.com" -L -v
```

## Expected Output

HTTP/1.1 200 OK or 302 Found with Location header showing the test redirect, indicating the parameter is accepted without validation.

## Related

- [[procedures/Open-URL-Redirection-Exploitation]]
- [[commands/add-redirect-url]]
