---
id: cmd-shopify-signup-001
data: >-
  curl -X POST https://app.shopify.com/services/signup/setup -d
  "signup[shop_name]=testdevstore" -d "signup[email]=test@example.com" -d
  "signup[password]=password123" -d "signup_types=affiliate_shop" -d
  "signup_source=development+shop" -d
  "extra[affiliate_shop]=extracted_signature_here" -d "address[first_name]=Test"
  -d "address[last_name]=User" -d "address[address1]=123 Test St" -d
  "address[city]=Test City" -d "address[zip]=12345" -d "address[country]=US"
tags:
  - web
  - post-request
  - shopify
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:57.381Z'
verified: false
validated: true
submitted: true
---
# shopify-signup-post

## Command

```bash
curl -X POST https://app.shopify.com/services/signup/setup \
  -d "signup[shop_name]=testdevstore" \
  -d "signup[email]=test@example.com" \
  -d "signup[password]=password123" \
  -d "signup_types=affiliate_shop" \
  -d "signup_source=development+shop" \
  -d "extra[affiliate_shop]=extracted_signature_here" \
  -d "address[first_name]=Test" \
  -d "address[last_name]=User" \
  -d "address[address1]=123 Test St" \
  -d "address[city]=Test City" \
  -d "address[zip]=12345" \
  -d "address[country]=US"
```

## Description

This curl command sends a form-encoded POST request to Shopify's signup endpoint to create a development store using an extracted signature, bypassing authorization checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-d` | Form data parameters (e.g., signup[shop_name]) | Yes |
| `extra[affiliate_shop]` | The persistent signature token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://app.shopify.com/services/signup/setup -d "signup[shop_name]=teststore" -d "extra[affiliate_shop]=sig_here"
```

### Advanced Usage

Include full address and auth fields as shown in the main command for complete signup.

## Expected Output

Successful response: HTTP 200/302 with redirect to store setup or JSON success. Failure: 401/403 if signature invalid.

## Related

- [[Related Procedure: Create-Development-Store-with-Extracted-Signature]]
