---
tags:
  - xss-execution
  - admin-panel
  - session-theft
type: procedure
tools:
  - '[[tools/Custom-JavaScript-Exploit-Script]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - Shopify
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.860Z'
sub_techniques: []
id: 78faf7ba-daf2-4732-8581-bb55096bffb0
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-Execution-in-Admin-Panel

## Summary

This procedure describes how an admin's interaction with the tainted order details triggers the persistent XSS payload, leading to JavaScript execution in their browser and potential shop takeover.

## Description

Once the malicious order is placed, the unsanitized referer appears as a hyperlink in the Shopify admin's order view (e.g., under 'How did they find us?'). Clicking it executes the javascript: URI in the admin's context, allowing cookie theft or session hijacking. The PoC uses a script to exfiltrate data. Prerequisites: Admin access to the panel; attacker waits for view. Outcomes: Arbitrary JS execution, full compromise.

## Requirements

1. Admin login to Shopify dashboard
2. Access to the specific order with tainted referer
3. No attacker intervention needed post-persistence

## Defense

Defensive measures and detection strategies:

- Render referer as plain text, not clickable links
- Implement output encoding for all admin-displayed user inputs
- Use browser extensions or WAF to block javascript: URIs

## Objectives

1. Execute payload in privileged admin session
2. Exfiltrate sensitive data like cookies
3. Achieve account or shop takeover

## Instructions

### Step 1: Access Admin Panel and View Order

**Context**: Admin navigates to the vulnerable order.

**Instructions**: Log in to `https://admin.shopify.com/store/{store}` and go to Orders > select the malicious order.

> The referer field shows as `<a href="javascript:alert(document.cookie)">javascript:alert(document.cookie)</a>`.

### Step 2: Click the Tainted Link

**Context**: Trigger execution by interacting with the link.

**Instructions**: Click the referer hyperlink; the browser executes the JS payload, e.g., alerting cookies or sending to attacker server via the custom script.

> For PoC: Loads external script from `https://4cf3b563d73754fce54cf4936833f2ef021ec815.googledrive.com/.../1.js` to perform session theft.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-JavaScript-Exploit-Script]]

## Tags

- [[xss-execution]]
- [[session-theft]]
