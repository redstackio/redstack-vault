---
id: cmd-834366-invalid-token
name: hackerone-invalid-token-test
type: command
executor: http
data: >-
  POST /users/sign_in HTTP/1.1

  Host: hackerone.com

  ...


  user[email]=:email&user[password]=:password&authenticity_token[]=this-is-an-array
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.550Z'
platforms:
  - Web
tags:
  - csrf
  - retest
verified: false
validated: true
submitted: true
---

# hackerone-invalid-token-test

## Command

```http
POST /users/sign_in HTTP/1.1
Host: hackerone.com
Content-Type: application/x-www-form-urlencoded

user[email]=test@example.com&user[password]=testpass&authenticity_token[]=this-is-an-array
```

## Description

HTTP POST request with invalid authenticity_token as an array to test CSRF fix enforcement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| user[email] | Test email | Yes |
| user[password] | Test password | Yes |
| authenticity_token[] | Array to trigger validation | Yes |

## Examples

### Basic Usage

Send via curl or Burp:

```bash
curl -X POST https://hackerone.com/users/sign_in -d 'user[email]=test&user[password]=pass&authenticity_token[]=array'
```

## Expected Output

HTTP 400 Bad Request: 'Invalid parameter: authenticity_token must be a string', with set-cookie but no authentication.

## Related

- [[procedures/Bypass-HackerOne-Login-CSRF-Token]]
