---
tags:
  - xss
  - cookie-injection
type: procedure
tools:
  - '[[tools/Browser-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:33.602Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: a500f17f-47b0-447b-8686-1f8dd941b518
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Set-Malicious-_landing_page-Cookie

## Summary

This procedure injects a JavaScript URI payload into Shopify's _landing_page cookie using browser tools, preparing it for storage during guest checkout to enable stored XSS in the admin panel.

## Description

In the context of a Shopify storefront, the _landing_page cookie tracks the referring page for analytics. By setting it to a javascript: URI, an attacker can store executable code in order data. This targets guest users and requires no authentication, but execution occurs only when admins view the order. Prerequisites include access to the public shop URL and a browser with dev tools.

## Requirements

1. Access to the Shopify storefront (e.g., [shop].myshopify.com)
2. Browser with developer tools (Chrome/Firefox)
3. No special permissions needed

## Defense

Defensive measures and detection strategies:

- Sanitize all cookie values before storage, rejecting javascript: URIs
- Implement Content Security Policy (CSP) to block inline JS execution in admin panels
- Monitor for anomalous cookie values in order data via logging

## Objectives

1. Set cookie to malicious payload without triggering immediate alerts
2. Ensure payload is a valid javascript: URI for link execution
3. Prepare for persistence in order metadata

## Instructions

### Step 1: Navigate to Storefront

**Context**: Access the target shop as a guest to establish the cookie context.

Open your browser and go to `[shop].myshopify.com/`.

> Verify the page loads without errors; no cookie set yet.

### Step 2: Open Developer Tools and Set Cookie

**Context**: Use dev tools to modify the _landing_page cookie directly.

Right-click on the page, select Inspect, go to the Application/Storage tab, expand Cookies, select the domain, and edit or add the _landing_page key with value `javascript:alert(1)` (replace with advanced payload for real attacks, e.g., to exfiltrate CSRF tokens).

> Expected: Cookie updates in the list; refresh the page to confirm persistence. No execution occurs until stored and clicked.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Developer-Tools]]

## Tags

- [[xss]]
- [[cookie-injection]]
