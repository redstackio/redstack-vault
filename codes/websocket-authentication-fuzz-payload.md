---
type: code
language: json
verified: true
platforms:
  - Web
tags:
  - web-sockets
  - fuzzing
  - authentication
validated: true
---

# websocket-authentication-fuzz-payload

## Code

```json
{"auth_user":"dGVzda==", "auth_pass":"[FUZZ]"}
```

## Description

This JSON payload serves as a template for authenticating via WebSocket handshakes. The auth_user field contains a base64-encoded username (e.g., 'test' base64'd), while auth_pass uses [FUZZ] as a placeholder for brute-forcing passwords. It is used to test the server's authentication logic for vulnerabilities like weak hashing or lack of salting.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| auth_user | Base64-encoded username for authentication | "dGVzdA==" (for 'test') |
| [FUZZ] | Placeholder for password candidates during fuzzing | "password", "admin", or wordlist entries |

## Usage

Save this JSON to a file (e.g., message.txt) and pass it to ws-harness.py for WebSocket transmission. For fuzzing, script a loop to replace [FUZZ] with values from a wordlist and monitor responses for successful auth. This is typically used in red team engagements targeting real-time web apps after initial recon.

## Detection

- Log analysis for repeated WebSocket handshakes with varying auth_pass values indicating brute-force attempts.
- WAF rules matching base64 patterns in payloads or high connection rates to auth endpoints.
- Anomaly detection in auth logs showing failed attempts from the same IP/source.

## Related

- [[procedures/Web-Sockets-Authentication-Exploitation]]
- [[tools/ws-harness]]
