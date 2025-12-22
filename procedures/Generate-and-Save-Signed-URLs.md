---
id: uuid-placeholder-4
tags:
  - shopify
  - signed-urls
  - path-hmac
  - connectors
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
updated_at: '2025-12-14T17:30:07.359Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Generate-and-Save-Signed-URLs

## Summary

This procedure generates and captures non-expiring signed URLs from Flow connector settings, which rely on a shared path_hmac parameter vulnerable to reuse.

## Description

By clicking settings in the connectors page, URLs are generated for services like Google Sheets. These URLs do not expire and use a path_hmac identical across staff, without session checks, enabling later unauthorized reuse.

## Requirements

1. Access to Flow connectors as staff.
2. Browser developer tools or URL copier for saving links.
3. Target services: Google Sheets, Trello, Asana.

## Defense

Defensive measures and detection strategies:

- Implement URL expiration and unique HMACs per session/user.
- Monitor for reused signed URLs in app logs.

## Objectives

1. Obtain exploitable signed URLs.
2. Capture path_hmac for bypass.
3. Enable post-revocation access.

## Instructions

### Step 1: Open Connectors Page

**Context**: Start interaction.

Ensure on https://[shop].myshopify.com/admin/apps/flow/connectors.

### Step 2: Click Settings Links

**Context**: Trigger URL generation.

For each service (Google Sheets, Trello, Asana), click 'Settings' or 'Connect' to generate the URL.

### Step 3: Save URLs

**Context**: Capture for reuse.

Copy the full URL, e.g., https://flow-connectors.shopifycloud.com/gsheet/connect?shop_domain=[shop].myshopify.com&shop_id=[id]&path_hmac=[hmac-value]. Save to a file or note.

> Expected output: URLs with valid parameters saved.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[signed-urls]]
- [[path-hmac]]
