---
id: 123e4567-e89b-12d3-a456-426614174008
name: shopify-graphql-base-request
type: command
executor: http
data: >-
  POST /admin/internal/web/graphql/flow HTTP/2

  Host: davidola2.myshopify.com

  Cookie: _secure_admin_session_id=93f2f; _secure_admin_session_id_csrf=93f2

  User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:98.0) Gecko/20100101 Firefox/98.0

  Accept: application/json

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Content-Type: application/json

  X-Shopify-Web-Force-Proxy: 1

  X-Csrf-Token: VD...

  Origin: https://davidola2.myshopify.com

  Content-Length: 44

  Dnt: 1

  Sec-Fetch-Dest: empty

  Sec-Fetch-Mode: cors

  Sec-Fetch-Site: same-origin

  Sec-Gpc: 1


  {"operationName":"AppAccessTimeUpdate","variables":{"appId":"gid://shopify/App/1602671"},"query":"mutation
  AppAccessTimeUpdate($appId: ID!) {\n appAccessTimeUpdate(id: $appId) {\n app
  {\n id\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n
  __typename\n }\n}\n"}
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:36.781Z'
platforms:
  - Web
tags:
  - http
  - shopify
  - graphql
verified: false
validated: true
submitted: true
---

# shopify-graphql-base-request

## Command

```http
POST /admin/internal/web/graphql/flow HTTP/2
Host: davidola2.myshopify.com
Cookie: _secure_admin_session_id=93f2f; _secure_admin_session_id_csrf=93f2
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:98.0) Gecko/20100101 Firefox/98.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
X-Shopify-Web-Force-Proxy: 1
X-Csrf-Token: VD...
Origin: https://davidola2.myshopify.com
Content-Length: 44
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Sec-Gpc: 1

{"operationName":"AppAccessTimeUpdate","variables":{"appId":"gid://shopify/App/1602671"},"query":"mutation AppAccessTimeUpdate($appId: ID!) {\n appAccessTimeUpdate(id: $appId) {\n app {\n id\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n __typename\n }\n}\n"}
```

## Description

Example HTTP POST request structure to the GraphQL endpoint, serving as a base template for modification and exploitation in Shopify Admin testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| appId | ID of the app (e.g., 'gid://shopify/App/1602671') | Yes (for this mutation) |

## Examples

### Basic Usage

```http
# As above, initial template
```

### Advanced Usage

```http
# Modified for flow mutations, replace body with templateInstall or activate
```

## Expected Output

JSON response with app details or user errors.

Example: {"data":{"appAccessTimeUpdate":{"app":{"id":"gid://shopify/App/1602671"}}}}

## Related

- [[commands/shopify-templateinstall-mutation]]
- [[procedures/Intercept-and-Modify-Shopify-Admin-Requests]]
