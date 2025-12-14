---
tags:
  - xss
  - shopify
  - timeline
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:28:58.830Z'
sub_techniques: []
id: 6447c58e-ab5e-4722-aae5-53283fdbc3ec
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Draft-Orders-Timeline

## Summary

This procedure creates a timeline entry referencing the completed draft order with deleted product, causing the unsanitized description to render and execute the XSS payload upon posting.

## Description

The Draft Orders Timeline in Shopify Admin (/admin/draft_orders/) renders product descriptions without escaping when no product link exists. By referencing the order in a new timeline note and posting, the payload executes in the authenticated admin context, enabling session theft or data exfiltration. Requires admin access; outcomes include JavaScript alert or further exploitation.

## Requirements

1. Completed draft order with deleted malicious product
2. Shopify admin access to timelines
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Output escape all rendered order data in timelines using HTML entity encoding
- Implement strict CSP to block unsafe inline scripts
- Monitor admin actions for timeline posts and JS errors

## Objectives

1. Reference the malicious order in a timeline
2. Trigger rendering of unsanitized payload
3. Achieve JavaScript execution in admin session

## Instructions

### Step 1: Create Timeline Entry

**Context**: Navigate to draft orders and add a timeline note.

No specific command; perform via UI:

1. In Shopify admin, go to Orders > Drafts > Select the completed draft (e.g., /admin/draft_orders/18344449).
2. In the timeline section, add a new activity note referencing the order.
3. Click 'Post' or save.

> The timeline renders the raw description, executing the XSS (e.g., alert('XSS') as in xss.png).

### Step 2: Verify Execution

**Context**: Observe the payload trigger.

No specific command; observe in browser:

1. Upon posting, check for alert dialog or console errors.
2. Inspect the rendered HTML for the injected <img> tag.

> Successful execution confirms vulnerability; potential for advanced payloads like session cookie theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- execution
- shopify
- timeline
