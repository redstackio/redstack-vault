---
tags:
  - xss
  - self-xss
  - injection
  - shopify
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: e803678e-901b-4152-9eca-a28613b27050
created_at: '2025-12-14T17:28:28.489Z'
updated_at: '2025-12-14T17:28:28.489Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Inject-HTML-Payload-into-Email-Field

## Summary

This procedure demonstrates injecting an HTML payload into the email address field on Shopify's password reset page to exploit a self-reflected XSS vulnerability, resulting in the rendering of unsanitized input within the user's browser session.

## Description

The procedure targets the lack of proper input sanitization or escaping in the email field at https://accounts.shopify.com/password-reset/new. By entering HTML like `<h1 style="color:blue;">█████</h1>`, the payload is reflected and executed, changing text color on the page. This is a self-XSS, meaning it only affects the user who injects it, requiring manual payload pasting for script execution. The vulnerability has low severity (3.8) and no impact on other users, but highlights the need for robust client-side validation.

## Requirements

1. Web browser with developer tools for inspection
2. Public access to https://accounts.shopify.com/password-reset/new
3. Basic knowledge of HTML and XSS payloads

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization using libraries like DOMPurify on the client and server sides
- Use Content Security Policy (CSP) to restrict inline scripts and styles
- Monitor for anomalous form submissions or reflected content in logs

## Objectives

1. Inject and render HTML in the email field to confirm XSS
2. Demonstrate self-execution limitations
3. Validate vulnerability for reporting

## Instructions

### Step 1: Access the Target Page

**Context**: Navigate to the password reset form to locate the vulnerable email input.

No specific command required; use browser navigation to https://accounts.shopify.com/password-reset/new.

> The page should load the form with the email field ready for input.

### Step 2: Enter and Submit Payload

**Context**: Input the HTML payload to trigger reflection.

Enter the following into the email field:

```html
<h1 style="color:blue;">█████</h1>
```

Submit the form or observe the immediate reflection.

> The payload renders as a blue heading, confirming injection.

### Step 3: Verify Execution

**Context**: Inspect the page to ensure the HTML executes without sanitization.

Use browser developer tools (F12) to check the DOM for the injected element.

> Look for the `<h1>` tag in the HTML source, indicating successful rendering. Test extensions like adding `<script>alert(1)</script>` for JavaScript, but note self-XSS constraints.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[self-xss]]
- [[injection]]
