---
id: proc-okru-dialog-xss-001
tags:
  - xss
  - stored-xss
  - ok.ru
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
updated_at: '2025-12-13T23:52:34.263Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Contact-Seller-Dialog

## Summary

This procedure triggers the execution of a stored XSS payload embedded in an ok.ru group market product title by opening the 'Contact seller' dialog, which renders the title without sanitization, allowing JavaScript execution in the victim's session.

## Description

In the mobile version of ok.ru, the 'Contact seller' feature displays product titles in a dialog box. Due to missing output encoding, stored payloads in titles (e.g., attribute breakouts) execute as JavaScript when the dialog loads. This procedure assumes the payload is already stored and focuses on the trigger mechanism, applicable to any victim viewing the product. Outcomes include alert popups for proof-of-concept or exfiltration of session data like cookies.

## Requirements

1. Access to the group market page with an infected product (https://m.ok.ru/group/54904397693159/market).
2. Logged-in session as a victim user.
3. Standard web browser.

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs and encode outputs in dynamic HTML contexts.
- Employ browser-based protections like XSS auditors or strict CSP headers.
- Log and alert on unexpected script executions in user dialogs.

## Objectives

1. Open the vulnerable dialog to render the payload.
2. Execute JavaScript in the victim's browser context.
3. Exfiltrate sensitive data such as session cookies.

## Instructions

### Step 1: Navigate to Affected Product

**Context**: Load the group market page and locate the product with the stored payload.

Visit https://m.ok.ru/group/54904397693159/market and identify the single listed product.

> Expected output: Product visible on the page.

### Step 2: Initiate Contact Seller Action

**Context**: Click the button to trigger the dialog, causing payload execution.

Select the product and click 'Связаться с продавцом'.

> Expected output: Dialog opens, and onerror handler in the img tag executes the alert or custom script.

### Step 3: Validate Execution and Exfiltration

**Context**: Confirm impact by checking for alerts or monitoring network traffic.

Use browser console (F12 > Console) to observe any logged errors or use a proxy to capture requests if exfiltrating data.

> Expected output: Alert box appears or data sent to attacker server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- dialog-exploit
- session-theft
