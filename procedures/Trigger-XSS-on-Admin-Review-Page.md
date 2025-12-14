---
tags:
  - xss
  - trigger
  - admin-panel
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
updated_at: '2025-12-13T23:52:39.101Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: e6a74290-f8ad-49d2-b5ef-367033d8e761
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Admin-Review-Page

## Summary

This procedure simulates or directs access to the Zomato admin panel's reviews_new page, where the stored XSS payload in the reported review's additional_text is rendered unsanitized, initiating execution.

## Description

Once the malicious report is stored, an admin viewing the report at https://www.zomato.com/admin/reviews_new?review_id={ID} will cause the additional_text to be inserted as innerHTML, executing the script. This blind XSS relies on admin interaction. The target environment is the web-based admin panel integrated with the mobile app's reporting. Expected outcome: Payload renders and begins execution upon page load.

## Requirements

1. Reported review ID from previous step
2. Admin credentials or simulation (e.g., social engineering to lure admin)
3. Browser access to Zomato admin domain

## Defense

Defensive measures and detection strategies:

- Render user-generated content in isolated iframes with strict CSP
- Audit admin views for XSS patterns in logs
- Implement client-side sanitization on admin panel

## Objectives

1. Cause rendering of unsanitized additional_text
2. Initiate XSS in admin browser context
3. Enable subsequent JS actions

## Instructions

### Step 1: Navigate to Admin Page

**Context**: Use the reported review ID to construct and visit the trigger URL, simulating admin access.

**Command** (Browser-based; no CLI):

> Open browser and visit: https://www.zomato.com/admin/reviews_new?review_id=32288944

> Expected output: Page loads showing review details, with additional_text rendered as HTML.

### Step 2: Confirm Rendering

**Context**: Inspect the page source or DOM to verify the payload is present unescaped.

**Command** (Use browser dev tools):

> In browser console: document.querySelector('[contains additional_text]').innerHTML

> Expected output: Raw HTML including <script> tag visible in DOM.

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
- [[trigger]]
