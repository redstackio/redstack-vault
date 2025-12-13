---
data: >-
  POST /users HTTP/1.1

  Host: hackerone.com

  ...

  user%5Bname%5D=[NAME]&user%5Busername%5D=[USERNAME]&user%5Bemail%5D=email%40example.com&user%5Bpassword%5D=[PASSWORD]&user%5Bpassword_confirmation%5D=[PASSWORD]
tags:
  - http
  - post
type: command
executor: bash
platforms:
  - Web
id: 02a3cf65-4366-482d-8bbd-4d93ca4890d7
created_at: '2025-12-13T09:01:26.712Z'
updated_at: '2025-12-13T09:01:26.712Z'
verified: false
validated: true
submitted: true
---
# Normal Signup POST Request

## Command

```bash
POST /users HTTP/1.1
Host: hackerone.com
...
user%5Bname%5D=[NAME]&user%5Busername%5D=[USERNAME]&user%5Bemail%5D=email%40example.com&user%5Bpassword%5D=[PASSWORD]&user%5Bpassword_confirmation%5D=[PASSWORD]
```

## Description

Standard signup request that triggers SSO redirect for restricted domains.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `user[email]` | Email address to register, triggers redirect if domain is SAML-enforced | Yes |
| `user[name]` | Full name | Yes |
| `user[username]` | Username | Yes |
| `user[password]` | Password | Yes |
| `user[password_confirmation]` | Password confirmation | Yes |

## Examples

### Basic Usage

```bash
POST /users HTTP/1.1
Host: hackerone.com
...
user%5Bname%5D=Test&user%5Busername%5D=testuser&user%5Bemail%5D=x@hackerone.com&user%5Bpassword%5D=pass123&user%5Bpassword_confirmation%5D=pass123
```

## Expected Output

{"redirect_path":"/users/saml/sign_in?email=email%40example.com"}

## Related

- [[commands/modified-signup-post-request]]
- [[procedures/Bypass-SAML-Signup-Enforcement]]
