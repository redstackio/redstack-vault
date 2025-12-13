---
data: 'GET https://hackerone.com/users/saml/sign_in?email=████&remember_me=true'
tags:
  - http
  - csrf
type: command
executor: bash
platforms:
  - Web
id: 30fbf752-ee22-4cfb-b0b7-3805cfc80e4a
created_at: '2025-12-13T09:01:26.485Z'
updated_at: '2025-12-13T09:01:26.485Z'
verified: false
validated: true
submitted: true
---
# GET SAML Sign In with Email and Remember Me

## Command

```bash
GET https://hackerone.com/users/saml/sign_in?email=████&remember_me=true
```

## Description

Initiates the SAML login flow with specified email and remember_me parameter for session persistence, used in Login CSRF attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `email` | Specifies the email to use for login | Yes |
| `remember_me` | Enables session persistence | Yes |

## Examples

### Basic Usage

```bash
GET https://hackerone.com/users/saml/sign_in?email=████&remember_me=true
```

### Advanced Usage

```bash
curl 'https://hackerone.com/users/saml/sign_in?email=████&remember_me=true'
```

## Expected Output

Redirects to SSO-SAML authentication flow.

## Related

- [[commands/get-saml-sign-in-with-email]]
- [[procedures/Exploit-Login-CSRF-for-Authentication-and-Redirect]]
