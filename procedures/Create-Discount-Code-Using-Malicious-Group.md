---
id: 123e4567-e89b-12d3-a456-426614174002
name: Create-Discount-Code-Using-Malicious-Group
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.712Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - stored-xss
  - shopify
platforms:
  - Web
commands: []
tools: []
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Create-Discount-Code-Using-Malicious-Group

## Summary

This procedure selects the malicious customer group in a new discount code form, positioning the stored XSS payload for reflection upon saving.

## Description

Shopify's Discounts section allows conditions based on customer groups. By selecting the group with the injected payload, the name is loaded into the form. No execution occurs here, but it sets up the unsanitized reflection. Requires the malicious group from prior steps and admin access. Outcome: Form populated with payload visible but inert.

## Requirements

1. Malicious customer group already created
2. Authenticated admin access
3. Web browser

## Defense

Defensive measures and detection strategies:

- Sanitize group names when rendering in forms
- Validate discount conditions server-side
- Log unusual group selections in admin actions

## Objectives

1. Load stored payload into discount form
2. Avoid premature execution
3. Prepare for save-triggered reflection

## Instructions

### Step 1: Navigate to Discounts

**Context**: Access the discount creation interface.

From admin dashboard, go to Discounts > Create discount > Discount code.

### Step 2: Configure Discount Basics

**Context**: Set up a simple discount to reach conditions.

Enter a code name (e.g., 'TEST10') and set a percentage off (e.g., 10%).

### Step 3: Select Malicious Group

**Context**: Apply the condition using the injected group.

Under 'Applies to', select 'Specific customer segments'. Choose the malicious group from the dropdown.

> The group name with payload appears in the form without escaping.

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
- [[stored-xss]]
- [[shopify]]
