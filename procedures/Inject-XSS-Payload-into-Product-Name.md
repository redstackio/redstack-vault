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
updated_at: '2025-12-13T23:55:06.678Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: c2e545a3-e610-4627-9a01-7bc3fc0cd2c4
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Product-Name

## Summary

This procedure injects a stored XSS payload into a Shopify product's name field, exploiting improper escaping to store malicious JavaScript for later execution in the admin panel.

## Description

In Shopify's admin interface, product names are not adequately escaped after updates to discount timeline features, allowing HTML and JavaScript injection. An attacker with staff access creates a product using a payload like '"'><img src=x onerror=alert(domain.domain)>"' as the title. This stores the executable code, which can be referenced elsewhere to trigger XSS. The procedure requires authenticated access but no advanced tools, making it accessible for intermediate users targeting Shopify stores.

## Requirements

1. Authenticated Shopify staff account with products creation permission
2. Access to the admin panel (https://store.myshopify.com/admin/products)
3. Basic knowledge of XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement strict output encoding for all user-controlled fields like product names (e.g., use HTML entity encoding)
- Audit recent code changes, especially around discount timelines, for escaping regressions
- Monitor admin panel for unusual JavaScript alerts or DOM manipulations via browser dev tools

## Objectives

1. Store malicious JavaScript in a product name without triggering errors
2. Verify the payload is saved intact for later use
3. Set up for cross-context execution in discount views

## Instructions

### Step 1: Access Product Creation

**Context**: Log in to the Shopify admin and navigate to the products section to begin creation.

No command required; use the web UI to go to Products > Add product.

> Ensure you are in an authenticated session with necessary permissions.

### Step 2: Set Malicious Product Name

**Context**: Enter the XSS payload as the product title to inject the code.

Payload example:

```html
"'><img src=x onerror=alert(domain.domain)>'
```

> Paste this directly into the title field. Fill other fields minimally (e.g., blank description) and save. The payload breaks out of any quoting and injects an img tag with an onerror handler to execute the alert.

### Step 3: Save and Verify Product

**Context**: Confirm the product is created and the payload is stored without sanitization.

Save the product via the UI button.

> Refresh the products list; the title should display the raw payload, indicating successful injection.

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
- shopify-products
