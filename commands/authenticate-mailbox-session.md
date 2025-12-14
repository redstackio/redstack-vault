---
id: cmd-884159-auth-session
data: >-
  curl 'https://mailbox.shopifycloud.com/session/authentication' -H 'Connection:
  keep-alive' -H 'Cache-Control: max-age=0' -H 'User-Agent: Mozilla/5.0
  (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko)
  Chrome/83.0.4103.61 Safari/537.36' -H 'Content-Type: application/json' -H
  'Accept: */*' -H 'Origin: https://{shop}.myshopify.com' -H 'Sec-Fetch-Site:
  cross-site' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H
  'Accept-Language: en-US,en;q=0.9' --compressed
tags:
  - authentication
  - session
  - shopify
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.565Z'
verified: false
validated: true
submitted: true
---
# authenticate-mailbox-session

## Command

```bash
curl 'https://mailbox.shopifycloud.com/session/authentication' -H 'Connection: keep-alive' -H 'Cache-Control: max-age=0' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: */*' -H 'Origin: https://{shop}.myshopify.com' -H 'Sec-Fetch-Site: cross-site' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Accept-Language: en-US,en;q=0.9' --compressed
```

## Description

This curl command initiates session authentication with Shopify's mailbox service, providing a redirect URL for completing the flow in a browser. Used to obtain a valid session ID for GraphQL requests in IDOR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H Origin` | Attacker's shop domain (replace {shop} with actual, e.g., attacker.myshopify.com) | Yes |
| `--compressed` | Handles gzip compression | No |
| Headers (User-Agent, etc.) | Mimics browser request for CORS compatibility | Yes |

## Examples

### Basic Usage

```bash
curl 'https://mailbox.shopifycloud.com/session/authentication' -H 'Origin: https://attacker.myshopify.com' [other headers]
```

### Advanced Usage

Include additional auth payload if needed, but typically empty body.

## Expected Output

JSON response like {"redirectUrl": "https://..."} for browser completion.

## Related

- [[commands/purchase-shipping-labels-graphql]]
- [[procedures/Initiate-Attacker-Session-Authentication]]
