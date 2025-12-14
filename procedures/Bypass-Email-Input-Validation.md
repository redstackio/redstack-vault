---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - bypass
  - client-side
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
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
updated_at: '2025-12-13T23:52:25.305Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Bypass-Email-Input-Validation

## Summary

This procedure uses browser developer tools to change the email input type from 'email' to 'text', bypassing client-side restrictions on special characters for XSS injection.

## Description

In the Shopify Product Reviews self-XSS scenario, the email field uses type='email' to enforce valid email formats, blocking JS payloads. By editing the DOM via dev tools, this validation is circumvented. Target is the review form; prerequisites include form access. Outcome: Input accepts arbitrary strings like script tags.

## Requirements

1. Open review form in browser
2. Developer tools enabled (F12)
3. Basic HTML inspection knowledge

## Defense

Defensive measures and detection strategies:

- Server-side validation of email formats regardless of client-side
- Monitor for unusual input patterns in logs
- Use Content Security Policy (CSP) to block inline scripts

## Objectives

1. Remove browser-enforced email validation
2. Enable payload injection
3. Maintain form functionality for submission

## Instructions

### Step 1: Open Developer Tools

**Context**: Access inspection features.

Press F12 or right-click and select 'Inspect' to open dev tools on the review form page.

### Step 2: Locate and Modify Input

**Context**: Target the email field attribute.

In the Elements tab, find the <input type="email" ...> element for the email field. Double-click the 'type' attribute and change it to 'type="text"'. Press Enter to apply.

> The field should now allow typing < > and other characters without the browser's popup validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- xss
- bypass
- client-side
