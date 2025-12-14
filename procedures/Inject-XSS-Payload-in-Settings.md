---
id: proc-inject-xss-shopify-settings
tags:
  - xss
  - stored-xss
  - waf-bypass
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
updated_at: '2025-12-13T23:52:44.545Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Settings

## Summary

This procedure demonstrates injecting a stored XSS payload into Shopify's general settings street address field by bypassing the WAF with an HTML comment prefix, allowing persistent script storage for later execution.

## Description

Shopify's admin settings include a street address field vulnerable to stored XSS due to incomplete sanitization. The WAF blocks direct HTML tags, but prepending '<!-->' evades detection, enabling an SVG element with an onload JavaScript handler to be saved. This payload executes when the address is rendered in views like the live dashboard, potentially leading to session cookie theft or client-side attacks in the admin context.

## Requirements

1. Authenticated admin session in Shopify
2. Access to /admin/settings/general endpoint
3. Knowledge of WAF evasion techniques (e.g., HTML comments)

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all form fields
- Update WAF rules to detect comment-prefixed payloads and SVG onload attributes
- Regularly audit stored data in settings for malicious content

## Objectives

1. Bypass WAF to store unsanitized JavaScript
2. Persist the payload in the database via settings save
3. Set up for execution in admin views

## Instructions

### Step 1: Locate Vulnerable Field

**Context**: Identify the injection point in the settings form.

Navigate to https://[store].myshopify.com/admin/settings/general and scroll to the "Store details" > "Address" section. Focus on the "Street address" input field.

> The field accepts text input without immediate validation feedback.

### Step 2: Craft and Inject Payload

**Context**: Enter the evasion payload to store the XSS.

Input the following into the street address field: `(xss)<!--><svg/onload=alert(document.domain)>)`. Click "Save" to submit.

> Expected output: Settings update succeeds; payload is stored without triggering WAF.

### Step 3: Verify Storage

**Context**: Confirm the payload persists post-save.

Reload the settings page and inspect the street address field or view page source to see the injected content.

> Success if the full payload, including SVG, is visible in the input.

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
- stored-xss
- waf-bypass
