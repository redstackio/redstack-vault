---
id: 123e4567-e89b-12d3-a456-426614174003
name: curl-portainer-login
type: command
executor: bash
data: >-
  curl -X POST https://data-07.uberinternal.com:9443/api/auth -H "Content-Type:
  application/json" -d '{"username":"admin","password":"password"}'
output: null
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:28.873Z'
platforms:
  - Linux
  - Web
tags:
  - authentication
  - portainer
verified: false
validated: true
submitted: true
---

# curl-portainer-login

## Command

```bash
curl -X POST https://data-07.uberinternal.com:9443/api/auth -H "Content-Type: application/json" -d '{"username":"admin","password":"password"}'
```

## Description

This command authenticates to the Portainer API, retrieving a JWT token for subsequent authenticated requests. Use it to establish a session before exploiting vulnerabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `https://data-07.uberinternal.com:9443/api/auth` | Portainer auth endpoint URL | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload header | Yes |
| `-d '{"username":"admin","password":"password"}'` | JSON payload with credentials | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://data-07.uberinternal.com:9443/api/auth -H "Content-Type: application/json" -d '{"username":"admin","password":"password"}'
```

### Advanced Usage

```bash
curl -X POST https://data-07.uberinternal.com:9443/api/auth -H "Content-Type: application/json" -d '{"username":"admin","password":"password"}' -v
```

## Expected Output

Successful response: {"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...","user":{"id":1,"username":"admin"}}

## Related

- [[Related Procedure]]
