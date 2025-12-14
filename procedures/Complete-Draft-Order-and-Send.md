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
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:58.836Z'
sub_techniques: []
id: f36a3250-8d2f-47dc-840a-82ee25fb5cf2
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Complete-Draft-Order-and-Send

## Summary

This procedure finalizes the malicious draft order by sending it to a recipient and marking it as completed, ensuring the payload remains in the order data for later rendering.

## Description

After creating the draft with the malicious product, this step simulates order completion to transition it to a 'completed' state in Shopify's admin. The payload in the product name persists as part of the order history. This is performed in the web admin interface and requires no additional tools beyond authentication. Outcomes include the order appearing in Completed Drafts without executing the payload yet.

## Requirements

1. Existing malicious draft order in Shopify admin
2. Authenticated session with order management permissions
3. Recipient email for sending the draft

## Defense

Defensive measures and detection strategies:

- Audit draft orders for suspicious line items or descriptions
- Log all order completions and review for anomalies
- Sanitize order data during state transitions

## Objectives

1. Send and complete the draft order
2. Preserve the malicious payload in order records
3. Verify order status change

## Instructions

### Step 1: Send Draft Order

**Context**: Open the draft and send it to initiate the process.

No specific command; perform via UI:

1. In Shopify admin, go to Orders > Drafts.
2. Open the malicious draft.
3. Click 'Send draft' and enter a recipient email.
4. Confirm send.

> The draft is emailed, maintaining the product data.

### Step 2: Mark as Completed

**Context**: Finalize the order status.

No specific command; perform via UI:

1. After sending, click 'Mark as paid' or complete via actions.
2. Verify it moves to Completed Drafts.

> Order now in completed state (e.g., visible in screenshots like order.png).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- shopify
- order-completion
