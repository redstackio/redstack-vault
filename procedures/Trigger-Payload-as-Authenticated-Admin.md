---
tags:
  - execution
  - admin-context
  - xss-trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/inject-auto-shopify-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.194Z'
sub_techniques: []
id: d31e8e3b-ef88-448f-9c03-cf91163f061a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Payload-as-Authenticated-Admin

## Summary

Access the modified store page as an admin to activate the injected script, resulting in XSS execution within the admin session.

## Description

Visiting the page loads the theme script, which opens the admin/themes window and sends the exploitative postMessage. The embedded app processes it, assigning the javascript: URL and executing the payload.

## Requirements

1. Admin login credentials
2. Injected theme from prior step
3. Browser without popup blockers

## Defense

Defensive measures and detection strategies:

- Block cross-origin postMessages without validation
- Monitor for unexpected window.open from storefront
- Alert on javascript: redirects in app code

## Objectives

1. Confirm payload delivery and execution
2. Demonstrate admin JS execution
3. Highlight session compromise potential

## Instructions

### Step 1: Log In and Visit Page

**Context**: Ensure authenticated state for full impact.

Log in as admin, navigate to the storefront page with the injected theme.

> Expected output: Page loads, script executes (popup or auto).

### Step 2: Observe Exploitation

**Context**: Verify postMessage and redirect.

Watch for new window to /admin/themes, then alert from javascript:alert(document.domain) in admin context. Use [[commands/inject-auto-shopify-xss-payload]] for auto-trigger.

> Expected output: Alert pops in admin window, confirming domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/inject-auto-shopify-xss-payload]]

## Tools Used


## Tags

- [[Execution]]
- [[dom-xss]]
