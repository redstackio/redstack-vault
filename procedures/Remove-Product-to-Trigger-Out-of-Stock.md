---
tags:
  - xss
  - bypass
  - out-of-stock
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
  - Shopify
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f78795e6-e190-4c48-abd2-1591ec330797
created_at: '2025-12-14T03:46:32.052Z'
updated_at: '2025-12-14T03:46:32.052Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Remove-Product-to-Trigger-Out-of-Stock

## Summary

This procedure deletes or deactivates the malicious product to set it as out-of-stock, bypassing sanitization that applies only to active products and exposing the payload in admin edits.

## Description

The vulnerability hinges on how Judge.me handles out-of-stock products in question edits; active product protections are bypassed. Deleting the product (or setting to out-of-stock) keeps the question intact but removes context-based sanitization. This step requires admin access. Expected outcome: Product unavailable, question persists with raw payload.

## Requirements

1. Shopify admin access
2. Malicious product and associated question exist
3. No additional tools needed

## Defense

Defensive measures and detection strategies:

- Apply uniform sanitization regardless of product status
- Log product deletions and correlate with question activity
- Prevent question edits for deleted product associations

## Objectives

1. Alter product state to evade mitigations
2. Preserve question for admin interaction
3. Set up unsanitized display

## Instructions

### Step 1: Access Admin Products

**Context**: Log in to Shopify admin.

Go to Products section in the dashboard.

### Step 2: Delete or Deactivate

**Context**: Remove the product to trigger the bypass.

Select the malicious product and choose 'Delete' or edit to set availability to zero/out-of-stock. Confirm the action.

> Product should no longer appear in storefront searches.

### Step 3: Confirm Persistence

**Context**: Verify question remains.

Navigate to Judge.me > Questions; the question should still list the now-unavailable product.

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
- [[bypass]]
