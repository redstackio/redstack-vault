---
id: proc-uuid-2
tags:
  - xss
  - graphql
  - publish
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
updated_at: '2025-12-14T17:25:53.008Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Publish-Product-via-Handshake-Portal

## Summary

This procedure publishes a product containing the stored XSS payload from the Shopify admin to the Handshake portal, triggering the productUpdate GraphQL query to propagate the unsanitized description.

## Description

The Handshake portal integrates with Shopify via GraphQL mutations. Publishing a product updates its details, including the description, without escaping HTML/JS, allowing the payload to reach the internal Handshake site where it can be rendered and executed.

## Requirements

1. Product with malicious description already created in Shopify
2. Access to the Handshake portal (merchant privileges)
3. Product eligible for publishing (e.g., active status)

## Defense

Defensive measures and detection strategies:

- Sanitize inputs in GraphQL resolvers for productUpdate
- Log and audit all product publications for anomalous content
- Use schema validation to reject HTML tags in description fields

## Objectives

1. Trigger GraphQL update to sync the malicious description
2. Expose the payload on the shared Handshake domain
3. Set up conditions for XSS execution on product views

## Instructions

### Step 1: Access Handshake Portal

**Context**: Log into the Handshake integration within Shopify or directly via the portal.

Navigate to the Handshake section in your Shopify admin or visit the Handshake dashboard.

### Step 2: Select and Configure Product

**Context**: Choose the product with the payload and set publishing parameters to initiate the update.

Search for the test product, select a price list and category, then click "Publish" or "Sync".

> This action invokes the productUpdate GraphQL query, updating the description field on the backend.

### Step 3: Confirm Publication

**Context**: Verify the product is now listed in Handshake without errors.

Check the Handshake product listings; the description should be synced, including the hidden payload.

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
- [[graphql]]
- [[publish]]
