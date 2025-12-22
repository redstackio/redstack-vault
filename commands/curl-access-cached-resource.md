---
data: 'curl [URL]'
tags:
  - exfiltration
  - web
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 2a1f5ee6-7c5b-4853-986f-ece45fc638fd
created_at: '2025-12-13T09:00:33.984Z'
updated_at: '2025-12-13T09:00:33.984Z'
verified: false
validated: true
submitted: true
---
# Curl Access Cached Resource

## Command

```bash
curl [URL]
```

## Description

This command retrieves the full response from a URL, used to access potentially cached resources in web cache deception scenarios to check for leaked information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[URL]` | Target cached URL | Yes |

## Examples

### Basic Usage

```bash
curl https://ads.tiktok.com/sensitive-page.css
```

### Advanced Usage

```bash
curl https://ads.tiktok.com/sensitive-page.css -o output.txt
```

## Expected Output

The full HTTP response body, potentially containing leaked sensitive data.

## Related

- [[commands/curl-test-cache-behavior]]
- [[procedures/Exploit-Cached-Response-for-Info-Leakage]]
