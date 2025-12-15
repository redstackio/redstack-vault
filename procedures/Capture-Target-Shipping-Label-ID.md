---
id: proc-884159-capture-label-id
tags:
  - idor
  - shopify
  - graphql
  - recon
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:36.579Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Capture-Target-Shipping-Label-ID

## Summary

This procedure involves accessing an unfulfilled order in the target Shopify store, initiating the shipping label creation process to intercept the GraphQL request, voiding any created label, and re-initiating to extract the shipping label ID for use in IDOR exploitation.

## Description

In the context of the Shopify IDOR vulnerability, this step gathers the critical shippingLabelId (a GraphQL global ID) from the target store. It requires legitimate access to the target store's admin panel. The process simulates normal label creation to capture details without completing the purchase, allowing repeated testing. Expected outcomes include obtaining the ID like gid://shopify/ShippingLabel/522221879427, which can then be referenced in unauthorized requests.

## Requirements

1. Valid shop owner credentials for the target store
2. Access to Shopify admin panel and unfulfilled order
3. Ability to intercept HTTP requests (browser dev tools or proxy)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on shipping label creation endpoints
- Log and monitor GraphQL mutations for anomalous shippingLabelId references
- Enforce strict session scoping to prevent cross-store ID usage

## Objectives

1. Extract the target's shipping label ID for unauthorized access
2. Reset order state to enable multiple captures
3. Validate the ID format for GraphQL compatibility

## Instructions

### Step 1: Access Unfulfilled Order and Initiate Label Creation

**Context**: Log in to the target store's Shopify admin and navigate to an unfulfilled order to trigger the initial GraphQL request for label purchase.

Use browser dev tools or [[tools/curl]] to capture the request to https://mailbox.shopifycloud.com/graphql/labels?sessionId={{sessionId}} with the PurchaseShippingLabels mutation.

> Navigate to the order, click 'Create a shipping label', and copy the CURL command from the network tab.

### Step 2: Void the Created Shipping Label

**Context**: If a label is generated, void it to revert the order state without completing the shipment.

In the Shopify admin, after label creation, select the option to void the label.

> This resets the fulfillment status for re-testing.

### Step 3: Re-Open Order and Extract Shipping Label ID

**Context**: Re-initiate the process to obtain the ID from the resulting URL or response.

Re-open the order, click 'Create a shipping label' again, and note the shipping_label_ids from the URL (e.g., gid://shopify/ShippingLabel/522221879427).

> Verify the ID is a valid GraphQL global ID starting with gid://shopify/ShippingLabel/.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]
- [[tools/Web-Browser]]

## Tags

- idor
- shopify
- graphql
