---
id: proc-uuid-2
tags:
  - recon
  - shopify
  - theme-id
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-13T23:52:55.662Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract-Shopify-Theme-ID-from-Page-Source

## Summary

This procedure involves inspecting the HTML source of a Shopify storefront to extract the active theme ID, a critical prerequisite for crafting XSS payloads in the theme preview feature.

## Description

Shopify embeds theme information in client-side JavaScript variables like Shopify.theme.id. By viewing the page source, attackers can locate and copy this ID without authentication. This step is low-risk and manual, enabling the construction of preview URLs that exploit unescaped parameters. Outcomes include obtaining a numeric ID for use in malicious requests.

## Requirements

1. Loaded Shopify storefront page
2. Browser with developer tools or view source capability
3. Basic HTML/JavaScript knowledge

## Defense

Defensive measures and detection strategies:

- Obfuscate or remove unnecessary client-side theme details in production builds
- Monitor for automated scraping of page sources via user-agent analysis

## Objectives

1. Retrieve the exact theme ID for preview manipulation
2. Understand the current theme configuration
3. Enable payload targeting without errors

## Instructions

### Step 1: Open Page Source

**Context**: Access the raw HTML to search for embedded theme data.

Instructions: Right-click on the loaded storefront page and select 'View Page Source' (or Ctrl+U/Cmd+U).

> The full HTML document opens; use Ctrl+F/Cmd+F to search.

### Step 2: Locate and Copy Theme ID

**Context**: Identify the JavaScript variable containing the theme ID.

Instructions: Search for 'Shopify.theme' and find the line like 'id: 123456789'. Copy the numeric value.

> The ID is a unique integer; store it securely for the next step. If not found, reload the page and retry.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[shopify]]
- [[theme-id]]
- [[web]]
