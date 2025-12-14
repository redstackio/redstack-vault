---
id: proc-uuid-002
name: Create-and-Upload-Price-List
tags:
  - shopify
  - csv-import
  - price-list
type: procedure
tools: []
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
updated_at: '2025-12-14T00:11:16.209Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-and-Upload-Price-List

## Summary

This procedure creates a new price list in Shopify's Wholesale channel by modifying and uploading a sample CSV file, setting up a target for XSS payload injection during subsequent updates.

## Description

To exploit the stored XSS, a legitimate price list must first be created via CSV import. This involves downloading Shopify's sample CSV, editing it to include a real product SKU from the store, and uploading it through the admin interface. The process targets the /admin/shops/x/price_lists endpoint indirectly. Prerequisites: Wholesale channel access. Outcomes: A new price list entry available for editing.

## Requirements

1. Access to Shopify admin with Wholesale enabled
2. Product SKU from the target store
3. Text editor for CSV modification

## Defense

Defensive measures and detection strategies:

- Validate CSV uploads for malicious content using file scanners
- Rate-limit price list imports to prevent abuse
- Log all CSV uploads and review for anomalies in file names or content

## Objectives

1. Establish a modifiable price list entry
2. Introduce a CSV file name that can be targeted for injection
3. Prepare for request interception

## Instructions

### Step 1: Download and Modify Sample CSV

**Context**: Obtain the official sample and adapt it with store-specific data.

No specific command; perform via browser and editor:

- Download from https://help.shopify.com/manual/sell-online/wholesale/channel/price-lists-customers/import-prices/sample-csv-sku.csv.
- Edit to include a valid SKU, e.g., add row: "handle,price,compare_at_price,sku" with "product-handle,10.00,,VALID-SKU".

> Modified CSV ready for upload, ensuring it passes validation.

### Step 2: Upload CSV to Create Price List

**Context**: Submit the file through the import interface.

No specific command; perform via browser:

- In Wholesale admin, go to Price Lists > Create > Import CSV, select and upload the file.

> Price list created and visible in the list view.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[csv-import]]
- [[price-list]]
