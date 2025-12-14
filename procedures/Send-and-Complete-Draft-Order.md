---
tags:
  - xss
  - shopify
  - draft-order
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 905c477b-73ae-40fc-88e7-3c69aabb4727
created_at: '2025-12-14T03:16:25.348Z'
updated_at: '2025-12-14T03:16:25.348Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Send-and-Complete-Draft-Order

## Summary

This procedure sends the malicious draft order to an email and marks it as completed, transitioning it to a referenceable state in the Completed Drafts list while preserving the injected XSS payload for later exploitation.

## Description

After creating a draft with a malicious product, sending it simulates customer interaction, and completing it moves the order to a viewable status. The payload in the product name remains intact. This step requires admin access and ensures the order URL (e.g., /admin/draft_orders/123456) can be referenced elsewhere. Outcomes include the order appearing in Completed Drafts, ready for manipulation.

## Requirements

1. Existing draft order with malicious payload
2. Valid email for sending (can be test)
3. Shopify admin permissions to complete orders

## Defense

Defensive measures and detection strategies:

- Audit logs for unusual draft completions or sends
- Sanitize all order data on status changes
- Rate-limit draft order creations and completions

## Objectives

1. Transition draft to completed status without losing payload
2. Generate referenceable order URL
3. Maintain payload for timeline rendering

## Instructions

### Step 1: Send Draft

**Context**: Initiate send to log the draft as in-progress.

UI action: From draft page, click "Send draft order" and enter email.

> Expected: Email sent; draft status updates.

### Step 2: Complete Order

**Context**: Mark as completed to archive it accessibly.

UI action: Click "Mark as completed" or equivalent.

> Expected: Order moves to Completed Drafts; URL noted (e.g., https://store.myshopify.com/admin/draft_orders/2797121).

### Step 3: Verify Status

**Context**: Confirm payload persistence.

UI action: View order details.

> Expected: Malicious product name visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[shopify]]
- [[draft-order]]
