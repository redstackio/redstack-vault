---
tags:
  - xss
  - execution
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:31.963Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 48974046-193b-4961-98f1-ce481679feee
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Saving-Discount-in-Shopify-Admin

## Summary

This procedure finalizes the XSS attack by saving the discount code, causing the unsanitized customer group name to be reflected and execute arbitrary JavaScript in the authenticated admin's browser.

## Description

Upon saving a discount configured with a malicious customer group, Shopify's interface renders the group name without proper HTML escaping, triggering the stored XSS payload. This executes in the high-privilege admin context, allowing attackers to steal session cookies, perform admin actions, or exfiltrate sensitive data. The procedure builds on prior injection and selection steps, requiring only the save action. Impact includes full admin compromise if exploited further (e.g., with more advanced payloads).

## Requirements

1. Configured discount form with malicious group selected.
2. Active admin session in the browser.
3. Payload designed for immediate execution (e.g., onerror handler).

## Defense

Defensive measures and detection strategies:

- Apply strict HTML escaping to all reflected user inputs in admin forms.
- Implement client-side validation and CSP to block unsafe scripts.
- Log and alert on JavaScript errors or unexpected DOM manipulations in admin sessions.

## Objectives

1. Execute the XSS payload via form submission.
2. Confirm arbitrary code execution in admin context.
3. Demonstrate potential for data theft or session hijacking.

## Instructions

### Step 1: Review and Prepare Form

**Context**: Ensure the discount is ready for save with payload in place.

No command required; UI review:

- Verify the malicious group is selected in the discount form.
- Complete any mandatory fields (e.g., discount percentage).

> Form should display the payload visibly but not execute yet.

### Step 2: Save Discount to Trigger Execution

**Context**: Submit the form to reflect and run the payload.

No command required; UI submission:

- Click the "Save" button at the bottom of the discount creation form.

> The save action renders the group name, executing the payload (e.g., prompt(7) alert). Expected output: JavaScript runs, such as a browser alert confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[shopify]]
