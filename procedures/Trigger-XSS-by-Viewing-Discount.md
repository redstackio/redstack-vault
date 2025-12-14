---
tags:
  - xss
  - execution
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
updated_at: '2025-12-13T23:55:06.671Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 3f1132b6-ab4b-4b51-8da4-542f4cf26b30
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Discount

## Summary

This procedure executes the stored XSS payload by viewing the affected discount in the Shopify admin, resulting in arbitrary JavaScript execution within the authenticated session.

## Description

When the discount details page loads, Shopify renders the comments containing the referenced product name without proper escaping, causing the injected HTML/JS to execute in the browser. The payload triggers an alert (proof-of-concept), but could be escalated to steal cookies, keylog, or perform actions on behalf of the staff user. This exploits the vulnerability introduced by discount timeline changes and requires only view access to discounts.

## Requirements

1. Authenticated Shopify staff account with discounts view permission
2. Access to the admin panel discounts section
3. Pre-existing discount with embedded malicious product reference

## Defense

Defensive measures and detection strategies:

- Apply HTML escaping to all rendered comments and referenced fields in admin views
- Enable strict CSP headers to prevent JS execution from inline sources
- Monitor for JS errors or alerts in admin session logs and use browser extensions to detect XSS

## Objectives

1. Render the discount to trigger payload execution
2. Demonstrate JS control in the admin context
3. Highlight potential for session hijacking or data exfiltration

## Instructions

### Step 1: Navigate to Affected Discount

**Context**: Open the discounts list and select the one with the malicious reference.

Use the UI to go to Discounts and click on the specific discount ID.

> Example URL: https://store.myshopify.com/admin/discounts/367541518396

### Step 2: Load Discount Details

**Context**: The page load will parse and render the comments, executing the payload.

Simply view the discount details page.

> Upon rendering, the img tag onerror should fire the alert(domain.domain).

### Step 3: Validate Execution

**Context**: Confirm the XSS has executed as expected.

Observe the alert popup or check browser console for JS errors/output.

> Success is indicated by the alert displaying the domain value; no further action needed.

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
- execution
- shopify-discounts
