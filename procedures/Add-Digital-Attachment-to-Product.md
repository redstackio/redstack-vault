---
id: proc-uuid-2
tags:
  - shopify
  - product-setup
  - attachment
type: procedure
tools:
  - '[[tools/Firefox]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:31.852Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Add-Digital-Attachment-to-Product

## Summary

This procedure configures a product in the Shopify admin to support digital attachments, setting the stage for the malicious file upload in the XSS exploit.

## Description

Once the Digital Downloads App is installed, this step involves navigating to a product in the store admin and activating the digital attachment feature. It requires no special privileges beyond admin access and prepares the upload endpoint for exploitation. Expected outcome is the availability of the upload interface.

## Requirements

1. Installed Digital Downloads App
2. Access to Shopify store admin
3. A product created or existing in the store

## Defense

Defensive measures and detection strategies:

- Monitor admin actions for unusual product modifications
- Sanitize all input fields in admin interfaces

## Objectives

1. Enable file attachment capability on a product
2. Expose the vulnerable upload endpoint
3. Verify setup without triggering alerts

## Instructions

### Step 1: Navigate to Product

**Context**: Log in to the Shopify admin and select a product to modify.

No command required; use the admin dashboard to go to Products > Select Product.

> Ensure the product is editable.

### Step 2: Add Attachment Option

**Context**: Initiate the digital attachment feature provided by the app.

No command required; click 'Add Digital Attachment' button.

> The interface for uploading files should now be visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[shopify]]
- [[product-setup]]
