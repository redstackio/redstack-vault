---
data: >-
  curl -X POST https://DOMAIN/admin/api/xauth -H "Content-Type:
  application/json" -d '{"email":"EMAIL","password":"PASSWORD"}'
tags:
  - auth
  - shopify
type: command
executor: bash
platforms:
  - Web
id: 2a8ea31e-6544-4ed0-a35b-2ed31acda559
created_at: '2025-12-14T17:29:57.260Z'
updated_at: '2025-12-14T17:29:57.260Z'
verified: false
validated: true
submitted: true
---
# post-shopify-xauth-login

## Command

```bash
curl -X POST https://alwayzhack.myshopify.com/admin/api/xauth \
  -H "Content-Type: application/json" \
  -d '{"email":"lowpriv@example.com","password":"password"}'
```

## Description

This command authenticates a low-privileged user via Shopify's xauth API to obtain a Ping access_token for use in IDOR exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| email | Low-priv user email | Yes |
| password | User password | Yes |
| DOMAIN | Shop domain (e.g., alwayzhack.myshopify.com) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.myshopify.com/admin/api/xauth \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"pass"}'
```

### Advanced Usage

Add verbose output:

```bash
curl -v -X POST https://DOMAIN/admin/api/xauth -H "Content-Type: application/json" -d '{"email":"EMAIL","password":"PASSWORD"}'
```

## Expected Output

JSON response: {"access_token": "eyJ..."}. Success if token present; error if invalid creds.

## Related

- [[Related Procedure: Obtain-Low-Priv-Access-Token]]
