---
tags:
  - connectors
  - signed-url
  - capture
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:44.802Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2d52ab3e-4f7b-4568-bf05-6486fc9e8eea
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Connect-External-Services-and-Capture-Signed-URL

## Summary

This procedure connects external services like Google Sheets, Trello, and Asana to Shopify's Flow app using a staff account, capturing the signed URL generated during the Google Sheets connection for later exploitation.

## Description

Log in as the staff user and navigate to the Flow connectors in the Shopify admin. Connect accounts for Google Sheets, Trello, and Asana by clicking the respective buttons, which may involve OAuth flows. Specifically for Google Sheets, the connection redirects to a signed URL on flow-connectors.shopifycloud.com with parameters like shop_domain, shop_id, timestamp, and path_hmac. Save this URL completely, as it expires after one hour but can be refreshed. This step establishes the baseline connections vulnerable to post-removal modification.

## Requirements

1. Active staff account with 'Apps' permission
2. Valid accounts for Google Sheets, Trello, Asana
3. Access to https://[Your-Shop].myshopify.com/admin/apps/flow/connectors

## Defense

Defensive measures and detection strategies:

- Validate signed URLs against current user permissions on each access
- Log all connector connections and monitor for unusual OAuth redirects
- Use short-lived tokens and invalidate on permission changes

## Objectives

1. Establish connections to external services via Flow
2. Capture exploitable signed URL parameters
3. Prepare for authorization testing post-removal

## Instructions

### Step 1: Navigate to Connectors

**Context**: Access the Flow connectors interface as staff.

No specific command; manual UI navigation:

Log in as staff > Go to https://[Your-Shop].myshopify.com/admin/apps/flow/connectors.

> Connectors list loads, showing available services.

### Step 2: Connect Services

**Context**: Link external accounts to Flow workflows.

No specific command; manual UI actions:

Click 'Connect' for Google Sheets, Trello, Asana > Authorize with respective accounts.

> Connections succeed; services now integrated into Flow.

### Step 3: Capture Signed URL

**Context**: During Google Sheets interaction, grab the redirect URL.

No specific command; manual capture:

Click Google Sheets connector > Redirects to https://flow-connectors.shopifycloud.com/gsheet/connect?shop_domain=...&shop_id=...&timestamp=[TIMESTAMP]&path_hmac=[PATH_HMAC] > Copy full URL.

> URL saved with all parameters for exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[connectors]]
- [[signed-url]]
- [[capture]]
