---
id: proc-uuid-3
tags:
  - xss
  - payload
  - url-crafting
  - shopify
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
updated_at: '2025-12-13T23:52:55.654Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Construct-Malicious-Theme-Preview-URL

## Summary

This procedure crafts a URL for Shopify's theme preview endpoint that injects an XSS payload into the theme_handle parameter, exploiting the lack of single-quote escaping to break out of string contexts.

## Description

The theme preview feature accepts parameters like theme_handle and preview_theme_id. By URL-encoding a payload such as xx'-alert(document.cookie)-', attackers can inject JavaScript that executes on load. This manual construction targets the vulnerability, allowing arbitrary code execution on the storefront. Prerequisites include the theme ID; outcomes are a navigable URL leading to XSS.

## Requirements

1. Extracted theme ID from previous step
2. Target store name
3. URL encoding knowledge (e.g., %27 for ')

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and escaping for URL parameters in preview features
- Log and block requests with suspicious query strings containing script tags or alerts

## Objectives

1. Create a functional malicious URL
2. Ensure payload bypasses basic sanitization
3. Prepare for immediate execution

## Instructions

### Step 1: Build Base URL Structure

**Context**: Start with the storefront base and add preview parameters.

Instructions: Form the base as https://<store-name>.myshopify.com/?theme_handle= &style_id=1&style_handle=1&preview_theme_id=<id>.

> Replace placeholders; style_id and style_handle are set to 1 as defaults.

### Step 2: Insert and Encode Payload

**Context**: Add the XSS payload to theme_handle to exploit escaping flaws.

Instructions: Set theme_handle to xx%27-alert(document.cookie)-%27, where %27 is the encoded single quote.

> Full example: https://echo.myshopify.com/?theme_handle=xx%27-alert(document.cookie)-%27&style_id=1&style_handle=1&preview_theme_id=123456789. Verify encoding in a URL tool if needed.

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
- [[payload]]
- [[url-crafting]]
- [[shopify]]
