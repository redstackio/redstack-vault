---
id: proc-shopify-extract-token
tags:
  - shopify
  - preview-token
  - extraction
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
updated_at: '2025-12-14T17:29:56.863Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Extract-Preview-Token-from-View-Store-Link

## Summary

This procedure involves generating and extracting the temporary preview token (?_bt=) from Shopify's 'View your store' link in the Themes section, which can later be reused for bypassing authentication on other stores.

## Description

Shopify generates short-lived preview tokens for bypassing password protection during theme development. Due to lack of store-specific validation, these tokens are reusable across development stores. This step targets the source store's preview URL. Prerequisites: Access to Themes section. Outcome: Isolated token string for manipulation.

## Requirements

1. Active session in source store's Themes section
2. Ability to inspect and copy URL query parameters
3. Browser developer tools (optional for easier extraction)

## Defense

Defensive measures and detection strategies:

- Scope tokens to specific store IDs in backend validation
- Expire tokens immediately after single use
- Monitor for token reuse across stores in logs

## Objectives

1. Generate a valid preview token
2. Isolate the ?_bt= parameter without altering it
3. Verify token grants access on source store

## Instructions

### Step 1: Click View Your Store

**Context**: Trigger the preview URL generation.

In the Themes section, click 'View your store' under the current theme.

> Expected output: Browser redirects to storefront URL with ?_bt= appended.

### Step 2: Inspect the URL

**Context**: Locate the token in the address bar.

Examine the full URL, e.g., https://source-store.myshopify.com/?_bt=longalphanumerictokenhere.

> Expected output: Identification of the ?_bt= value.

### Step 3: Copy the Token

**Context**: Extract for reuse.

Copy the entire ?_bt=<token> string to a secure note or clipboard.

> Expected output: Token ready; test by refreshing to confirm bypass on source.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[shopify]]
- [[preview-token]]
- [[extraction]]
