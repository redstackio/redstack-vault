---
data: 'GET https://hackerone.com/users/saml/sign_in?email=███'
tags:
  - http
  - redirect
type: command
executor: bash
platforms:
  - Web
id: 37209264-d0c3-4927-a5a7-b1914b78ce1f
created_at: '2025-12-13T09:01:26.480Z'
updated_at: '2025-12-13T09:01:26.480Z'
verified: false
validated: true
submitted: true
---
# GET SAML Sign In with Email

## Command

```bash
GET https://hackerone.com/users/saml/sign_in?email=███
```

## Description

Automatically starts the SSO-SAML login flow with specified email, enabling open redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email` | Specifies the email to use for login | Yes |

## Examples

### Basic Usage

```bash
GET https://hackerone.com/users/saml/sign_in?email=███
```

### Advanced Usage

```bash
curl 'https://hackerone.com/users/saml/sign_in?email=███'
```

## Expected Output

Redirects to external URLs.

## Related

- [[commands/get-saml-sign-in-with-email-and-remember-me]]
- [[procedures/Exploit-Login-CSRF-for-Authentication-and-Redirect]]
