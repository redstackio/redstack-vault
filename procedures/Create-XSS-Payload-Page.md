---
id: proc-001
tags:
  - xss
  - payload-creation
type: procedure
tools:
  - '[[tools/Google-Chrome]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/xss-alert-and-log-sensitive-data]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:18.439Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-XSS-Payload-Page

## Summary

This procedure creates a custom Shopify storefront page containing a JavaScript XSS payload designed to alert and log sensitive admin data when loaded into the admin panel frame via path traversal.

## Description

In the context of exploiting Shopify's admin panel vulnerability, this step involves creating a page at '/pages/xss' with a script that executes DOM-based XSS upon loading. The payload targets admin-specific elements like CSRF tokens and logs cookies, window objects, and location for data exfiltration. Prerequisites include Shopify store access to create pages.

## Requirements

1. Shopify admin access to create custom pages
2. Knowledge of target store URL (e.g., [STORE].myshopify.com)
3. Browser for testing page creation

## Defense

Defensive measures and detection strategies:

- Sanitize user-controlled paths in route handlers
- Implement Content Security Policy (CSP) to block inline scripts
- Monitor for anomalous postMessage events in admin JavaScript

## Objectives

1. Establish a payload page for later injection into admin context
2. Ensure payload captures sensitive admin data
3. Verify page loads without triggering store defenses

## Instructions

### Step 1: Access Shopify Page Editor

**Context**: Log into Shopify admin and navigate to create a new page.

**Command** ([[commands/xss-alert-and-log-sensitive-data]]):
```html
<script>alert("XSS By Tiago")console.log("Document:", document)console.log("Window:", window)console.log("Cookies:", document.cookie)console.log("Location:", window.location)console.log("CSRF Token:", document.querySelectorAll('[data-serialized-id="csrf"]')[0].innerText)</script>
```

> This injects the XSS script into the page content. Save the page with title 'xss' and handle '/pages/xss'. Expected output: Page publishes successfully.

### Step 2: Test Page Load

**Context**: Verify the page loads the payload without errors.

**Instructions**: Navigate to https://[STORE].myshopify.com/pages/xss in browser.

> No alert should fire yet; console should be clean until triggered in admin.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/xss-alert-and-log-sensitive-data]]

## Tools Used

- [[tools/Google-Chrome]]

## Tags

- xss
- payload-creation
