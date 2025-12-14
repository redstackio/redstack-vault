---
id: proc-shopify-extract-theme-id-927567
tags:
  - shopify
  - id-extraction
  - recon
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:29:29.095Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Extract-Paid-Theme-ID-from-Shopify-Admin

## Summary

This procedure retrieves the unique GraphQL ID of an installed paid theme from the Shopify admin URL, enabling targeting in subsequent API mutations to bypass purchase requirements.

## Description

Targeting Shopify's admin interface, this step involves navigating to the theme editor for the paid (demo) theme and parsing the URL for the theme ID. The ID is in the format [theme_id] within https://yourshop.myshopify.com/admin/themes/[theme_id]/editor, which translates to gid://shopify/OnlineStoreTheme/[theme_id] for GraphQL. Prerequisites include an installed paid theme and browser access. This reconnaissance step is low-impact but critical for precise API abuse.

## Requirements

1. Installed paid theme in Shopify admin
2. Browser developer tools for URL inspection
3. Authenticated admin session

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize internal IDs in URLs to hinder extraction
- Log and alert on frequent theme editor accesses
- Implement client-side ID validation before API calls

## Objectives

1. Identify the paid theme's GraphQL-compatible ID
2. Prepare ID for use in modified API requests
3. Ensure ID accuracy to avoid mutation failures

## Instructions

### Step 1: Access Theme Editor

**Context**: Navigate to the paid theme's customization page to expose the ID in the URL.

In Shopify admin, go to Themes > Select paid theme > Click 'Customize'.

> URL updates to include /themes/[theme_id]/editor.

### Step 2: Parse and Copy ID

**Context**: Extract the numeric ID from the URL bar.

Copy the [theme_id] segment (e.g., 1234567890) and format as gid://shopify/OnlineStoreTheme/[theme_id].

> Use browser console if needed: location.href.split('/')[5] to grab ID programmatically.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- shopify
- id-extraction
- recon
