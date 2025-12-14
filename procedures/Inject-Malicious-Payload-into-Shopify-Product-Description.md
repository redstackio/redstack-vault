---
tags:
  - xss
  - injection
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
updated_at: '2025-12-14T03:16:25.602Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: e43eee55-b1c3-4e88-97e7-bcea632a76b3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-Payload-into-Shopify-Product-Description

## Summary

This procedure injects a malicious HTML payload into a Shopify product's description field in HTML mode, storing cross-site scripting code that can later be rendered unsanitized.

## Description

In the context of exploiting a stored XSS vulnerability in Shopify's Handshake plugin, this step involves creating or editing a product in the Shopify admin panel. By switching to HTML editing mode, an attacker can directly insert raw HTML/JavaScript, such as an image tag with an onerror handler. The product is then set to Active status, persisting the payload in the backend database. This sets up the vulnerability for the subsequent publishing step via GraphQL, where the lack of sanitization allows execution on viewing pages.

## Requirements

1. Access to Shopify admin panel with product creation/editing permissions
2. Web browser for UI interaction
3. Knowledge of basic HTML/JavaScript payloads

## Defense

Defensive measures and detection strategies:

- Enable content security policy (CSP) to restrict inline script execution
- Sanitize all user-supplied HTML inputs using libraries like DOMPurify
- Monitor product description fields for suspicious tags like <img> with onerror

## Objectives

1. Store malicious JavaScript in the product description
2. Prepare the product for syncing without triggering immediate errors
3. Enable arbitrary code execution upon rendering

## Instructions

### Step 1: Access Product Editor

**Context**: Log in to the Shopify admin and navigate to the product creation or editing interface to access the description field.

Navigate to Products > Add product (or edit an existing one) in the Shopify dashboard.

### Step 2: Switch to HTML Mode and Inject Payload

**Context**: Enable raw HTML editing to bypass any visual editor sanitization and insert the XSS payload.

Click the < > button to toggle HTML mode in the description editor. Insert the following payload:

```html
<img src=x onerror=prompt(document.domain)>
```

Save the changes.

### Step 3: Set Product Status

**Context**: Activate the product to make it eligible for publishing and rendering.

Set the product status to Active and save the product.

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
- shopify
- injection
