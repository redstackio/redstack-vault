---
id: cmd-curl-observe
data: >-
  curl -v
  "https://assistant-client.meteorapp.com/shopify/callback?code=6aae881ab9c4f12d5b264e6c871a108a&hmac=6109806a12b0439d6a2dce2d547344eb1c2c53e9691259f39eefbb93b9c9c97b&shop=pappuza-2.myshopify.com&timestamp=1494008598"
tags:
  - web
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:26.661Z'
verified: false
validated: true
submitted: true
---
# curl-observe-callback

## Command

```bash
curl -v "https://assistant-client.meteorapp.com/shopify/callback?code=6aae881ab9c4f12d5b264e6c871a108a&hmac=6109806a12b0439d6a2dce2d547344eb1c2c53e9691259f39eefbb93b9c9c97b&shop=pappuza-2.myshopify.com&timestamp=1494008598"
```

## Description

This command observes the Shopify Alexa app callback URL with legitimate parameters to inspect the response and redirect behavior during app installation simulation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output showing headers and details | Yes |
| URL | Full callback URL with parameters | Yes |

## Examples

### Basic Usage

```bash
curl -v "https://assistant-client.meteorapp.com/shopify/callback?shop=example.myshopify.com"
```

### Advanced Usage

```bash
curl -v -H "User-Agent: Mozilla/5.0" "https://assistant-client.meteorapp.com/shopify/callback?code=example&hmac=example&shop=example.myshopify.com&timestamp=1234567890"
```

## Expected Output

Verbose logs with HTTP/1.1 302 Found, Location: https://example.myshopify.com/admin/oauth/authorize, confirming legitimate redirect.

## Related

- [[Related Procedure|procedures/Observe-Shopify-Alexa-App-Installation-Callback]]
