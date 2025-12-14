---
tags:
  - verification
  - impact-assessment
  - order-manipulation
  - shopify
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fetch-transaction]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:20.326Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 9ed20824-3064-4eb1-9a5f-cac11051c09f
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Verify-Signature-in-Order-or-Transaction-View

## Summary

This procedure checks the target order or transaction endpoint to confirm the uploaded malicious signature file is associated and visible, validating the exploitation.

## Description

After upload, access the Shopify order page or API endpoint `/admin/orders/_order_id_/transaction.json` to inspect for the new signature. The file should appear in the signatures list, and viewing it may trigger the embedded JS. This confirms unauthorized modification in the web admin environment, with outcomes including proof of data tampering.

## Requirements

1. Order ID and transaction ID from target
2. Authenticated session (low-priv sufficient for view)
3. Access to admin UI or API

## Defense

Defensive measures and detection strategies:

- Display uploaded files in isolated viewers (no direct rendering)
- Alert on new signatures from unauthorized users
- Regularly audit transaction attachments

## Objectives

1. Confirm file association with transaction
2. Verify visibility in order views
3. Test JS execution for full impact

## Instructions

### Step 1: Access Order Page

**Context**: Navigate to the admin order details UI.

Log in and go to `/admin/orders/_order_id_` to view signatures section.

> Look for the uploaded SVG in the transaction signatures list.

### Step 2: Query Transaction API

**Context**: Use API to fetch transaction details programmatically.

Execute [[commands/curl-fetch-transaction]]:

```bash
curl -H "Cookie: shop_session=your_session" https://your-shop.myshopify.com/admin/orders/_order_id_/transaction.json
```

> Response JSON includes 'signatures' array with the new file URL.

### Step 3: Test File Rendering

**Context**: Load the S3 URL or view in UI to trigger JS.

Click or request the signature URL; observe alert or console errors.

> Success if JS executes, confirming client-side impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-transaction]]

## Tools Used


## Tags

- [[verification]]
- [[web]]
