---
id: cmd-hackerone-signup-standard
data: >-
  curl -X POST https://hackerone.com/users -H 'Content-Type:
  application/x-www-form-urlencoded' -d 'user[name]=Test
  User&user[username]=testuser&user[email]=test@hackerone.com&user[password]=password123&user[password_confirmation]=password123'
tags:
  - signup
  - saml
type: command
output: '{"redirect_path":"/users/saml/sign_in?email=test%40hackerone.com"}'
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.342Z'
verified: false
validated: true
submitted: true
---
# hackerone-signup-standard

## Command

```bash
curl -X POST https://hackerone.com/users \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'user[name]=Test User&user[username]=testuser&user[email]=test@hackerone.com&user[password]=password123&user[password_confirmation]=password123'
```

## Description

This command performs a standard HackerOne user signup with a restricted domain email to trigger SAML redirect, used for reconnaissance of enforcement behavior.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user[name] | Display name | Yes |
| user[username] | Username | Yes |
| user[email] | Email (restricted domain) | Yes |
| user[password] | Password | Yes |
| user[password_confirmation] | Password confirm | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/users -d 'user[email]=test@hackerone.com&user[password]=pass'
```

### Advanced Usage

Include full form data as above for complete signup.

## Expected Output

JSON response with redirect to SAML sign_in path.

## Related

- [[commands/hackerone-signup-bypass]]
