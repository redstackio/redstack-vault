---
tags:
  - idor
  - shopify
  - pdf-download
  - pii-leak
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/shopify-invoice-pdf-download]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1d2b3598-6cde-46ff-9fe8-9f80611b3969
created_at: '2025-12-14T17:26:00.222Z'
updated_at: '2025-12-14T17:26:00.222Z'
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
  - '[[Account Discovery]]'
---
# Retrieve-Leaked-Invoice-PDF

## Summary

This procedure downloads the generated PDF invoice or credit note for an arbitrary ID, exploiting IDOR to obtain files with embedded PII from other merchants, such as full addresses and emails, despite the document header showing the attacker's shop.

## Description

Following the mutation in prior steps, the download endpoint (/invoices/[id]/download.html) serves the PDF without re-validating ownership. This allows direct retrieval of sensitive documents, providing a tangible exfiltration vector for billing data in Shopify environments. Ideal for verifying and extracting leaked info in vulnerability assessments.

## Requirements

1. Authenticated session cookie
2. Invoice ID (theid) from enumeration or mutation job
3. document_type parameter (INVOICE or CREDIT_NOTE)
4. HTTP GET client supporting cookie persistence

## Defense

Defensive measures and detection strategies:

- Validate session ownership on all download endpoints before serving files
- Use time-limited, signed tokens for PDF access instead of direct ID-based URLs
- Scan logs for download requests with mismatched shop IDs
- Employ DLP tools to watermark or block sensitive PDF exfiltration

## Objectives

1. Download unauthorized PDF documents containing full PII
2. Extract and analyze leaked billing details from other shops
3. Confirm end-to-end IDOR exploitation chain

## Instructions

### Step 1: Identify Download URL

**Context**: Use the invoice ID and document_type to construct the GET URL after mutation success.

### Step 2: Send Download Request

**Context**: Fetch the PDF using the authenticated session to bypass any superficial checks.

**Command** ([[commands/shopify-invoice-pdf-download]]):
```bash
curl -X GET "https://admin.shopify.com/store/[yourshop]/invoices/[theid]/download.html?document_type=INVOICE" \
  -H "Cookie: [your_session_cookie]" \
  --output leaked_invoice.pdf
```

> The output is a PDF file. Open it to verify leaked data: attacker's shop in header but victim's email, address, and invoice details in body.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/shopify-invoice-pdf-download]]

## Tools Used


## Tags

- idor
- shopify
- pdf-download
- pii-leak
