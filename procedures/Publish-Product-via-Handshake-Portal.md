---
tags:
  - xss
  - graphql
  - shopify
  - handshake
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
updated_at: '2025-12-14T03:16:25.597Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 272a577b-2177-4d7a-a7ed-08b99bbbdde3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Publish-Product-via-Handshake-Portal

## Summary

This procedure publishes a product containing a stored XSS payload from the Shopify store to the Handshake portal, utilizing the productUpdate GraphQL query to sync the unsanitized description.

## Description

After injecting the payload, this step involves accessing the Handshake portal (integrated with Shopify) to select pricing and category details for the product. Publishing triggers a GraphQL mutation (productUpdate) that updates the product data and syncs it to the Handshake ecosystem. Due to insufficient sanitization in the plugin, the malicious HTML is preserved and propagated, setting the stage for execution when viewed on the internal Handshake site.

## Requirements

1. Authentication to the Handshake portal
2. Product with injected payload set to Active in Shopify
3. Basic understanding of GraphQL mutations (handled via UI)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize GraphQL inputs server-side before processing
- Log all productUpdate queries for anomalous payloads
- Implement rate limiting on product publishing actions

## Objectives

1. Sync the malicious product to the Handshake catalog
2. Propagate the unsanitized description via GraphQL
3. Make the payload available for rendering on shared domains

## Instructions

### Step 1: Access Handshake Portal

**Context**: Log in to the Handshake integration within Shopify to manage product syncing.

Navigate to the Handshake portal from the Shopify apps section.

### Step 2: Configure Product Details

**Context**: Assign necessary metadata to the product to enable publishing.

Select the target product, set a price, and choose a category.

### Step 3: Publish the Product

**Context**: Initiate the sync process, which invokes the productUpdate GraphQL query.

Click the Publish button to update and sync the product to Handshake.

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
- graphql
- publishing
