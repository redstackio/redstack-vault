---
id: 123e4567-e89b-12d3-a456-426614174003
name: Save-Discount-to-Trigger-XSS
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:36.709Z'
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
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Save-Discount-to-Trigger-XSS

## Summary

This procedure finalizes the discount save, causing the unsanitized customer group name to reflect and execute the stored XSS payload in the admin browser.

## Description

Upon saving the discount, Shopify processes and redisplays the customer group name without proper encoding, injecting and running the JavaScript (e.g., prompt alert). This occurs in the authenticated admin context, allowing potential session theft or further exploits. Requires prior steps completed. Outcome: Immediate JS execution confirming vulnerability.

## Requirements

1. Discount form with malicious group selected
2. Admin session active
3. Browser with JS enabled

## Defense

Defensive measures and detection strategies:

- Encode all outputs in admin forms (e.g., HTML entity encoding)
- Implement XSS filters or WAF rules for admin endpoints
- Alert on JS errors or unexpected prompts in browser console

## Objectives

1. Trigger payload execution on save
2. Demonstrate arbitrary JS in admin context
3. Highlight impact like session hijacking

## Instructions

### Step 1: Review Form

**Context**: Ensure malicious group is selected before saving.

Double-check the discount form shows the group name with payload.

### Step 2: Execute Save

**Context**: Submit the form to process and reflect the input.

Click the 'Save' button on the discount creation form.

> The backend saves the discount, but frontend reflection executes `<img src=x onerror=prompt(7)>`, showing an alert.

### Step 3: Validate Execution

**Context**: Confirm XSS via alert and inspect for further impact.

Observe the prompt(7) alert. Check browser dev tools for executed script.

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
