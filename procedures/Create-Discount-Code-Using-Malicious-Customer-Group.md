---
tags:
  - xss
  - discount
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
updated_at: '2025-12-14T03:15:31.965Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 151667d1-aeeb-492d-9069-959ecc85e702
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Discount-Code-Using-Malicious-Customer-Group

## Summary

This procedure selects the previously created malicious customer group during discount code creation in Shopify admin, positioning the unsanitized payload for reflection upon form submission.

## Description

Shopify's discounts interface allows applying discounts to specific customer groups. When selecting a group with an injected XSS payload, the name is displayed in the form without sanitization. This step bridges the injection phase to execution by incorporating the payload into the discount configuration. It requires admin access and assumes the malicious group from the prior procedure exists. The outcome sets the stage for JavaScript execution on save, enabling attacks like cookie theft in the admin context.

## Requirements

1. Existing malicious customer group from previous procedure.
2. Authenticated Shopify admin session.
3. Access to the Discounts section in the admin UI.

## Defense

Defensive measures and detection strategies:

- Enforce output encoding when rendering group names in forms (e.g., HTML entity encoding).
- Audit discount creation logs for suspicious group selections.
- Deploy web application firewall (WAF) rules to detect common XSS patterns in admin actions.

## Objectives

1. Integrate the malicious group into a new discount code.
2. Confirm the payload appears in the form without execution.
3. Advance toward triggering the reflection.

## Instructions

### Step 1: Navigate to Discounts

**Context**: Access the discounts creation area.

No command required; UI navigation:

- In Shopify admin, click "Discounts" in the left sidebar.
- Click "Create discount" and select "Discount code" type.

> Form loads for configuration.

### Step 2: Select Malicious Group

**Context**: Configure the discount to use the injected group.

No command required; UI selection:

- In the "Applies to" or customer selection section, choose "Specific customer segments".
- Search for and select the malicious group name containing the payload.
- Fill minimal required fields (e.g., discount code name, value).

> Payload is reflected in the UI as the group name. Expected output: Group selected, form ready for save.

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
- [[shopify]]
- [[discount]]
