---
data: >-
  curl -X POST https://3d.cs.money/sync -H "Cookie: steamid=7656119XXXXXXXXXX"
  -H "Content-Type: application/json" -d
  '{"backgrounds":["/assets/images/back3.jpeg"],"builds":[],"edition":1}'
tags:
  - http
  - post
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:47.969Z'
id: d6346999-b002-4b89-9ffe-35791eb88c9e
verified: false
validated: true
submitted: true
---
# curl-sync-request-craft

## Command

```bash
curl -X POST https://3d.cs.money/sync -H "Cookie: steamid=7656119XXXXXXXXXX" -H "Content-Type: application/json" -d '{"backgrounds":["/assets/images/back3.jpeg"],"builds":[],"edition":1}'
```

## Description

Crafts and sends a legitimate POST request to the CS.Money sync endpoint using curl, simulating build synchronization with an authenticated session cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Cookie: steamid=..."` | Sets the session cookie with attacker's Steam ID | Yes |
| `-H "Content-Type: application/json"` | Defines JSON payload type | Yes |
| `-d '{...}'` | JSON body with backgrounds, builds, and edition | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://3d.cs.money/sync -H "Cookie: steamid=7656119XXXXXXXXXX" -H "Content-Type: application/json" -d '{"backgrounds":["/assets/images/back3.jpeg"],"builds":[],"edition":1}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://3d.cs.money/sync -H "Cookie: steamid=7656119XXXXXXXXXX" -H "Content-Type: application/json" -d '{"backgrounds":["/assets/images/back3.jpeg"],"builds":[],"edition":1}'
```

## Expected Output

HTTP 200 OK with JSON response like {"status":"ok"}, indicating successful sync. No errors if cookie is valid.

## Related

- [[commands/curl-idor-exploit]]
