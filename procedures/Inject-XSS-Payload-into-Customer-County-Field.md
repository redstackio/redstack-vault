---
tags:
  - xss
  - injection
  - payload
  - woocommerce
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
updated_at: '2025-12-13T23:52:34.330Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 92e14cc2-5548-4da3-95db-5f7a41e4f724
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-into-Customer-County-Field

## Summary

This procedure injects a JavaScript payload into the WooCommerce customer address county field during checkout or account editing, exploiting the lack of encoding to store it persistently for later execution in the admin context.

## Description

On a vulnerable WooCommerce 3.5.7 installation, the county field in billing details accepts user input without proper sanitization. By selecting UK as the country (which exposes the county field) and injecting a payload like '><img src=x onerror=alert(1) x=y' (noting that some tag filtering may strip the leading <), the input is saved to the database. This payload will be echoed unencoded in the WordPress admin user-edit.php page, leading to XSS when viewed by admins. The procedure can be performed via checkout after adding an item to cart or directly via /my-account/edit-address/.

## Requirements

1. Authenticated customer session.
2. Access to checkout or edit-address pages.
3. Knowledge of payload that bypasses basic filtering (e.g., img tag onerror).

## Defense

Defensive measures and detection strategies:

- Sanitize and encode all user inputs in address fields using esc_html() or similar in WooCommerce templates.
- Validate county field against whitelists for UK regions.
- Audit admin views for unencoded echoes from user data.

## Objectives

1. Store malicious JavaScript in the county field without immediate detection.
2. Ensure persistence in the customer profile database.
3. Bypass any client-side validation on the form.

## Instructions

### Step 1: Access Injection Point

**Context**: Reach the form exposing the vulnerable county field.

Add an item to cart and proceed to checkout, or go to http://192.168.0.101/wordpress/my-account/edit-address/billing/.

> Select UK as country to display the County field under Billing Details.

### Step 2: Enter and Submit Payload

**Context**: Inject the XSS string and save the address.

In the County field, enter: '><img src=x onerror=alert(1) x=y

> Complete the form submission; the payload should save without errors, though the leading < may be filtered.

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
- [[injection]]
- [[payload]]
