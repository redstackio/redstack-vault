---
tags:
  - shopify
  - api-bypass
  - post-request
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:28:36.746Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
id: 6f2972e3-eeea-4b4c-9ff8-acefa189f5ef
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Alternative-POST-Request-for-Tax-Override

## Summary

This procedure bypasses the UI entirely by sending a direct POST request to the tax override endpoint with a foreign collection_id, confirming the vulnerability via API.

## Description

Instead of form submission, craft a POST to /admin/settings/taxes/*/override, where * is the tax zone ID. Include parameters like authenticity_token (from the page source), tax_override[collection_id]=foreign_id (e.g., 137861635), and tax details (e.g., rate=50 for TX state). This exploits the same lack of ShopID validation in Shopify's Rails API. Use tools like curl or Postman, with cookies from an authenticated session. Expected outcome: Successful override addition with unauthorized data exposure.

## Requirements

1. Authenticated session cookies and authenticity_token from the taxes page
2. Knowledge of tax zone ID and foreign collection_id
3. Tool for HTTP requests (e.g., curl, browser console)

## Defense

Defensive measures and detection strategies:

- Verify authenticity_token and session ownership in API endpoints
- Implement parameter whitelisting and ShopID cross-checks
- WAF rules to block mismatched collection_ids in POST bodies

## Objectives

1. Demonstrate bypass without UI dependency
2. Add override via direct API call
3. Expose collection data in response or subsequent GET

## Instructions

### Step 1: Extract Tokens

**Context**: Gather necessary auth elements from the page.

Use DevTools Network tab to capture authenticity_token from a prior request or inspect the form.

### Step 2: Craft and Send POST

**Context**: Simulate form submission with manipulated data.

Send a POST request to https://SHOP.myshopify.com/admin/settings/taxes/*/override with body:

form data: authenticity_token=TOKEN, tax_override[is_shipping]=false, tax_override[collection_id]=137861635, tax_override[tax_override_regions_attributes][0][zone]=state::TX, tax_override[tax_override_regions_attributes][0][rate]=50

> Using curl example (adapt with real token/cookies): The server responds with success, and a GET to the taxes page shows the foreign collection name.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- shopify
- api-bypass
- post-request
